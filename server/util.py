import json,pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    #Create Input Array
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print('Loading Saved Artifacts Started . . . ')
    global __locations
    global __data_columns
    global __model
    
    with open ('C:/Users/Administrator/Desktop/Deep LearNNN/Machine Learning Startttttttt/First ML Project/BHP/server/artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]


    with open('C:/Users/Administrator/Desktop/Deep LearNNN/Machine Learning Startttttttt/First ML Project/BHP/server/artifacts/Bengaluru_Home_Prices_Model.pickle', 'rb') as f:
        __model = pickle.load(f)
    
    print("Loading Artifacts Done . . .")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())