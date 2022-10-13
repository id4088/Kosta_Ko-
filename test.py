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
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10,
	         col11, col12, col13, col14, col15, col16, col17, col18, col19, col20,
	         col21, col22, col23, col24, col25, col26, col27, col28, col29, col30,
	         col31, col32
        from TEST_TBL
        """
conn = cx_Oracle.connect('c##sqldb/1234@localhost:1521/xe')
# conn = cx_Oracle.connect('user_id/password@host_name:port/sid')
cs = conn.cursor()
rs = cs.execute(sql)

X = np.empty((569,30))
y = []

num = 0
for record in rs:
    for i in range(0, 29):
        X[num][i] = record[i+2]
    """
    X[num][0] = record[2]
    X[num][1] = record[3]
    X[num][2] = record[4]
    X[num][3] = record[5]
    X[num][4] = record[6]
    X[num][5] = record[7]
    X[num][6] = record[8]
    X[num][7] = record[9]
    X[num][8] = record[10]
    X[num][9] = record[11]
    X[num][10] = record[12]
    X[num][11] = record[13]
    X[num][12] = record[14]
    X[num][13] = record[15]
    X[num][14] = record[16]
    X[num][15] = record[17]
    X[num][16] = record[18]
    X[num][17] = record[19]
    X[num][18] = record[20]
    X[num][19] = record[21]
    X[num][20] = record[22]
    X[num][21] = record[23]
    X[num][22] = record[24]
    X[num][23] = record[25]
    X[num][24] = record[26]
    X[num][25] = record[27]
    X[num][26] = record[28]
    X[num][27] = record[29]
    X[num][28] = record[30]
    X[num][29] = record[31]
    """
    y.append(record[1])
    num = num + 1
   
#print(X)    
#print(y)

X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1, shuffle=True)
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, np.ravel(Y_train), cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()
