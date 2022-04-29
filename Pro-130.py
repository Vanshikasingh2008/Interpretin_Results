import pandas as pd

df = pd.read_csv('unit.csv')
df.head()

del df['luminosity']
del df['radius']
del df['mass']

df = df[df['mass'].notna()]
df = df[df['radius'].notna()]

df.to_csv('clean.csv')