# -*- coding: utf-8 -*-

#https://towardsdatascience.com/machine-learning-workflow-on-diabetes-data-part-01-573864fcc6b8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
diabetes = pd.read_csv('datasets/diabetes.csv')
print("Diabetes data set dimensions : {}".format(diabetes.shape))
print(diabetes.columns)
print(diabetes.head())
print(diabetes.groupby('Outcome').size())
diabetes.groupby('Outcome').hist(figsize=(9, 9))
diabetes.isnull().sum()
diabetes.isna().sum()
 