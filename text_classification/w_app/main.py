from fastapi import FastAPI
import pickle
import pandas as pd
import uvicorn
import txt_preprocessing
import time



MODELS_PATH = "models/ensemble_model_pklV2.pkl"


def load_model():
    #return pickle.load(MODELS_PATH)

    # Open the file in binary mode
    with open(MODELS_PATH, 'rb') as file:
      
    # Call load method to deserialze
        modl = pickle.load(file)
        return modl

LOADED_MODEL = load_model()

app = FastAPI(title="Cyber Analysis", description="API to predict CyberThreat on tweets", debug=True)


def time_cal(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " :mili sec")
        return result
    return timer

@time_cal
def make_inference_df(input_text):
    
    # create dataframe and preprocess that
    i_txt = pd.DataFrame({"in_text": str(input_text)}, index=[0])
    pre_text = txt_preprocessing.preprocess_text(i_txt["in_text"][0])
    test_vectors = pre_text.reshape(1, -1)
    return test_vectors

# input_text = "Experts Explain the Threats and Opportunities for Artificial Intelligence and the Economy. An Article on Disadvantages & Benefits of Artificial Intelligence Technology."
# test = make_inference_df(input_text)
# print(test)

@app.get("/")
def read_root():

    return {"message": "Welcome to the API"}

@app.get("/predict/")
def predict(text: str):
    model_input = make_inference_df(text)
    prediction = LOADED_MODEL.predict_proba(model_input)

    if prediction[0][0] < 0.8:
        print(prediction[0][0])
        return " It's not a cyber crime"

    else:
        print(prediction[0][1])
        return "Be aware it a cyber crime"


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)