import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gravity_and_stars.csv')  

del df['radius']
del df['mass']

dist = df['distance'].tolist()
grav = df['gravity'].tolist()

count=0
for d in dist:
    if(d>100):
        count = count+1
        del df.loc[count]

count2=0
for g in grav:
    if(g<150 or g>350):
        count2 = count2+1
        del df.loc[count]

df.to_csv("filtered_version.csv")