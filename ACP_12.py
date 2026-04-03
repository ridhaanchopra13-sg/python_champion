decimal_num= int(input("Enter a decimal number: "))
binary_str=""
n = decimal_num
while n>0:
    remainder=n%2
    binary_str=str(remainder)+binary_str
    n=n//2
if decimal_num == 0:
    binary_str="0"
print(binary_str)