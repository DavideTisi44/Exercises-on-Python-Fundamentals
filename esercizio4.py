
L1=[]
L2=[]
L3=[]

for i in range(0,1001,2):
    L1.append(i)
for v in range(1,1001,2):
    L2.append(v)

print(L1)
print(L2)

L3.append(L1)
L3.append(L2)

print(L3)

