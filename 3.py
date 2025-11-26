# Q3. (Array + Loops + Conditionals) 
# Create a Java program that takes an integer array from the user. - Find the maximum and minimum elements in the array. - Count how many elements are even and how many are odd. - Print the array in reverse order without using extra arrays.
arr =[]
size =int(input("Enter array size :"))
print("Enter array element :")
for i in range(size):
    arr.append(int(input()))

min = max = arr[0]
for item in arr:
    if item<min:
        min = item
    elif item>max:
        max = item
print("Maximum :",max)
print("Minimum :",min)

even_counter = odd_counter =0
for item in arr:
    if item%2==0:
        even_counter+=1
    else:
        odd_counter+=1

print("Even numbers :",even_counter)
print("Odd numbers :",odd_counter)

print("Original array :",arr)
print("Reversed array:",arr[::-1])  #1]array.reverse() 2]list(reversed(array)) 
