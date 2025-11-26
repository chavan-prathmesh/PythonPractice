# Q5. (Operators + Arrays + Loops) 
# Write a Java program that accepts marks of 5 subjects of a student in an array. - Calculate the total marks and percentage using arithmetic operators. - Using if-else conditions, assign grades as: - A for ≥ 75% - B for ≥ 60% - C for ≥ 45% - Fail otherwise - Print the subject-wise marks, total, percentage, and grade. 

def cal_percentage(marks_array):
    total = sum(marks_array)
    percentage = (total/500)*100

    for i in range(len(marks_array)):
        print("Sub",i,"=",marks_array[i])
    print("Total = ",total)
    print("Percentage = ",percentage)

    if percentage>=75 and percentage<=99:
        print("A grade")
    elif percentage>=60 and percentage<=74:
        print("B grade")
    elif percentage<=59 and percentage>=45:
        print("C grade")
    else:
        print("Fail")

marks =[89,90,91,92,93]
cal_percentage(marks)