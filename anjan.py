print("hello world")
import numpy as np
import pandas as pd
data=pd.DataFrame(data=pd.read_csv('d:\Batman\ENJOYSPORT.csv'))
concepts=np.array(data.iloc[:,0:-1])
print(concepts)
target=np.array(data.iloc[:,-1])
print(target)
def learn(concepts,target):
  specific_h=concepts[0].copy()
  print("initialization of specific_h and general_h")
  print(specific_h)
  general_h=[["?" for i in range(len(specific_h))]for i in range(len(specific_h))]
  print(general_h)
  for i, h in enumerate(concepts):
    if target[i]==1:
        for x in range(len(specific_h)):
          if h[x]!=specific_h[x]:
             specific_h[x]='?'
             general_h[x][x]='?'
        print(specific_h)
    if target[i]==0:
           for x in range(len(specific_h)):
              if h[x]!=specific_h[x]:
                 general_h[x][x]=specific_h[x]
              else:
                general_h[x][x]='?'
        
  print(specific_h)
  print(general_h)
learn(concepts,target)

            
                