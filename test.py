import pandas as pd
import numpy as np
import matplotlib.pyplot as py


train = pd.read_csv(r"C:\Users\HAMZA\Downloads\USA_Housing.csv")


x_train = train[['Avg. Area Income']]
y_train = train[['Price']]


py.scatter(x_train,y_train,c='blue')
py.xlabel('Price')
py.ylabel('Average income')


theta0 = 10
theta1 = 20

predicted = theta0 + theta1*x_train

py.scatter(x_train,y_train,c='magenta')

py.plot(x_train,predicted,'-y')

py.xlabel('House price')

py.ylabel('Average income')

py.show()