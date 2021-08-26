def recur_factorial(num):
    if num ==1:
        return num
    else:
        return num * recur_factorial(num-1)
number = int(input("Enter The Number : "))

if number < 0 :
    print("Sorry, Factorial doesn't exist for negative numbers")

elif number == 0 :
    print("The fatorial of 0 is 1")

else:
    print("The factorial of",number,"is",recur_factorial(number))


print("-------------------------------------------------------")



##Another Solution :
import math

num = int(input('enter a num = '))

print(math.factorial(num))