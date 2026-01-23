# **University Fees Management System**

## **Group 2 Members**
- BOUGMA Sadiata (Leader)
- KABORE Awa
- ZONGO Pascal
- WANGRE Delwendé Esther
- KAFANDO Dan Ernest Patrice
- SAWADOGO Sandrine

## **Description**
Python console application for managing university student fees. The system allows adding students, tracking payments, managing scholarships, and generating reports.

## **Problem Solved**
Automates manual university fee management: balance calculation, payment tracking, payment statistics, and scholarship management.

## **Program Structure**

### **Main Classes**
1. **Student**: Stores student information (name, ID, fees, payments, scholarship)
2. **StudentDatabase**: Manages the student collection and statistics

### **Features**
- Add students with complete information
- Automatic calculation: balance, percentage paid, monthly payments
- Search by student ID
- Overall statistics
- Categorized payment report
- Scholarship student filtering

## **How to Run**
1. Make sure Python 3 is installed
2. Copy code to a file `university_fees.py`
3. Run:
```bash
python university_fees.py
```

## **Main Menu**
1. Add student
2. View all students
3. Search by ID
4. View statistics
5. Scholarship students
6. Payment report
7. Exit

## **Design Decisions**
- Data in memory (no persistence)
- Automatic calculations at creation
- Currency: CFA
- Scholarship = yes/no (not percentage)
- Simple console interface

## **Future Improvements**
- Save data to file
- Input validation
- Graphical interface
- Database

---

**Academic Project - 2023-2024**
