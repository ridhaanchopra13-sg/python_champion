
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)
tup3 = ()
for i in range(min(len(tup1),len(tup2))):
    tup3 = tup3+(tup1[i]*(tup2[i]),)
print("Product of tup1 and tup2:", tup3)