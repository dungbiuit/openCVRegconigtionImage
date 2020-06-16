import csv
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd

DATA_CSV = pd.read_csv('datas.csv', header=0)

featureColumns = pd.get_dummies(DATA_CSV[['mean_hue', 'stddev_hue', 'mean_sat',
                                          'stddev_sat', 'mean_val', 'stddev_val']])

REAL_VALUE_COLUMNS = DATA_CSV.values[:, 6]
classificationColumn = pd.get_dummies(REAL_VALUE_COLUMNS)
nightDayClassification = classificationColumn.iloc[:, 0]

featuresTrain, featuresTest, classificationTrain, classificationTest = train_test_split(featureColumns, nightDayClassification,
                                                                          test_size = 0.3, random_state = 100)

def trainByGini(featuresTrain, classesTrain):
    classifierByGini = tree.DecisionTreeClassifier(random_state = 100, max_depth=3, min_samples_leaf=5)
    classifierByGini.fit(featuresTrain, classesTrain)
    return classifierByGini

def returnPredictClassValue(featuresTest, treeClassifier):
    predictClass = treeClassifier.predict(featuresTest)
    print("Predict value: ", predictClass)
    return predictClass

predictValueList = returnPredictClassValue(featuresTest, trainByGini(featuresTrain, classificationTrain))

def calculateDifferenceOfPredictAndRealValue(predictValue, testValue):
    print("Report: ", classification_report(testValue, predictValue))
    return (accuracy_score(predictValue, testValue) * 100)

print("Percentage prediction: ", calculateDifferenceOfPredictAndRealValue(predictValueList, classificationTest ))
