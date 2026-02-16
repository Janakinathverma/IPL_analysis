import pandas as pd
#read IPL.csv and return its datastructure
df = pd.read_csv("data/IPL.csv", low_memory=False)
print(df.columns.tolist())