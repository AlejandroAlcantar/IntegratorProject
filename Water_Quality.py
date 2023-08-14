# %% [markdown]
# # Baseline
#
# The results of the following projects were used:
#
# https://www.kaggle.com/code/wadors/proyecto2/input
#
# https://www.kaggle.com/code/monicacinthya/water-potability-eda
#
# Colunms
# 1. ph: pH of 1. water (0 to 14).
# 2. Hardness: Capacity of water to precipitate soap in mg/L.
# 3. Solids: Total dissolved solids in ppm.
# 4. Chloramines: Amount of Chloramines in ppm.
# 5. Sulfate: Amount of Sulfates dissolved in mg/L.
# 6. Conductivity: Electrical conductivity of water in μS/cm.
# 7. Organic_carbon: Amount of organic carbon in ppm.
# 8. Trihalomethanes: Amount of Trihalomethanes in μg/L.
# 9. Turbidity: Measure of light emiting property of water in NTU.
# 10. Potability: Indicates if water is safe for human consumption. Potable -1 and Not potable -0
#
# Drinking water that is not potable causes health problems and, in turn,
# this causes a higher health expense, for which it seeks to create a model that predicts
# whether the water is drinkable or not; In this way, improve the quality of life and reduce
# health costs caused by consuming water that is not drinkable.
#
# Several models have been made with an accuracy between 60% and 70% of prediction
# if the water is drinkable or not.
#
# A model is sought that at least has an average of 65% in accuracy or higher.
# The objective of this project is for the subject of Deployment of machine learning models
# and it is a proof of concept.
#

# %% [markdown]
# # Setup
# In this notebook section, we will import the libraries needed to run
# this code.

import matplotlib.pyplot as plt
import numpy as np
# %%
import pandas as pd
import seaborn as sns
# ML
from scipy.stats import zscore
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

DATASETS_DIR = 'Users/jesus.alcantar/Documents/GitHub/IntegratorProject/DataSet/water_potability'

# %%
data_set = pd.read_csv(DATASETS_DIR)
data_set

# %%
data_set.head()

# %%
data_set.info()

# %%
data_set.isnull().sum()

# %%
data_set = data_set.fillna(data_set.mean())

# %%
data_set.isnull().sum()

# %%
data_set = (data_set - data_set.min()) / (data_set.max() - data_set.min())
data_set

# %%
data_set.plot(kind='box',
              figsize=(18, 8)
              )
plt.grid()

# %%
z_scores = zscore(data_set)
Datos_limpios = (np.abs(z_scores) < 2.5).all(axis=1)
data_set = data_set[Datos_limpios]

# %%
data_set.plot(kind='box',
              figsize=(18, 8)
              )
plt.grid()

# %%
data_set = data_set.reset_index()
del data_set['index']
data_set

# %%
corr = data_set.corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr,
            xticklabels=True,
            yticklabels=True,
            annot=True,
            ax=ax
            )
plt.title('Correlación de las variables')

# %%
data_set_X = data_set.drop(['Potability'], axis=1).values

# %%
data_set_Y = data_set['Potability'].values
data_set_Y

# %%
X_train, X_test, y_train, y_test = train_test_split(
    data_set_X, data_set_Y, test_size=0.2, random_state=0)

# %%
param_GB = {'n_estimators': range(100, 1000, 100),
            'max_depth': range(2, 6),
            'loss': ['deviance', 'exponential']}

# %%
GradBoost = GradientBoostingClassifier()

# %%
gsearch_GB = GridSearchCV(
    GradBoost,
    param_grid=param_GB,
    scoring='r2',
    cv=5,
    return_train_score=True)

# %%
gsearch_GB.fit(X_train, y_train)

# %%
# GridSearchCV(cv=5, estimator=GradientBoostingClassifier(),
#             param_grid={'loss': ['deviance', 'exponential'],
#                         'max_depth': range(2, 6),
#                         'n_estimators': range(100, 1000, 100)},
#             return_train_score=True, scoring='r2')

# %%
gsearch_GB.best_params_, gsearch_GB.best_score_

# %%
gsearch_GB.best_estimator_.score(X_test, y_test)
