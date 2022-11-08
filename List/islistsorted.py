def isSorted(arr):
        #code here
        b=[]
        b=arr.sort()
        c=arr[::-1]
        if arr==b:
            return 1
        elif arr==c:
            return 1
        else:
            return 0
        print(b)
# arr=[1,2,3]
# print(isSorted(arr))
arr=[1,2,3]
arr.sort()
print(arr)