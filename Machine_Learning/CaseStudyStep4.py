import pandas as pd

import matplotlib.pyplot as plt     # use to Visualisation
import seaborn as sns               # use to Visualisation

Border = "*"*55
####################################################
# Step 1 : Load the Dataset
####################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("Dataset Loaded Succesfully")
print("Initial entries from dataset are :")
print(df.head())

####################################################
# Step 2 : Data Analysis (EDA)
####################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of dataset : ",df.shape)

print("Column name : ",list(df.columns))

print("Missing Values per column : ")
print(df.isnull().sum())                # total missing values + total count

print("Class distribution (species count)")
print(df["species"].value_counts())         # species all column

print("Statistical report of dataset : ")
print(df.describe())

######################################################
# Step 3 : Decide Independent and Dependent Variables
######################################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X : Independent Variable / Fetures
# Y : Dependent Variables / Labels

feture_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]

X = df[feture_cols]
Y = df["species"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)

######################################################
# Step 4 : Visualisation of Dataset
######################################################

print(Border)
print("Step 4 : Visualisation of Dataset")
print(Border)

# Scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)

plt.title("Marvellous Iris case study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()