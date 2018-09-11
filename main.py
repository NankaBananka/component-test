#import necessary libraries
import requests
import json
import pandas as pd

#obtain url property from config.json file
with open('/data/config.json') as f:
    json_data = json.load(f)
    url = json_data['parameters']['url']
    path = json_data['parameters']['path']
    name = json_data['parameters']['name']
    
#request url and save response into variable
r = requests.get(url)

#create or open (if exists) output file for writing and write the content of the response
with open('/data/out/tables/titanic.csv', 'wb') as f:
    f.write(r.content)

#read output file and print to console log first 10 rows
data = pd.read_csv('/data/out/tables/titanic.csv', header=0)

print(data.loc[0:10,["Name", "Survived"]])
