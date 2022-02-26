import pandas as pd
from pandas import DataFrame as df

sheet_url = "https://docs.google.com/spreadsheets/d/1BZSPhk1LDrx8ytywMHWVpCqbm8URTxTJrIRkD7PnGTM/edit#gid=0"

url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")

df = pd.read_csv(url_1)
df = df.head(5)

df1 = df[['Asin', 'country']]

#for row in df1:
   # a, b = df1[row]

for i, row in df1.iterrows():
    asin = row['Asin']
    country = row['country']
    site = "https://www.amazon.{}/dp/{}".format(country, asin)
    print (site)
