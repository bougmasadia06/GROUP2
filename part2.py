print("*** UNIVERSITY SCHOOL FEES MANAGEMENT SYSTEM ***\n")


class Student:
    def __init__(self, name, student_id, email, phone, academic_year,
                 university, faculty, total_fee, amount_paid, months_remaining, has_scholarship):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.phone = phone
        self.academic_year = academic_year
        self.university = university
        self.faculty = faculty
        self.total_fee = total_fee
        self.amount_paid = amount_paid
        self.months_remaining = months_remaining
        self.has_scholarship = has_scholarship

        # calculate balance and payments
        self.balance_due = self.total_fee - self.amount_paid
        if self.total_fee > 0:
            self.percentage_paid = (self.amount_paid / self.total_fee) * 100
        else:
            self.percentage_paid = 0

        if self.months_remaining > 0:
            self.monthly_payment = self.balance_due / self.months_remaining
        else:
            self.monthly_payment = 0

    def show_info(self):
        print("\n--- STUDENT INFORMATION ---")
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("University:", self.university)
        print("Faculty:", self.faculty)
        print("Academic Year:", self.academic_year)
        if self.has_scholarship == True:
            print("Scholarship: Yes")
        else:
            print("Scholarship: No")
        print("Total Fees:", format(self.total_fee, ".2f"), "CFA")
        print("Amount Paid:", format(self.amount_paid, ".2f"), "CFA")
        print("Balance Due:", format(self.balance_due, ".2f"), "CFA")
        print("Percentage Paid:", format(self.percentage_paid, ".2f"), "%")
        print("Monthly Payment Remaining:", format(self.monthly_payment, ".2f"), "CFA/month")
        print("Email:", self.email)
        print("Phone:", self.phone)

    def get_basic_info(self):
        basic = (self.name, self.student_id, self.university)
        return basic

    def is_fully_paid(self):
        if self.balance_due <= 0:
            return True
        else:
            return False

    def payment_status(self):
        if self.percentage_paid >= 100:
            return "Fully Paid"
        elif self.percentage_paid >= 50:
            return "Partially Paid"
        else:
            return "Payment Needed"


class StudentDatabase:
    def __init__(self):
        self.students = []  # list to store students
        self.universities = {}  # dictionary to count students by university

    def add_student(self, student):
        self.students.append(student)
        if student.university in self.universities:
            self.universities[student.university] += 1
        else:
            self.universities[student.university] = 1
        print(student.name, "has been added to the system.")

    def show_all_students(self):
        if len(self.students) == 0:
            print("No students in the database yet.")
        else:
            print("\n=== ALL STUDENTS ===")
            count = 1
            for student in self.students:
                print("\nStudent #", count)
                student.show_info()
                count += 1

    def get_stats(self):
        if len(self.students) == 0:
            print("No students to calculate statistics.")
        else:
            total_fees = 0
            total_paid = 0
            scholarship_count = 0
            fully_paid_count = 0

            for student in self.students:
                total_fees += student.total_fee
                total_paid += student.amount_paid
                if student.has_scholarship == True:
                    scholarship_count += 1
                if student.is_fully_paid() == True:
                    fully_paid_count += 1

            print("\n*** DATABASE STATISTICS ***")
            print("Total Students:", len(self.students))
            print("Total Fees:", format(total_fees, ".2f"), "CFA")
            print("Total Paid:", format(total_paid, ".2f"), "CFA")
            print("Students with Scholarship:", scholarship_count)
            scholarship_percent = (scholarship_count / len(self.students)) * 100
            print("Scholarship Percentage:", format(scholarship_percent, ".1f"), "%")
            print("Fully Paid Students:", fully_paid_count)

            print("\n--- Students by University ---")
            for uni in self.universities:
                print(uni, ":", self.universities[uni], "student(s)")


def get_student_info():
    print("\nEnter student information:")
    name = input("Full Name: ")
    student_id = int(input("Student ID: "))
    academic_year = input("Academic Year: ")
    university = input("University Name: ")
    faculty = input("Faculty/Department: ")
    email = input("Email: ")
    phone = input("Phone: ")
    total_fee = float(input("Total Tuition Fees (CFA): "))
    amount_paid = float(input("Amount Paid (CFA): "))
    months_remaining = int(input("Months Remaining to Pay: "))
    has_scholarship_input = input("Scholarship (yes/no): ").lower()
    if has_scholarship_input == "yes":
        has_scholarship = True
    else:
        has_scholarship = False

    student = Student(name, student_id, email, phone, academic_year, university,
                      faculty, total_fee, amount_paid, months_remaining, has_scholarship)
    return student


def show_payment_report(database):
    print("\n*** PAYMENT STATUS REPORT ***")
    
    fully_paid = []
    partially_paid = []
    payment_needed = []

    for student in database.students:
        status = student.payment_status()
        if status == "Fully Paid":
            fully_paid.append(student.name)
        elif status == "Partially Paid":
            partially_paid.append(student.name)
        else:
            payment_needed.append(student.name)

    print("\nFully Paid:", len(fully_paid))
    if len(fully_paid) == 0:
        print("No students are fully paid.")
    else:
        for name in fully_paid:
            print(" -", name)

    print("\nPartially Paid:", len(partially_paid))
    if len(partially_paid) == 0:
        print("No students are partially paid.")
    else:
        for name in partially_paid:
            print(" -", name)

    print("\nPayment Needed:", len(payment_needed))
    if len(payment_needed) == 0:
        print("No students need to pay.")
    else:
        for name in payment_needed:
            print(" -", name)


def show_scholarship_students(database):
    print("\n=== SCHOLARSHIP STUDENTS ===")
    found = False
    for student in database.students:
        if student.has_scholarship == True:
            found = True
            info = student.get_basic_info()
            print("Name:", info[0], "ID:", info[1], "University:", info[2])
            print("Balance:", format(student.balance_due, ".2f"), "CFA")
    if found == False:
        print("No scholarship students found.")


# MAIN PROGRAM
db = StudentDatabase()
running = True

while running:
    print("\n*** MAIN MENU ***")
    print("1. Add new student")
    print("2. View all students")
    print("3. Search for a student by ID")
    print("4. View statistics")
    print("5. Show scholarship students")
    print("6. Payment status report")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        student = get_student_info()
        db.add_student(student)

    elif choice == "2":
        db.show_all_students()

    elif choice == "3":
        student_id = int(input("Enter student ID to search: "))
        found_student = None
        for student in db.students:
            if student.student_id == student_id:
                found_student = student
                break
        if found_student:
            print("\nStudent found!")
            found_student.show_info()
        else:
            print("Student not found in the database.")

    elif choice == "4":
        db.get_stats()

    elif choice == "5":
        show_scholarship_students(db)

    elif choice == "6":
        show_payment_report(db)

    elif choice == "7":
        print("Goodbye!")
        running = False

    else:
        print("Invalid choice. Please enter a number from 1-7.")