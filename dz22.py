a=[1,2,3,4,4,5,5,7,9,11,12]
b=[1,4,5,7,9,11,11,11,9,5,12]
c=set()
if len(b)>=len(a):
    for i in range(len(b)):
        if b[i] in a:
            c.add(b[i])
print(c)
