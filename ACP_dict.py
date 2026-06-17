test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test Dictionary:", test_dict)
K = int(input("What number do you want (1, 2, or 3)? "))
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res += 1
print("The number", K, "appears", res, "times")