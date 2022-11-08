def get_even_odd(x):
    odd=[]
    even=[]
    for i in x:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return(even,odd)
l=x=[10,20,30,40]
print(get_even_odd(x))