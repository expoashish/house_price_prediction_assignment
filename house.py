import pandas as pd # data processing
import matplotlib.pyplot as plt # visualization
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split # data split
 
main_data = pd.read_excel("data_file.xlsx")
# print(main_data.head())
# print(main_data.shape)
# print(main_data.describe()) #mean, median, standard deviation
# print(main_data.isnull().sum())
# print(main_data.duplicated().sum())
# print(main_data.dtypes)

X = main_data.drop(['House price of unit area','Transaction date'], axis=1)
Y = main_data['House price of unit area']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8, test_size=0.2, random_state=0)


from sklearn import svm
from sklearn.svm import SVC
from sklearn.metrics import mean_absolute_percentage_error
SVR_model = svm.SVR()
SVR_model.fit(X_train,Y_train)
Y_pred = SVR_model.predict(X_test)
print("SVM= ",mean_absolute_percentage_error(Y_test, Y_pred))


from sklearn.ensemble import RandomForestRegressor
Random_model = RandomForestRegressor(n_estimators=10)
Random_model.fit(X_train, Y_train)
Y_pred = Random_model.predict(X_test)
print("RFA=",mean_absolute_percentage_error(Y_test, Y_pred))
