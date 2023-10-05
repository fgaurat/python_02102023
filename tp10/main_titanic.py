import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier

titanic = sns.load_dataset('titanic')

titanic = titanic[["survived","pclass","sex","age"]]



titanic.dropna(axis=0,inplace=True)


titanic['sex'].replace(['male','female'],[0,1],inplace=True)

y = titanic['survived']
X = titanic.drop('survived',axis=1)

model = KNeighborsClassifier()
model.fit(X,y)
model.score(X,y)

def has_survived(model,pclass,sex,age):
    X = np.array([pclass,sex,age]).reshape(1,3)    
    # print(np.array([pclass,sex,age]))
    # print(X)
    return model.predict(X)

p = has_survived(model,1,0,37)
print(p)


