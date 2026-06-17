numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x,y:x+y,numbers1,numbers2)
print("Addition of lists: ")
print(list(result))
nums = [1,2,3,4,5]
def sq(n):
    return(n**2)
square = map(sq,nums)
print(list(square))