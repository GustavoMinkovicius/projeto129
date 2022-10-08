from heapq import merge
import pandas as pd

df1 = pd.read_csv('C:/Users/user/OneDrive/Área de Trabalho/programa/projeto127/dwarf_stars.csv')
df2 = pd.read_csv('C:/Users/user/OneDrive/Área de Trabalho/programa/projeto127/dwarf_stars.csv')

df1.dropna()

df1['Mass'].float(df1['Mass'])
df1['Radius'].float(df1['Radius'])

df1['Radius'] = df1['Radius'] *0.102763
df1['Mass'] = df1['Mass'] * 0.000954588


dfinal = pd.merge(df1,df2)


dfinal.to_csv('final.csv')
