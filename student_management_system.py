
student_name = input("Enter Student Full Name:")
roll_no =(input("Enter Your Roll Number:"))
department = input("Enter Department:")
semester = input("Enter Semester:")
age = int(input("Enter Your Age:"))
gender = input("Enter Gender(Male/Female):")
phone_no = (input("Enter Your Phone Number(xxxx-xxxxxxx):"))
email = input("Enter Your Email:")
city = input("Enter City:")
admission_year = int(input("Enter Admission Year:"))

english_marks = int(input("Enter English Marks:"))
maths_marks = int(input("Enter Maths Marks:"))
physics_marks = int(input("Enter Physics Marks:"))
computer_marks= int(input("Enter Computer Marks:"))
urdu_marks = int(input("Enter Urdu Marks:"))
city = input("Enter City:")
admission_year = int(input("Enter Admission Year:"))
personal_information = {
    "Student Name: " : student_name,
    "Student Roll No: ": roll_no,
    "Department:" : department,
    "Semester:" : semester,
    "Student Age:": age,
    "Gender:" : gender,
    "Student Phone No:" : phone_no,
    "Student Email:" : email,
    "Student City Name:" : city,
    "Student Admission Year:" :admission_year
}
academic_information = {
    "Student English Marks:" : english_marks,
    "Student Maths Marks:" : maths_marks,
    "Student Physics Marks:" : physics_marks,
    "Student Computer Marks:" : computer_marks,
    "Student Urdu Marks:" : urdu_marks,
}

total_marks  =  maths_marks + english_marks + physics_marks + computer_marks + urdu_marks
print (total_marks)

total_percentage = round((total_marks)*100 / 500)
print (total_percentage)



if (total_percentage>=90):
    grade = "A++"
elif(total_percentage >= 80):
    grade = "A+"
elif(total_percentage >= 70):
    grade = "A"
elif(total_percentage >= 60):
    grade = "B" 
elif(total_percentage >= 50):
    grade = "C"  
elif(total_percentage >= 40):
    grade = "D" 
else:
    grade = "Fail"   

print ("_________Student Information__________")
print("Student Personal Information:")
print (personal_information)
print("Student Academic Information:")
print (academic_information)
print ("Total Marks: " , total_marks)
print ("Total Percentage: ", total_percentage)
print ("Student Grade: " , grade)


