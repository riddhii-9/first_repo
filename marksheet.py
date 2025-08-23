#Write a python program to create a student's marksheet
student_name=input("Ente the student's name: ")
rno=int(input("Enter student's roll no: "))
sub1=input("Enter sub1 name: ")
sub2=input("Enter sub2 name: ")
sub3=input("Enter sub3 name: ")

sub1_marks=float(input(f"Enter marks in {sub1} : "))
sub2_marks=float(input(f"Enter marks in {sub2} : "))
sub3_marks=float(input(f"Enter marks in {sub3} : "))

subjects=[sub1,sub2,sub3]
marks=[sub1_marks,sub2_marks,sub3_marks]
total_marks=sum(marks)
avg_marks=total_marks/len(marks)
percentage=(total_marks/(len(marks)*100))*100
grade=None
if percentage>=90:
    grade='A+'
elif percentage>=80:
    grade='B+'
elif percentage>=70:
    grade='C+'
elif percentage>=60:
    grade='D+'
else:
    grade='F'

print("Student's Marksheet")
print("-----------------------")
print(f"Name: {student_name}")
print(f"Roll No: {rno}")
print("Subject\t\tMarks Obtained")
for subject, mark in zip(subjects,marks):
    print(f"{subject}\t\t{mark}")
print("---------------------------")
print(f"Total marks: {total_marks}")
print(f"Average marks: {avg_marks}")
print(f"Percentage: {percentage}")
print(f"Grade: {grade}")
print("------------------------------")
print("End of marksheet")
