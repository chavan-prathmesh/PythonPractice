# Q1. (Operators) 
# Write a Java program that takes two numbers as input and performs the following 
# operations without using built-in methods: - Find which number is greater using only the ternary operator. - Swap the two numbers without using a third variable (use arithmetic operators). - Check if the sum of both numbers is even or odd. 

num1 = int(input("Enter a first number :"))
num2 = int(input("Enter second number :"))
print("Number 1:",num1)
print("Number 2:",num2)
greater =  num1 if num1>num2 else num2

print("Greater Number:",greater)

num1,num2 = num2,num1 

print("Numbers after swapping :")
print("Number 1:",num1)
print("Number 2:",num2)
sum = num1+num2
print("Sum of both numbers :",sum)
if sum%2==0:
    print("sum is Even ")
else:
    print("sum is Odd")
