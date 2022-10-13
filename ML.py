from unicodedata import name
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score, balanced_accuracy_score

df = pd.read_csv('C:\\Users\\KOSTA\\mD\\breast-cancer.csv')
df.head()
df.isna().sum()
df.dropna(axis=1, inplace=True)
df.columns
df.describe().T
#sns.pairplot(df)
df['diagnosis'] = (df['diagnosis'] == 'M').astype(int) #encode the label into 1/0
df.head()
df['diagnosis'].values

corr = df.corr()
##corr2 = corr.drop(corr.columns[0],axis=1)
##corr3 = corr2.drop(labels=range(0),axis=0)
#print(corr)
plt.figure(figsize =(20,20))
sns.heatmap(corr,annot=True,linewidths=0.5,fmt=".1f",square=True)
#plt.show()

# Get the absolute value of the correlation
cor_target = abs(corr["diagnosis"])

# Select highly correlated features (thresold = 0.2)
relevant_features = cor_target[cor_target>0.2]
#print(relevant_features)

# Collect the names of the features
names = [index for index, value in relevant_features.iteritems()]

# Drop the target variable from the results
names.remove('diagnosis')

# Display the results
#print(names)

X = df[names]
y = df['diagnosis']

def train_evaluate_model(model, X, y):
    '''
    Keyword arguments:
    X -- Training data
    y -- Traing labels

    returns a dataframe for evaluating metrics
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42) #split the  data into traing and validating

    scaler = StandardScaler() #create an instance of standard scaler
    scaler.fit(X_train) # fit it to the training data

    scaler.transform(X_train) #transform training data
    scaler.transform(X_test) #transform validation data

    model.fit(X_train, y_train)  #fit the model instance 


    predictions = model.predict(X_test) # calculate predictions

    #compute metrics for evaluation
    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    balanced_accuracy = balanced_accuracy_score(y_test, predictions)

    #create a dataframe to visualize the results
    eval_df = pd.DataFrame([[accuracy, f1, precision, recall, balanced_accuracy]], columns=['accuracy', 'f1_score', 'precision', 'recall', 'balanced_accuracy'])
    return eval_df

## LogisticRegression

lg = LogisticRegression()

results = train_evaluate_model(lg, X, y)

results.index = ['LogisticRegression']

results

## Decision Tree

decision_tree = DecisionTreeClassifier()
decision_tree_results = train_evaluate_model(decision_tree, X, y)

decision_tree_results.index = ['DecisionTree']

results = results.append(decision_tree_results)

results

## KNearestNeighbors

knn = KNeighborsClassifier(n_neighbors=12)

knn = train_evaluate_model(knn, X, y)
knn.index =['KNearsNeighbors']
results = results.append(knn)

results

## RandomForestClassifer

rfc = RandomForestClassifier()

rfc_result = train_evaluate_model(rfc, X, y)
rfc_result.index = ['RandomForest']

results = results.append(rfc_result)

results

## XGBoost

xgboost = xgb.XGBClassifier()
xgboost_result = train_evaluate_model(rfc, X, y)
xgboost_result.index = ['XGBoost']

results = results.append(xgboost_result)

results

## All together

X_all_features = df.drop('diagnosis',axis=1)

LogisticRegression_all_features = train_evaluate_model(decision_tree, X_all_features, y)

LogisticRegression_all_features.index = ['LogisticRegression_all_features']
results = results.append(LogisticRegression_all_features)

DecisionTree_all_features = train_evaluate_model(decision_tree, X_all_features, y)

DecisionTree_all_features.index = ['DecisionTree_all_features']
results = results.append(DecisionTree_all_features)


KNearsNeighbors_all_features =  train_evaluate_model(decision_tree, X_all_features, y)

KNearsNeighbors_all_features.index = ['KNearsNeighbors_all_features']
results = results.append(KNearsNeighbors_all_features)

RandomForest_all_features = train_evaluate_model(decision_tree, X_all_features, y)

RandomForest_all_features.index = ['RandomForest_all_features']
results = results.append(RandomForest_all_features)


XGBoost_all_features = train_evaluate_model(xgboost, X_all_features, y)

XGBoost_all_features.index = ['XGBoost_all_features']
results = results.append(XGBoost_all_features)

print(results)


plt.figure(figsize=(8,8))
plt.plot(results.iloc[:5,0],label='accuracy',color='blue')
plt.plot(results.iloc[:5,1],label='F1',color='red')
plt.plot(results.iloc[:5,2],label='Precision',color='green')
plt.plot(results.iloc[:5,3],label='recall',color='orange')
plt.plot(results.iloc[:5,4],label='balanced_accuracy',color='purple')
plt.legend()

plt.show()


