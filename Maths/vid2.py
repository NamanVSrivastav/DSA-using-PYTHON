# palindrome number
# for eg: i/p n=78987 o/p:yes
#      or ip n=21 o/p:no

# code
# by iterating the whole string ltor and take out last digit and will store it in another variable 



# def ispalin(n):
#     rev=0
#     temp=n
#     while temp!=0:
#         ld=temp%10
#         rev=rev*10+ld
#         temp=temp//10
#     return rev==n
# n=3223
# print(ispalin(n))
j=10
j=str(j)[-1:]
print(j)