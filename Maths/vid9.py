# All divisors of a number
# using for loop
n = int(input("Enter n:\n"))

for x in range(1,n+1):
    
    if n%x ==0:
        print(x)
        
# using while loop
n = int(input("Enter n:\n"))

x = 1

while x<=n:
    
    if n%x ==0:
        print(x)
    
    x = x+1
        


        

