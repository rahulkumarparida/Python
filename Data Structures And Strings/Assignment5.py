#Task 1: Create a Dictionary of Student Marks
StudentMark = {"Rahul" : 10 , "Swayam" : 15 , "Satya" : 20, "Jagadish": 25,"Soumya": 30 , "Hitesh": 40}
print({i for i in StudentMark})
name = input("Enter the Student Name Among the Above : ")
if name in StudentMark:
    print(name+"'s marks: ",StudentMark[name])
else:
    print("Student not found")


# Task 2: Demonstrate List Slicing
list = [i for i in range(1,11)]
extracted_list = [i for i in list if i <= 5]
print("Orignal list: ",list)
print("Extracted first five elements: ",extracted_list)
extracted_list.reverse()
print("Reversed extracted elements: ", extracted_list )