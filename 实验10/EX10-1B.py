# Import modules, complete subsequent code
import os
import pandas as pd
import matplotlib.pylab as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
plt.rcParams['font.sans-serif'] = ['SimHei']  # Used to display Chinese labels normally
# Load data, file type is CSV


# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "brain_weight_new.csv")

data =pd.read_csv(input_file) # Read data file, complete this line
print(data)  # Optional code, observe data structure
# Read samples (independent variables) and labels (dependent variables), complete subsequent code
x=data["Head_Size"].values.reshape(-1,1)
y=data["Brain_Weight"].values.reshape(-1,1)
# Randomly split training set and test set, test set is 30%, complete subsequent code
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
# Build linear model, complete subsequent code
regr=linear_model.LinearRegression()
# Train model using training set, complete subsequent code
regr.fit(x_train,y_train)
# Display linear function regression coefficients and intercept, complete subsequent code
a =regr.intercept_  # Get intercept, complete this line
b =regr.coef_  # Get regression coefficient, complete this line
print("Coefficients: \n", b) # Display regression coefficient, complete code inside parentheses
print("Intercept:\n", a)     # Display intercept, complete code inside parentheses
# Get predicted data for test set independent variables, complete subsequent code
y_pred=regr.predict(x_test)
# Display mean squared error, complete subsequent code inside parentheses
print("Mean Squared Error:",mean_squared_error(y_test,y_pred))
# Display coefficient of determination, complete subsequent code inside parentheses
print("R2 Score: ",r2_score(y_test,y_pred))
# Draw trained linear regression fitting line, complete subsequent code
# Include drawing test set data scatter plot, best fit line, title, x-axis label, y-axis label
plt.title("Brain Weight Prediction")
plt.xlabel("Head Size")
plt.ylabel("Brain Weight")
plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, y_pred, color="blue", linewidth=3)
plt.show()
# Display regression equation, complete subsequent code
print("Brain_Weight={}+{}*Head_Size".format(a,b))
