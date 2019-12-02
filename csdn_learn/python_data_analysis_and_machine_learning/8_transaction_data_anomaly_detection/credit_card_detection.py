#1. add data (missing, abnormal, ...)
#2. give a complete solution to the problem
#3. data set segmentation
#4. comparison of evaluation methods
#5. logistic regression model
#6. analysis of modeling results
#7. scheme effect comparison

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("creditcard.csv")
print(data.head())
count_classes = pd.value_counts(data["Class"], sort=True).sort_index()
count_classes.plot(kind="bar")
plt.title("Fraud class histogram")
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.show()

from sklearn.preprocessing import StandardScaler

data["normAmount"] = StandardScaler().fit_transform(data["Amount"].values.reshape(-1, 1))
data = data.drop(["Time", "Amount"], axis=1)
print(data.head())
