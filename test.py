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

array = []

for record in rs:
    array.append(record[0])
       

X = np.empty((569,30))
y = np.empty((569,1))

for i in range(0, 568):
    for j in range(2, 31):
        X[i][j-2] = array[j + 32]
        y[i][0] = array[2]

print(y)    

"""
X = array[:,2:32]
y = array[:,1:2]

print(y)


for record in rs:
    array[0].append(record[0])
    array[0].append(record[1])
    array[0].append(record[2])
    array[0].append(record[3])
    array[0].append(record[4])
    array[0].append(record[5])
    array[0].append(record[6])
    array[0].append(record[7])
    array[0].append(record[8])
    array[0].append(record[9])
    array[0].append(record[10])
    array[0].append(record[11])
    array[0].append(record[12])
    array[0].append(record[13])
    array[0].append(record[14])
    array[0].append(record[15])
    array[0].append(record[16])
    array[0].append(record[17])
    array[0].append(record[18])
    array[0].append(record[19])
    array[0].append(record[20])
    array[0].append(record[21])
    array[0].append(record[22])
    array[0].append(record[23])
    array[0].append(record[24])
    array[0].append(record[25])
    array[0].append(record[26])
    array[0].append(record[27])
    array[0].append(record[28])
    array[0].append(record[29])
    array[0].append(record[30])
    array[0].append(record[31])
    

X = array[:,2:32]
y = array[:,1:2]

print(X)
print(y)
"""