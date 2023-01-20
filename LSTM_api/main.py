from fastapi import FastAPI
import fasttext
import pandas as pd
import uvicorn
import data_preprocessing
import time
import logging
from model.model import load_model
from pydantic import BaseModel


class Datavalid(BaseModel):
    text : str



# Load The Model
LOADED_MODEL = load_model()



app = FastAPI(title="Cyber Analysis", description="API to predict CyberThreat on tweets", debug=True)


logging.basicConfig(filename='text_api.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S')

# Create decorator for time calculation
def time_cal(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " :mili sec==> TIME")
        return result
    return timer

@time_cal
def make_inference_df(input_text):
    
    # create dataframe and preprocess that
    i_txt = pd.DataFrame({"in_text": str(input_text)}, index=[0])
    pre_text = data_preprocessing.preprocessAndEncode(i_txt['in_text'][0]) #i_txt["in_text"][0]
    return pre_text
logging.debug("Preprocessing has been done!")
# input_text = "Experts Explain the Threats and Opportunities for Artificial Intelligence and the Economy. An Article on Disadvantages & Benefits of Artificial Intelligence Technology."
# test = make_inference_df(input_text)
# print(test)


@app.get("/")
def read_root():

    return {"message": "Welcome to the API"}


@app.post("/predict")
def predict(text: Datavalid):
    model_input = make_inference_df(text)
    prediction = LOADED_MODEL.predict(model_input)
    print(prediction)

    if round(prediction[0][0],2) < 0.4 :
        tex= "Wallah!, Its not a cyber crime Enjoy"
    else:
        tex = "Its a cyber crime, Be aware"
    return {
        round(prediction[0][0]) : f"{tex} and score is {prediction}"
        }

logging.info("Prediction has been done!")
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)