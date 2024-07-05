import pandas as pd

csv_path = 'samples\country-list.csv'
df = pd.read_csv(csv_path)

field1 = df['country']
field2 = df['capital']
# print(df)


fields = df[['country', 'capital']]
df['fields'] = df[['country', 'capital']].apply(lambda x: x.tolist(), axis=1)

# print(df['combined'])
np_array_specific_columns = df[['country', 'capital']].to_numpy()
print(len(np_array_specific_columns))
    # print(np_array_specific_columns[i])
# print(np_array_specific_columns[])
