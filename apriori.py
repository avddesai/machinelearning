from itertools import combinations
z = 2.220446049250313**-16

data = {
    'T100': [1, 2, 5],
    'T200': [2, 4],
    'T300': [2, 3],
    'T400': [1, 2, 4],
    'T500': [1,3],
    'T600': [2, 3],
    'T700': [1, 3],
    'T800': [1, 2, 3, 5],
    'T900': [1, 2, 3]
    }

def rsubset(arr,r): 
    return list(combinations(arr,r))

min_sup=2
min_con=0.5

C1 = {}

for i in data.values():
    for j in i:
        if j in C1.keys():
            C1[j] += 1
        else:
            C1[j] = 1

print("----------C1----------")
print(C1)
# print(clist)


L1 = []
for i in C1:
    if C1[i] >= 2:
        L1.append(i)
print("----------L1----------")
print(L1,'\n')




#two_items= [(a,b) for idx,a in enumerate(clist) for b in clist[idx + 1:]]
two_items=rsubset(L1,2)
#print(two_items)
C2={}

for a,b in two_items:
    C2[(a,b)]=0
#    print((a,b))
    for i in data:
#        print(data[i])
        if a in data[i] and b in data[i]:
            C2[(a,b)]+=1
print("C2 is:")            
print(C2)

L2=[]

for i in C2:
    if C2[i]>=2:
        L2.append(i)
print("L2 is:")       
print(L2)


C3={}
three_items= rsubset(L1,3)
#print(three_items)
for a,b,c in three_items:
#    print(rsubset([a,b,c],2))
    check=all(item in L2 for item in rsubset([a,b,c],2) )
    if check==True:
        C3[(a,b,c)]=0
        for i in data:
            if a in data[i] and b in data[i] and c in data[i]:
                C3[(a,b,c)]+=1
print("C3 is:")
print(C3)

L3=[]
for i in C3:
    if C3[i]>=2:
        L3.append(i)
print("L3 is:")       
print(L3)

print("Association rules are")

for i in L3:
    twoitems=rsubset(list(i),2)

    oneitem=list(i)
#    print(oneitem)
#    print(twoitems)
    result1 = [(k, j) for k in oneitem for j in twoitems if k not in j]
#    print(result1)
    for a, b in result1:
        x = C3[i] / (C1[a] + z)
        if (x) > 0.5:
            print(a, b, '=>', x)
        
        
#    result2 = [(j, k) for k in oneitem for j in twoitems if k not in j]
#    print(result2)
    result2 = [(j, k) for k in oneitem for j in twoitems if k not in j]
    #print(result2)
    for a, b in result2:
        x = C3[i] / (C2[a] + z)
        if (x) > 0.5:
            print(a, b, '=>', x)
    

    

        
          
    
    

    
    
    
    
