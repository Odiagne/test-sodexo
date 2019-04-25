import pandas as pd


def import_data(file_name):
    '''
        Function to import a specific json file located in the folder data into a dataframe
    '''
    try:
        data = pd.read_json("../data/{}".format(file_name))
    except:
        print("The import of {} has failed".format(file_name))
        exit(0)

    return data

def str_to_none(value):
    '''
        Function to set to None every value of type different to None.
        In the longitude and latitude values we sometimes have values like "not relevant".
        This function help to deal with those values
    '''
    if isinstance(value,float):
        res = value
    else:
        res = None
    return res

def replace_with_coordinates(row, coord):
    '''
        This function applied to a data frame will help to replace missing longitude or latitude by the value of the column coordinates if not null.
        It will be applied to a row of a data frame.
    '''
    if (pd.isna(row[coord]) and pd.notna(row.coordinates)):
        res = row.coordinates[coord]
    else:
        res = row[coord]
    return res

def data_without_na(data):
    '''
        Function to return only row without nan in longitude and latitude.
    '''
    return data[data.apply(lambda x: (pd.notna(x.latitude) and pd.notna(x.longitude)), 1)]

def data_with_na(data):
    '''
        Function to return rows with a missing value on longitude or latitude.
    '''
    return data[data.apply(lambda x: (pd.isna(x.latitude) or pd.isna(x.longitude)), 1)]

if __name__ == "__main__":
    data = import_data("Brisbane_CityBike.json")
    data['longitude']=data.apply(lambda x: str_to_none(x.longitude), axis=1)
    data['latitude']=data.apply(lambda x: str_to_none(x.latitude), axis=1)
    data['latitude'] = data.apply(lambda x: replace_with_coordinates(x, 'latitude'), axis=1)    
    data['longitude'] = data.apply(lambda x: replace_with_coordinates(x, 'longitude'), axis=1)
    data_wo_na = data_without_na(data)
    data_na = data_with_na(data)
    print(data_wo_na[['latitude', 'longitude']][142:146])
    print(data_na[['id','latitude', 'longitude']])