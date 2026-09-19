students = []

while True:

    print("\n===== STUDENT RESULT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Display Topper")
    print("5. Display Passed Students")
    print("6. Display Failed Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        department = input("Enter Department: ")

        tamil = int(input("Enter Tamil Mark: "))
        english = int(input("Enter English Mark: "))
        maths = int(input("Enter maths Mark: "))
        science = int(input("Enter science Mark: "))
        socialscience = int(input("Social Science Mark: "))

        total = tamil + english + maths + science+ socialscience
        average = total / 5

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        if tamil >= 40 and english >= 40 and maths >=40 and science >=40 and socialscience >=40 :
            result = "PASS"
        else:
            result = "FAIL"

        student = [name, roll, department, tamil, english, maths, science, socialscience,
                   total, average, grade, result]

        students.append(student)

        print("\nStudent added successfully!")

    elif choice == 2:

        if len(students) == 0:
            print("No student records found.")

        else:
            for student in students:

                print("\n----------------------------")
                print("       STUDENT MARK SHEET")
                print("----------------------------")

                print("Name            :", student[0])
                print("Roll No         :", student[1])
                print("Department      :", student[2])
                print("Tamil           :", student[3])
                print("English         :", student[4])
                print("Maths           :", student[5])
                print("science         :", student[6])
                print("Social Science  :", student[7])
                print("Total           :", student[8])
                print("Average         :", student[9])
                print("Grade           :", student[10])
                print("Result          :", student[11])

    elif choice == 3:

        roll = input("Enter Roll Number to Search: ")

        found = False

        for student in students:

            if student[1] == roll:

                print("\n----------------------------")
                print("       STUDENT DETAILS")
                print("----------------------------")

                print("Name            :", student[0])
                print("Roll No         :", student[1])
                print("Department      :", student[2])
                print("Tamil           :", student[3])
                print("English         :", student[4])
                print("Maths           :", student[5])
                print("science         :", student[6])
                print("Social Science  :", student[7])
                print("Total           :", student[8])
                print("Average         :", student[9])
                print("Grade           :", student[10])
                print("Result          :", student[11])


                found = True

        if found == False:
            print("Student not found.")

    elif choice == 4:

        if len(students) == 0:
            print("No student records found.")

        else:
            topper = students[0]

            for student in students:

                if student[9] > topper[9]:
                    topper = student

            print("\n===== TOPPER =====")
            print("Name    :", topper[0])
            print("Roll No :", topper[1])
            print("Average :", topper[9])
            print("Grade   :", topper[10])

    elif choice == 5:

        print("\n===== PASSED STUDENTS =====")

        for student in students:

            if student[11] == "PASS":
                print(student[0], "-", student[1])

    elif choice == 6:

        print("\n===== FAILED STUDENTS =====")

        for student in students:

            if student[11] == "FAIL":
                print(student[0], "-", student[1])

    elif choice == 7:

        print("Thank you!")
        break

    else:
        print("Invalid choice.")
