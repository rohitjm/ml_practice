import pandas as pd
import numpy as np

df = pd.read_csv('example.csv')
print(df)
data = df.to_dict()
print(data)

data2 = {'Column1':{10:11}, 'Column2':{10:'G'}, 'Column3': {10:15}}
df2 = pd.DataFrame(data2)

## Types
print(f"type of data frame 1 {type(df)}")
print(f"type of data frame 2 {type(df2)}")
print(f"type of a column {df['Column2']}")

## Concat
print(pd.concat([df,df2], axis = 0))

## Merge
print(pd.merge(left=df, right=df2, on='Column1', how='outer'))

## Info
print(df.info())

## Describe
print(df.describe())

## Head() & Tail() & Shape()
print(df.head())
print(df.head(10))
print(df.tail())
print(df.tail(10))
print(df.shape)
print(df.index) # Essentially the number of rows
print(df.columns)

## Rename
renamed_df = df.rename(index = {1:'Person2'}, columns = {'Column1': 'id'})
print(renamed_df)

