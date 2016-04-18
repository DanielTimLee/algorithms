c=input()
d=map(int, raw_input().split())
d.sort()
n=input()
l=list()
v=0
for i in range(n):
    l.append(input())

for i in range(n):
    if float(sum(d))/2>l[i]:
        v+=abs(d[0]-l[i])
        d[0]=l[i]
    elif float(sum(d))/2==float(l[i]):
        comp(d[0],d[1],i,n)
        if l[i]>l[i+1]:
            v+=abs(d[0]-l[i])
            d[0]=l[i]
        else:
            v+=abs(d[1]-l[i])
            d[1]=l[i]
    else:
        v+=abs(d[1]-l[i])
        d[1]=l[i]
print v

def comp(a,b,i,n):
    for i in range(i,n):
