import array as arr
t = arr.array("i",[1,3,2,3,4,5,3,3,6])
print(t)
print("Number of occurences of the duplicate values in the said array: "+str(t.count(3)))
t.reverse()
print(t)