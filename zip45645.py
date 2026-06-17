s1 = {1,2,3}
s2 = {'a','b','c'}
s3 = list(zip(s1,s2))
print(s3)
list1 = [10,20,30,40]
list2 = [100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
stocks = ["reliance","infosys","chatgpt"]
price = [12876,8613,3678554]
new_dict = {stocks:price for stocks,price in zip(stocks,price)}
print(new_dict)