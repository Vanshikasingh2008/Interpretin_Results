import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('filtered_version.csv')  

star = df["Star_name"].tolist()
mass = df["mass"].tolist()
radius=df["radius"].tolist()
gravity = df["gravity"].tolist()
distance = df["distance"].tolist()

plt.figure(figsize=(10,5))
plt.title("Stars vs Mass")
plt.bar(star[0:9],mass[0:9])

plt.figure(figsize=(10,5))
plt.title("Stars vs Radius")
plt.bar(star[0:9],radius[0:9])

plt.figure(figsize=(10,5))
plt.title("Stars vs Gravity")
plt.bar(star[0:9],gravity[0:9])

plt.figure(figsize=(10,5))
plt.title("Stars vs Distance")
plt.bar(star[0:9],distance[0:9])