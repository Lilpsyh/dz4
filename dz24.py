a=(2,3,4,5,1,9,8,6,2,4,1,11)
maxsum=a[0]+a[1]+a[2]
d=0
b=0
c=0
for i in range(1,len(a)-2):
    if(a[i]+a[i+1]+a[i+2])>maxsum:
        maxsum=a[i]+a[i+1]+a[i+2]
        d=a[i]
        b=a[i+1]
        c=a[i+2]
print(d,b,c)
print(maxsum)
