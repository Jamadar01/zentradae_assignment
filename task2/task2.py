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


def save_as_json(dataframe, file_name):
    # Convert DataFrame back to JSON
    json_data = dataframe.to_json(orient='index')
    
    # Save JSON data to a file
    with open(file_name, 'w') as file:
        file.write(json_data)


url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'
data = fetch_json(url)
dataframe = datastorage(data)
display(dataframe)

# Save the DataFrame as a JSON file
save_as_json(dataframe, 'output.json')
