import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gravity_and_stars.csv")

mass = df["mass"].tolist()
gravity = df["gravity"].tolist()
radius = df["radius"].tolist()

mass = mass.sort()
gravity = gravity.sort()
radius = radius.sort()

plt.plot(mass,radius)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.title("Radius and mass")

plt.plot(mass,gravity)
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.title("Gravity and mass")

plt.plot(mass,radius)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.title("Radius and mass")