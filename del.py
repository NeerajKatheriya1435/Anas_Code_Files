# def flattan(lst):
#     newlist=[]
#     for item in lst:
#         if isinstance(item,list):
#             newlist.extend(flattan(item))
#         else:
#             newlist.append(item)
#     return newlist

# nested_list = [1, [2, 3], [4, [5, 6]], 7]
# print(flattan(nested_list))

# lst=[3,4,5,6,2,4,6,7,8]

# freq={}

# for item in lst:
#     if item in freq:
#         freq[item]+=1
#     else:
#         freq[item]=1

# print(freq)
# num=5
# for i in range(num):
#     number=1
#     for j in range(num-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print(number,end=" ")
#         number=number*(i-k)//(k+1)
#     print()

num=15
for i in range(num):
    for j in range(num):
        if(i==0 or i==num-1 or j==0 or j==num-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()