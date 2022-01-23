import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
iris_dataset = load_iris()
print('\nIRIS FEATURES\TARGET NAMES: \n',iris_dataset.target_names)
for i in range(len(iris_dataset.target_names)):
    print("\n[{0}]:[{1}]".format(i,iris_dataset.target_names[i]))
x_train,x_test,y_train,y_test = train_test_split(iris_dataset["data"],iris_dataset["target"],random_state=0)
kn = KNeighborsClassifier(n_neighbors=4)
kn.fit(x_train,y_train)
i=1
x = x_test[i]
x_new = np.array([x])
for i in range(len(x_test)):
    x=x_test[i]
    x_new=np.array([x])
    prediction = kn.predict(x_new)
    print("\nActual : {0}\t{1} & Predicted: {2}{3}".format(y_test[i],iris_dataset.target_names[y_test[i]],prediction,iris_dataset.target_names[prediction]))
print('\nTEST SCORE[ACCURACY]:{:.2f}\n'.format(kn.score(x_test,y_test)))