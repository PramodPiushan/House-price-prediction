import pickle
import json

import numpy as np

__locations = None
__data_columns = None
__model = None

def predict_Home_price(Baths,Beds,Land_size,House_size,location):
    try:
        location_index = __data_columns.index(location.lower())
    except:
        crop_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Baths
    x[1] = Beds
    x[2] = Land_size
    x[3] = House_size
    if location_index>=0:
        x[location_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns_house.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]

    global __model
    if __model is None:
        with open('./artifacts/House_price_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(predict_Home_price(2,2,10.0,2000.0,'Wellampitiya'))
