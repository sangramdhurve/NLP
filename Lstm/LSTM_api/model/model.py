import pickle


def load_model():
    #return pickle.load(MODELS_PATH)

    # Open the file in binary mode
    with open("model/LSTM_v2.pkl", 'rb') as file:
      
    # Call load method to deserialze
        modl = pickle.load(file)
        return modl

# LOADED_MODEL = load_model()