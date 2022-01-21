'''import numpy as np
import pandas as pd

#data = pd.DataFrame(data=pd.read_csv('data.csv'))
data = pd.read_csv('data.csv')
print('The Dataset is: ')
print(data)
concepts = np.array(data.iloc[0:, 0:-1])
target = np.array(data.iloc[:,-1])
print('\nThe concepts are :\n', concepts)
print('\nThe target is:\n', target)
if target[0] == 'No':
    for i in range(1, len(target)):
        if target[i] == 'Yes':
            target[0], target[i] = target[i], target[0]
            temp = [i for i in concepts[i]]
            concepts[i] = concepts[0]
            concepts[0] = temp
            break


def learn(concepts, target):
    specific_h = concepts[0].copy()
    #print(specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    #print(general_h)
    for i, h in enumerate(concepts):
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        if target[i] == "No":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    return specific_h, general_h


s_final, g_final = learn(concepts, target)
print("\nFinal S:", s_final)
print("\nFinal G:", g_final)'''

import numpy as np
import pandas as pd
data = pd.read_csv('data.csv')
print('The data is: \n')
print(data)
concepts = np.array(data.iloc[0:,0:-1])
target = np.array(data.iloc[:,-1])
print('The concepts are :\n',concepts)
print('The target is \n',target)
def learn(concepts,target):
	s_h = concepts[0].copy()
	g_h = [['?' for i in range(len(s_h))] for i in range(len(s_h))]
	for i,h in enumerate(concepts):
		if target[i]=='Yes':
			for x in range(len(s_h)):
				if h[x]!=s_h[x]:
					s_h[x] = '?'
					g_h[x][x]='?'
		if target[i]=='No':
			for x in range(len(s_h)):
				if h[x]!=s_h[x]:
					g_h[x][x]=s_h[x]
				else:
					g_h[x][x]='?'
	indices = [i for i,val in enumerate(g_h) if val==['?','?','?','?','?','?']]
	for i in indices:
		g_h.remove(['?','?','?','?','?','?'])
	return s_h,g_h

sfinal,gfinal = learn(concepts,target)
print(sfinal)
print(gfinal)