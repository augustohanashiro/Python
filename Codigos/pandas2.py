import pandas as pd 

uri = "https://raw.githubusercontent.com/augustohanashiro/introducao-a-data-science/master/aula1.2/ratings.csv"

df = pd.read_csv(uri)

df.head()