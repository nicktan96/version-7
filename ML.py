import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

dataset = pd.read_csv('heart10.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.20)

sc = preprocessing.StandardScaler()
X_train = pd.DataFrame(sc.fit_transform(X_train))
X_test = pd.DataFrame(sc.transform(X_test))

classifier = RandomForestClassifier(max_features = 'sqrt', n_estimators = 500, criterion = 'entropy', random_state = 5)
classifier.fit(X_train, y_train)


pickle.dump(classifier, open('heart.pkl', 'wb'))
model=pickle.load(open('heart.pkl', 'rb'))
print("done")