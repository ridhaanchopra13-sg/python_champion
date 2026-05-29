L = [4,1,2,6,7,9,5,8]
print("original_list :",L)
count = 0
for i in L:
    count +=1
avg = count/len(L)
print("sum=",count)
print("average=",avg)  
L.sort()
print("smallest element is", L[0])
print("greatest element is", L[-1])