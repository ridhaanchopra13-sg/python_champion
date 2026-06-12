square=[5,8,3,7,2,9,12]
even_squares=[]
odd_squares=[]
print("Original squares", square)
for i in range(len(square)):
    square[i]=square[i]**2
    if (square[i]%2==0):
        even_squares.append(square[i])
    else:
        odd_squares.append(square[i])
print("Squared list", square)
print("even numbers squares", even_squares)
print("Odd numbers squares", odd_squares)