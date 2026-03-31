# Import modules
import os
import pandas as pd
import matplotlib.pylab as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
# Load data, file type is xls

# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "time_cholesterol.xls")

data = pd.read_excel(input_file)
print(data) # Optional code, to observe data structure
# Read samples (independent variables) and labels (dependent variables)
x=data["time"].values.reshape(-1,1)
y=data["cholesterol"].values.reshape(-1,1)
# Randomly split training set and test set, test set is 30%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# Build linear model
regr = linear_model.LinearRegression()
# Train model using training set
regr.fit(x_train, y_train)
# Display linear function regression coefficients and intercept
a = regr.intercept_
b = regr.coef_
print("Coefficients: \n", b)
print("Intercept:\n", a)
# Get predicted data for test set independent variables
y_pred = regr.predict(x_test)
# Display mean squared error
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
# Display coefficient of determination
print("R2 Score: ", r2_score(y_test, y_pred))
# Draw trained linear regression fitting line
plt.title("LinearRegression time-choles")
plt.xlabel("time")
plt.ylabel("choles")
plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, y_pred, color="red", linewidth=3)
plt.show()
# Display regression equation
print("choles= {}+ {}* time".format(a, b))