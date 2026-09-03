import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
import pickle

def winee(path):
    df=pd.read_csv(path)
    print(df.columns)

    X = df.drop(columns=['Class'])
    Y = df['Class']


    obj=MinMaxScaler()
    X=obj.fit_transform(X)


    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2, random_state=43)


    model=SVC()

    model.fit(x_train,y_train)

    prediction=accuracy_score(y_test,model.predict(x_test))

    print(f"accruracy score:{prediction*100}")

    pickle.dump(model,open('wine_pickel.pkl','wb'))
    print(f"pickel file saved successfully!!")

def main():
    winee("WinePredictor.csv")

if __name__ == "__main__":
    main()



