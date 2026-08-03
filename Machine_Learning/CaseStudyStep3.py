import pandas as pd

Border = "*"*50
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