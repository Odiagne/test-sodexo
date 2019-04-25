import os
from dotenv import load_dotenv
from sklearn.cluster import KMeans
from datamanagement import *

load_dotenv(dotenv_path='../.env')
def cleaning_data(file_name):
    '''
        Function to import and clean data 
    '''
    data = import_data(file_name)
    data['longitude']=data.apply(lambda x: str_to_none(x.longitude), axis=1)
    data['latitude']=data.apply(lambda x: str_to_none(x.latitude), axis=1)
    data['latitude'] = data.apply(lambda x: replace_with_coordinates(x, 'latitude'), axis=1)    
    data['longitude'] = data.apply(lambda x: replace_with_coordinates(x, 'longitude'), axis=1)
    return data_without_na(data)

def make_clusters(data, nb_clusters):
    '''
        Fonction to make clusters of coordinates
    '''
    kmeans = KMeans(n_clusters=nb_clusters, random_state=0).fit(data[['latitude', 'longitude']].values)
    data['clusters'] = kmeans.labels_
    return data

def export_result(data, file_name):
    data.to_json('../output/{}'.format(file_name), orient='records')
    print("---------END---------")


if __name__ == "__main__":
    data_wo_na = cleaning_data(os.environ['INPUT_FILE'])
    data_clusters = make_clusters(data_wo_na, 2)
    export_result(data_clusters, 'result.json')