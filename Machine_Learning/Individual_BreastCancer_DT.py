import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


#----------------------------------
# Step 1 : Load the Dataset
#----------------------------------

df = pd.read_csv("breast_cancer.csv")

print("Shape of Dataset : ", df.shape)
print(df.head())

#-------------------------------------
# Step 2 : Seprate fetures and labels
#-------------------------------------

X = df.drop("target", axis=1)
Y = df["target"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

#------------------------------------------------
# Step 3 : Split dataset for training and testing
#------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
                                            X,
                                            Y,
                                            test_size=0.2,
                                            random_state=42
                                            )

#-----------------------------------
# Step 4 : Scale the Fetures
#-----------------------------------

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)

#-----------------------------------
# Step 5 : Create the model
#-----------------------------------

model = DecisionTreeClassifier(random_state=42)

#-----------------------------------
# Step 6 : Train the Model
#-----------------------------------

model = model.fit(X_train, Y_train)

#-----------------------------------
# Step 7 : Test the Model
#-----------------------------------

Y_pred = model.predict(X_test)

#-----------------------------------
# Step 8 : Evaluate the model
#-----------------------------------

print("Accuracy : ", accuracy_score(Y_test, Y_pred))

print("confusion matrix : ")
print(confusion_matrix(Y_test, Y_pred))