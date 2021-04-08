import pprint
import numpy as np
import pandas as pd
z = 2.220446049250313**-16
from numpy import log as log

dataset=pd.read_csv('Buy_Computer.csv')
df = pd.DataFrame(dataset,columns=['age','income','student','credit_rating','Buy_Computer'])

ent_node = 0  
values = df.Buy_Computer.unique() 
for value in values:
    fraction = df.Buy_Computer.value_counts()[value]/len(df.Buy_Computer)  
    ent_node += -fraction*np.log2(fraction)

def ent_attribute(df,attribute):
    target_variables = df.Buy_Computer.unique() 
    variables = df[attribute].unique()        
    entropy_attribute = 0
    for variable in variables:
        entropy_each_feature = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute]==variable][df.Buy_Computer ==target_variable]) 
            den = len(df[attribute][df[attribute]==variable])  
            fraction = num/(den+z) 
            entropy_each_feature += -fraction*log(fraction+z)
        fraction2 = den/len(df)
        entropy_attribute += -fraction2*entropy_each_feature
    return(abs(entropy_attribute))    

def test_attribute(df):
    IG = []
    for key in df.keys()[:-1]:
        IG.append(ent_node-ent_attribute(df,key))
    return df.keys()[np.argmax(IG)]
  
def get_subtable(df, node,value):
  return df[df[node] == value].reset_index(drop=True)


def decisiontree(df,tree=None):
    node = test_attribute(df)
    attValue = np.unique(df[node])
    
        
    if tree is None:                    
        tree={}
        tree[node] = {}
    


    for value in attValue:
        
        subtable = get_subtable(df,node,value)
        clValue,counts = np.unique(subtable['Buy_Computer'],return_counts=True)                        
        
        if len(counts)==1:
            tree[node][value] = clValue[0]                                                    
        else:        
            tree[node][value] = decisiontree(subtable)  
                   
    return tree
 
     
dt=decisiontree(df)
print("The decision tree is:")
pprint.pprint(dt)    



