import pandas as pd

data = pd.read_csv('in/tables/titanic.csv')
data_male = data[data['Sex']=='male']
data_female = data[data['Sex']!='male']
    
data_male.reset_index(drop=True, inplace=True)
data_female.reset_index(drop=True, inplace=True)
    
data_female.to_csv('out/tables/titanic_filter_female.csv')
data_male.to_csv('out/tables/titanic_filter_male.csv')
