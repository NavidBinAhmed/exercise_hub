#collect and integrate data into warehouse using API

'''import requests
import pandas as pd
from sqlalchemy import create_engine

# Step 1: Define the API endpoint and parameters
base_url = "https://api.navid.com/v1/info"
api_key = 'dsbjhsd-asfbg-ajdg' #"your_api_key"
params = {
    'location': 'New York',
    'units': 'metric',
    'apikey': api_key
}

# Step 2: Make the API request
response = requests.get(base_url, params=params)

# Step 3: Check the response status and process data
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    print(f"The temperature in New York is {temperature}°C with {weather_description}.")
    
    # Step 4: Transform the data into a DataFrame
    df = pd.json_normalize(data)
    
    # Step 5: Load data into PostgreSQL
    db_url = "postgresql://username:password@host:port/database"
    engine = create_engine(db_url)
    df.to_sql('weather_data', engine, if_exists='append', index=False)
    
    print("Data loaded into the database successfully!")
else:
    print(f"Failed to retrieve data: {response.status_code}")

''''''
class
Arg: update ID, Update name

'''

'''class Identity:
#initialization
    update_ID = " "
    update_name = " "

    def __init__(self, update_ID, update_name):
        self.update_ID = update_ID
        self.update_name = update_name

    @classmethod
    def results(self):
        print("The class performed well.")


student_1 = Identity("1234", "navid")
print(student_1.update_ID)
print(student_1.results())'''