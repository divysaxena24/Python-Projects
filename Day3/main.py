student_name = input("Enter your name : ")
name_length = len(student_name)

n = int(input("Enter number of students : "))

marks = []
for i in range(n):
    m = int(input("Enter Mark :"))
    marks.append(m)

valid_count = 0
fail_count = 0

for m in marks:
    if name_length % 2 == 0:
        tag = "(Checked by even-logic)"
    else:
        tag = "(checked by odd-logic)"

    if m < 0 or m > 100:
        print(m, "Invalid Mark", tag)
    else:
        valid_count += 1
        if m >= 90:
            print(m, "Excellent", tag)
        elif m >= 75:
            print(m, "Very Good", tag)
        elif m >= 60:
            print(m, "Good", tag)
        elif m >= 40:
            print(m, "Average", tag)
        else:
            print(m, "Fail", tag)
            fail_count += 1

print("Valid Students : ", valid_count)
print("Fail Students : ", fail_count)