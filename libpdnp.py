import pandas as pd                                                         #importing pandas and numpy with alis as pd and np respectively
import numpy as np
iris = pd.read_csv(r"C:\Users\poras\OneDrive\Documents\dataset\iris.csv")   # r to read the file ; pd.read_extension
print("The .head will print the top 5 values.")
print(iris.head())  
print("The .describe will print the statistical values.")
print(iris.describe())
print("The .tail will print the top 5 values.")
print(iris.tail())