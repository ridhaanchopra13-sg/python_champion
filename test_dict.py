test_dict = {"Codingal":2,"is":2,"best":2,"for":2,"coding":1}
print("The orginal dictionary: "+ str((test_dict)))
K = 2
res = 0
for keys in test_dict:
    if test_dict[keys] == K:
        res = res+1
print("The number 2 appears",res,"times")