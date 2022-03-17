a=[9,6,5,9,3,2,1,0,5,0,4,6,0]
zeros=[]
for i in a:
    if i==0:
        zeros.append(i)
        a.remove(i)
a=sorted(a)

result = a + zeros
print(result)