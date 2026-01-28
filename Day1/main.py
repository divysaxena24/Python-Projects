#User Profile validation System

full_name = input("Enter Full Name: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile No. ")
age = int(input("Enter Age: "))

name_valid = False
if full_name[0]!=' ' and full_name[-1]!=' ':
    if full_name.count(" ")>=1:
        name_valid = True

email_valid = False
if '@' in email and "." in email:
    if email[0] != "@":
        email_valid = True

mobile_valid = False
if len(mobile) == 10 and mobile.isDigit() and mobile[0] != "0":
    mobile_valid = True

age_valid = False
if age >= 18 and age <= 60:
    age_valid = True

if name_valid and email_valid and mobile_valid and age_valid:
    print("User Profile is Valid")
else:
    print("Invalid user Profile")
    if not name_valid:
        print("Invalid Name")
    if not email_valid:
        print("Invalid Email ID")
    if not mobile_valid:
        print("Invalid Mobile No.")
    if not age_valid:
        print("Invalid Age")
    
