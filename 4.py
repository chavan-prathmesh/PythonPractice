# Q4. (Conditional + Loops) 
# Write a Java program to accept a number from the user and check the following: - If the number is prime or not. - If it is prime, also check whether it is a palindrome (e.g., 131, 151). - Print appropriate messages. 
def call_palindrome(num):
    dup = num 
    rev = 0
    while(num>0):
        remainder = num%10
        rev = (rev*10)+remainder
        num = num//10

    if dup == rev:
        print("Number is Palindrome!!!!")

    else:
        print("Number is not Palindrome....")


def check_prime(num):
    flag = 0
   
    for i in range(2,num):
        if num%i==0:
            flag+=1
    if flag==0:
        print("Entered number is PRIME")
        call_palindrome(num)
    else:
        print("Entered number is NOT PRIME")

num = int(input("Enter a number :"))
check_prime(num)