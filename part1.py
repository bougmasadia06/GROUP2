

print("*** UNIVERSITY SCHOOL FEES MANAGEMENT SYSTEM ***")

print("\nPlease enter the student's information:")

#  Student Informations
student_name = input("Full name of the student: ")
student_id = int(input("Student identification number: "))

academic_year = input("Academic year : ")
university_name = input("University name: ")
faculty_name = input("Faculty/Department: ")
email_address = input("Student email address: ")
phone_number = int(input("Phone number: "))

#  Fees, Amount paid by the Student and the Remaining Month
total_fee = float(input("Total tuition fees (CFA): "))
amount_paid = float(input("Amount already paid (CFA): "))
months_remaining = int(input("Number of months remaining to pay: "))

#  BOOLEAN : Does the student have a scholarship or not
has_scholarship_input = input("Has a scholarship (yes/no): ")

#  ARITHMETIC CALCULATIONS
# Remaining balance to pay
balance_due = total_fee - amount_paid

#  Percentage of fees already paid
percentage_paid = (amount_paid / total_fee) * 100

#  Average monthly payment
monthly_payment = balance_due / months_remaining

#  SUMMARY DISPLAY
print("\n*****")
print("ACADEMIC RECORD - COMPLETE SUMMARY")
print("\n*****")

print("\n PERSONAL INFORMATION")
print(f"   Name: {student_name}")
print(f"   ID: {student_id}")
print(f"   University: {university_name}")
print(f"   Faculty: {faculty_name}")


print("\n ACADEMIC INFORMATION")
print(f"   Year: {academic_year}")


print("\n FINANCIAL SITUATION")
print(f"   Total fees: {total_fee:} CFA")
print(f"   Amount paid: {amount_paid:} CFA")
print(f"   Balance due: {balance_due:} CFA")
print(f"   Percentage paid: {percentage_paid:}%")
print(f"   Remaining monthly payment: {monthly_payment:} CFA/month")

print("\n CONTACT INFORMATION")
print(f"   Email: {email_address}")
print(f"   Phone: {phone_number}")

print("\n*****")
print("Thank you for using our academic management system!")
print("\n*****")
