#import necessary libraries
import requests
import pandas as pd

#request url and save response to variable
url = 'http://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
r = requests.get(url)

#create or open (if exist) output file for writing and write the content of the response
with open('out/tables/titanic.csv', 'wb') as f:  
    f.write(r.content)

#read output file and print to console log first 10 rows
data = pd.read_csv('out/tables/titanic.csv', header=0)
print(data.loc[0:10,["Name", "Survived"]])
