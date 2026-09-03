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

#----------------------------------------------------------------------
#   Function Name : LoadData
#   Description :   Load the data from csv
#   Input :         None
#   Output :        None
#   Author :        Tushar Vijay Shilimkar
#   Date :          16/08/2026
#----------------------------------------------------------------------

def main():
    LoadData("MarvellousTitanicDataset.csv")


if __name__ == "__main__":
    main()