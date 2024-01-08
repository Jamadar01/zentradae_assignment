import requests
import pandas as pd


def fetch_json(data_url):
    response = requests.get(data_url)
    data = response.json()
    return data['products']  


def datastorage(data):
   
    dataframe = pd.DataFrame.from_dict(data, orient='index')
    
   
    dataframe['price'] = pd.to_numeric(dataframe['price'])
    dataframe['popularity'] = pd.to_numeric(dataframe['popularity'])
    
   
    dataframe = dataframe.sort_values(by='popularity', ascending=False)
    
    return dataframe


def display(dataframe):
    print(dataframe)


url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'


data = fetch_json(url)
dataframe = datastorage(data)
display(dataframe)
