import os
os.chdir(r'/raid/home/tejus/MLMC/Actual_data/HMM/Test_hmm_parsed')
files=os.listdir()
d={}
for i in range(1, 3501):
    if str(i)+'.csv' in files:
        d[i]=1
    else:
        d[i]=0
        
        
import numpy as np
import pandas as pd
np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True, formatter={'float': '{:0.10f}'.format})
def feat_ext(file):
    
    print("Processing:"+str(file))
    if d[file]==1:
        df=pd.read_csv(str(file)+'.csv')
        V=np.array([])
        for j in df.columns[0:20]:
            V=np.append(V,df[j].mean())
        N=len(df)
        for X in range(1,16):
            s=[0 for _ in range(20)]
            for i in range(N-X):
                for j in range(0,20):
                    s[j]+=((df.iloc[i,j]-df.iloc[i+X,j])**2)
            for i in range(20):
                s[i]=s[i]/(N-X)
            V=np.append(V,s)
        return V
    else:
        return np.array([None for _ in range(320)])
    
for cc in range(1, 3501):
    try:
        x = feat_ext(cc)
        x.tofile(rf'/raid/home/tejus/MLMC/Actual_data/HMM/Train_hmm_features/{cc}.csv', sep=',')
    except ZeroDivisionError as e:
        x=np.array([None for _ in range(320)])
        x.tofile(rf'/raid/home/tejus/MLMC/Dataset_1/HMM/Train_hmm_features/{cc}.csv', sep=',')
        continue  # Move to the next iteration
    
    