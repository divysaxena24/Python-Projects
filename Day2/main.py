# Smart ID & Credential Validator
# Course: CSE205 | Day-2 Challenge

# INPUTS
student_id = input().strip()
email = input().strip()
password = input().strip()
referral = input().strip()

# ---------------- STUDENT ID VALIDATION ----------------
valid_id = False
if len(student_id) == 7:
    if student_id[0:3] == "CSE" and student_id[3] == "-":
        if student_id[4].isdigit() and student_id[5].isdigit() and student_id[6].isdigit():
            valid_id = True

# ---------------- EMAIL VALIDATION ----------------
valid_email = False
if "@" in email and "." in email:
    if email[0] != "@" and email[-1] != "@":
        if email.endswith(".edu"):
            valid_email = True

# ---------------- PASSWORD VALIDATION ----------------
valid_password = False
has_digit = (
    ("0" in password) or ("1" in password) or ("2" in password) or
    ("3" in password) or ("4" in password) or ("5" in password) or
    ("6" in password) or ("7" in password) or ("8" in password) or ("9" in password)
)

if len(password) >= 8:
    if password[0].isupper():
        if has_digit:
            valid_password = True

# ---------------- REFERRAL CODE VALIDATION ----------------
valid_referral = False
if len(referral) == 6:
    if referral[0:3] == "REF":
        if referral[3].isdigit() and referral[4].isdigit():
            if referral[5] == "@":
                valid_referral = True

# ---------------- FINAL DECISION ----------------
if valid_id and valid_email and valid_password and valid_referral:
    print("APPROVED")
else:
    print("REJECTED")
