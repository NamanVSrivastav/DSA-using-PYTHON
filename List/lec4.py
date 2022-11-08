def smallerthanx(x,s):
    l=[]
    for i in x:
        if i<s:
            l.append(i)
        
    return(l)
x=[10,2,4,5]
s=6
print(smallerthanx(x,s))
