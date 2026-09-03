import pandas as pd
import numpy as np
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#----------------------------------------------------------------------
#   Function Name : LoadData
#   Description :   Load the data from csv
#   Input :         Name of csv file
#   Output :        Data frame
#   Author :        Tushar Vijay Shilimkar
#   Date :          16/08/2026
#----------------------------------------------------------------------

def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset loaded succefully")
    print(df.head())
    return df

# Step 2 : Data Preprocessing

#----------------------------------------------------------------------
#   Function Name : PreprocessData
#   Description :   It performs data analysis
#   Input :         Data frme
#   Output :        Updated Data frame
#   Author :        Tushar Vijay Shilimkar
#   Date :          16/08/2026
#----------------------------------------------------------------------

def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors = "ignore"
    )

    # Handle mmissing values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Convert categorical to numeric data
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )
    
    print(df.head())

    print("Data preprocessing completed")

    return df

# Step 3 : Split data

#----------------------------------------------------------------------
#   Function Name : SplitData
#   Description :   It performs Spliting Activity
#   Input :         Data frme
#   Output :        4 Subsets for training and testing
#   Author :        Tushar Vijay Shilimkar
#   Date :          16/08/2026
#----------------------------------------------------------------------

def SplitData(df):
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Dataset Spliting complited succesfully...")
    return X_train, X_test, Y_train, Y_test 

#----------------------------------------------------------------------
#   Function Name : main
#   Description :   Entry point Function
#   Input :         None
#   Output :        None
#   Author :        Tushar Vijay Shilimkar
#   Date :          16/08/2026
#----------------------------------------------------------------------

def main():
    # Step 1
    df = LoadData("MarvellousTitanicDataset.csv")

    # Step 2
    df = PreprocessData(df)

    # Step 3
    X_train, X_test, Y_train, Y_test  = SplitData(df)

if __name__ == "__main__":
    main()