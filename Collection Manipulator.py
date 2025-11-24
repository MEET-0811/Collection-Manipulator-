print("\nWelcome to the Student Data Organizer!")

# Main list to store all student dictionaries
students = []

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter name: ")
    age = int(input("Enter age: "))         # type casting
    grade = input("Enter grade: ")
    subjects = input("Enter subjects (comma separated): ")

    subject_set = set(subjects.split(","))  # set => no duplicates

    student_id = input("Enter student ID: ")
    dob = input("Enter date of birth (DD-MM-YYYY): ")

    # Tuple => immutable
    id_dob = (student_id, dob)

    # Student dictionary
    student_info = {
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subject_set,
        "id_dob": id_dob
    }

    students.append(student_info)
    print("Student added successfully!")


def display_all_students():
    print("\n--- All Student Records ---")
    if not students:
        print("No student records found.")
        return

    for s in students:
        print(f"\nID: {s['id_dob'][0]}")
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Grade: {s['grade']}") 
        print(f"Subjects: {', '.join(s['subjects'])}")


def update_student():
    print("\n--- Update Student Information ---")
    sid = input("Enter student ID to update: ")

    for s in students:
        if s["id_dob"][0] == sid:
            print("1. Update Age")
            print("2. Update Subjects")
            ch = int(input("Enter your choice: "))

            if ch == 1:
                new_age = int(input("Enter new age: "))
                s["age"] = new_age  # list/dict are mutable
                print("Age updated.")
            elif ch == 2:
                new_subs = input("Enter new subjects (comma separated): ")
                s["subjects"] = set(new_subs.split(","))
                print("Subjects updated.")
            else:
                print("Invalid choice.")
            return

    print("Student ID not found.")


def delete_student():
    print("\n--- Delete Student ---")
    sid = input("Enter student ID to delete: ")

    for i, s in enumerate(students):
        if s["id_dob"][0] == sid:
            del students[i]        # using del keyword
            print("Student deleted.")
            return

    print("Student ID not found.")


def display_subjects_offered():
    print("\n--- Subjects Offered ---")
    all_subjects = set()

    for s in students:
        all_subjects.update(s["subjects"])

    print(", ".join(all_subjects) if all_subjects else "No subjects found.")


# ---------------- Main Menu Loop ----------------
while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_all_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_subjects_offered()
    elif choice == "6":
        print("Thank you for using the Student Data Organizer!")
        break
    else:
        print("Invalid choice. Try again!")
