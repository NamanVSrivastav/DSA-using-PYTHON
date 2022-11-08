# count digits 
# for eg: i/p x=9235 o/p:4

# code 


def count_dig(x):
    res=0
    while x>0:
        x=x//10
        res+=1
    return res

number=95566
print(count_dig(number))     