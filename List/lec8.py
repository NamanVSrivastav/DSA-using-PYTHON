# complexity=o(n) with two traversals
# def getsecmax(l):
#     if len(l)<=1:
#         return None
#     lar=max(l)
#     slar=None
#     for x in l:
#         if x!=lar:
#             if slar==None:
#                 slar=x
#             else:
#                 slar=max(slar,x)
#     return slar
# l=[10,5,8,20] 
# print(getsecmax(l))      
# complexity=o(n) with 1 traversal
# def getsecmax(l):
#     if len(l)<=1:
#         return None
#     lar=l[0]
#     slar=None
#     for x in l[1:]:
#         if x>lar:
#             slar=lar
#             lar=x
#         elif x!= lar:
#             if slar==None or slar<x:
#                 slar=x
#     return slar
# l=[10,5,8,20] 
# print(getsecmax(l)) 