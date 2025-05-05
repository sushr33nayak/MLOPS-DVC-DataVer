import pandas as pd 
import os

#create sample dataframes which have column names
data={'Name':['Alice','Bob','Charlie'],
       'Age':[25,30,34],
       'City':['NY','Ohio','Chicago']}

df=pd.DataFrame(data)

## adding new row to df for V2
new_row_loc={'Name': 'Sushree','Age':20,'City':'Dallas'}
df.loc[len(df.index)]=new_row_loc


data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print(f"CSV file saved to{file_path}")