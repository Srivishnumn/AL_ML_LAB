import pandas as pd
data = pd.read_csv('data6.csv')
te = len(data)
np = len(data.loc[data[data.columns[-1]]=='Yes'])
nn = te-np
training = data.sample(frac=0.75,replace=False)
test = pd.concat([data,training,training]).drop_duplicates(keep=False)
print('Training set: \n',training)
print('\nTest data set: \n',test)
prob = {}
for col in training.columns[:-1]:
    prob[col]={}
    vals = set(data[col])
    for val in vals:
        temp = training.loc[training[col]==val]
        pe = len(temp.loc[temp[temp.columns[-1]]=='Yes'])
        ne = len(temp)-pe
        prob[col][val] = [pe/np,ne/nn]
prediction = []
right_prediction = 0
for i in range(len(test)):
    row = test.iloc[i,:]
    fpp = np/te
    fpn = nn/te
    for col in test.columns[:-1]:
        fpp *= prob[col][row[col]][0]
        fpn *= prob[col][row[col]][1]
    if fpp>fpn:
        prediction.append('Yes')
    else:
        prediction.append('No')
    if prediction[-1]==row[-1]:
        right_prediction += 1
print('\nActual values : ',list(test[test.columns[-1]]))
print('Predicted: ',prediction)
print('Accuracy :',right_prediction/len(test))


'''
outlook temperature humidity    windy   play tennis
sunny    hot         high        weak     No
sunny    hot         high        strong   No
overcast hot         high        weak     Yes
rainy    mild        high        weak     Yes
rainy    cool        normal      weak     Yes
rainy    cool        normal      strong   No
overcast cool        normal      strong   Yes
sunny    mild        high        weak     No
sunny    cool        normal      weak     Yes
rainy    mild        normal      weak     Yes
sunny    mild        normal      strong   Yes
overcast mild        high        strong   Yes
overcast hot         normal      weak     Yes
rainy    mild        high        strong   No
'''