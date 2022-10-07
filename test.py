import cx_Oracle
import numpy as np
from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

sql =   """
        select
            col1,
            col2,
            col3,
            col4
        from TEST_TBL
        """
conn = cx_Oracle.connect('c##sqldb/1234@localhost:1521/xe')
# conn = cx_Oracle.connect('user_id/password@host_name:port/sid')
cs = conn.cursor()
rs = cs.execute(sql)

col1 = []
col2 = []
col3 = []
col4 = []

for record in rs:
    col1.append(record[0])
    col2.append(record[1])
    col3.append(record[2])
    col4.append(record[3])

print(col1[0]+col1[1]+col1[2])
print(col2[0]+col2[1]+col2[2])
print(col3[0]+col3[1]+col3[2])
print(col4[0]+col4[1]+col4[2])

X = col1
y = col4

print(type(X))
print(type(y))
"""
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1, shuffle=True)
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
#models.append(('LDA', LinearDiscriminantAnalysis()))
#models.append(('KNN', KNeighborsClassifier()))
#models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=2, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()
"""