import os
import csv
from sklearn import tree
import pandas as pd
import pydotplus
from IPython.display import Image
from IPython.display import display
from graphviz import Graph


#Tên các cột
LIST_INDEPENDENT_COLUMN_NAMES = ['outlook', 'temperature', 'humidity', 'wind'] 
DEPENDENT_COLUMN_NAME = "play"

listColumn = [LIST_INDEPENDENT_COLUMN_NAMES, DEPENDENT_COLUMN_NAME]
#Bộ dataset từ file csv
DATASET = pd.read_csv('testDataSet.csv')

#In ra bảng chứa các giá trị dummies 0 và 1 
table_0_and_1_value = pd.get_dummies(DATASET[LIST_INDEPENDENT_COLUMN_NAMES])

#Xây dựng Cây quyết định
decisionTree = tree.DecisionTreeClassifier()
decisionTree = decisionTree.fit(table_0_and_1_value, DATASET[DEPENDENT_COLUMN_NAME])
print(decisionTree.get_params())
dotData = tree.export_graphviz(decisionTree,
                               out_file= None,
                               feature_names= list(table_0_and_1_value.columns.values),
                               # class_names = DATASET[DEPENDENT_COLUMN_NAME]))
                              )
# print(dotData)
