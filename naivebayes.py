import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
df = pd.read_csv('Buy_Computer.csv')
le= preprocessing.LabelEncoder()
labels = df.apply(le.fit_transform)
X = labels.values[:14,1:5]
Y = labels.values[:14,5]
X_train, X_test, y_train, y_test= train_test_split(X,Y, test_size=0.33, random_state=15)
gaus  = GaussianNB()
gaus.fit(X_train, y_train)
prediction = gaus.predict(X_test)
print(prediction)
print("Gaussian Naive Bayes successfully implemented on dataset. Accuracy is:")
print(accuracy_score(y_test,prediction))


    


