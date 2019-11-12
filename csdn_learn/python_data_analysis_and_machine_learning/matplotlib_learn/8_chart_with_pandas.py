import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
df = pd.DataFrame({"Condition 1":np.random.rand(20),
                   "Condition 2":np.random.rand(20)*0.9,
                   "Condition 3":np.random.rand(20)*1.1 })
#print(df.head())
#print(df)

fig, ax = plt.subplots()
#df.plot.bar(ax=ax)
##堆叠图 stacked diagram
df.plot.bar(ax=ax, stacked=True)
plt.show()


######################### 堆叠图按百分比来画 Stacked drawings are drawn by percentage

from matplotlib.ticker import FuncFormatter
df_ratio = df.div(df.sum(axis=1), axis=0)
fig, ax = plt.subplots()
df_ratio.plot.bar(ax = ax, stacked=True)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y,_:"{:.0%}".format(y)))
plt.show()




########################### PCA 36维降为3维再画图PCA 36-dimensional reduction to 3D and then drawing

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv'
df = pd.read_csv(url, na_values="?")
print(df.head())

##用sklearn处理缺失值,如用均值填充
##using sklearn to handle missing values, such as filling with average
from sklearn.preprocessing import Imputer
impute = pd.DataFrame(Imputer().fit_transform(df))
impute.columns = df.columns
impute.index = df.index

print(impute.head())

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

features = impute.drop('Dx:Cancer', axis=1)
y = impute["Dx:Cancer"]

pca = PCA(n_components=3)
X_r = pca.fit_transform(features)

print("Explained variance:\nPC1 {:.2%}\nPC2 {:.2%}\nPC3 {:.2%}"
      .format(pca.explained_variance_ratio_[0],
              pca.explained_variance_ratio_[1],
              pca.explained_variance_ratio_[2]))

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(X_r[:, 0], X_r[:, 1], X_r[:, 2], c=y, cmap=plt.cm.coolwarm)

# Label the axes
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')

plt.show()














