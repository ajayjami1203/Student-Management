import json
import os


if not os.path.exists('students.json'):
    with open('students.json', 'w') as f:
        json.dump({}, f)

def add_student_record():
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    try:
        with open('students.json', 'r+') as f:
            data = json.load(f)
            if roll_number in data:
                print("Roll number already exists!")
            else:
                data[roll_number] = {"name": name, "marks": marks}
                f.seek(0)
                json.dump(data, f)
                f.truncate()
                print("Student record added successfully!")
    except json.JSONDecodeError:
        print("Invalid JSON format!")
    except Exception as e:
        print("An error occurred: ", str(e))

def view_student_records():
    try:
        with open('students.json', 'r') as f:
            data = json.load(f)
            if not data:
                print("No student records found!")
            else:
                print("Student Records:")
                for roll_number, student in data.items():
                    print(f"Roll No: {roll_number}, Name: {student['name']}, Marks: {student['marks']}")
    except json.JSONDecodeError:
        print("Invalid JSON format!")
    except Exception as e:
        print("An error occurred: ", str(e))

def search_student_by_roll_number():
    roll_number = input("Enter Roll Number to search: ")
    try:
        with open('students.json', 'r') as f:
            data = json.load(f)
            if roll_number in data:
                student = data[roll_number]
                print(f"Student Found: Name: {student['name']}, Marks: {student['marks']}")
            else:
                print("Roll number not found!")
    except json.JSONDecodeError:
        print("Invalid JSON format!")
    except Exception as e:
        print("An error occurred: ", str(e))

def update_student_record():
    roll_number = input("Enter Roll Number to update: ")
    try:
        with open('students.json', 'r+') as f:
            data = json.load(f)
            if roll_number in data:
                name = input("Enter new Name: ")
                marks = input("Enter new Marks: ")
                data[roll_number] = {"name": name, "marks": marks}
                f.seek(0)
                json.dump(data, f)
                f.truncate()
                print("Student record updated successfully!")
            else:
                print("Roll number not found!")
    except json.JSONDecodeError:
        print("Invalid JSON format!")
    except Exception as e:
        print("An error occurred: ", str(e))

def delete_student_record():
    roll_number = input("Enter Roll Number to delete: ")
    try:
        with open('students.json', 'r+') as f:
            data = json.load(f)
            if roll_number in data:
                del data[roll_number]
                f.seek(0)
                json.dump(data, f)
                f.truncate()
                print("Student record deleted successfully!")
            else:
                print("Roll number not found!")
    except json.JSONDecodeError:
        print("Invalid JSON format!")
    except Exception as e:
        print("An error occurred: ", str(e))

def main():
    while True:
        print("\nWelcome to Student Management System")
        print("1. Add Student Record")
        print("2. View Student Records")
        print("3. Search Student by Roll Number")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student_record()
        elif choice == "2":
            view_student_records()
        elif choice == "3":
            search_student_by_roll_number()
        elif choice == "4":
            update_student_record()
        elif choice == "5":
            delete_student_record()
        elif choice == "6":
            print("Exiting the management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()