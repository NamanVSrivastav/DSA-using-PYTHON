def avg(l):
    sum=0
    for x in l:
        sum=sum+x
    n=len(l)
    return (sum/n)
l=[10,20,30,40,50,60]
print(avg(l))