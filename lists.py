l=[3,5,6]
print(l)
print (type(l))
print(l[0])

# Create an empty list
students = []

while True:
    print("\n--- Student List Menu ---")
    print("1. Add student")
    print("2. Display students")
    print("3. Search student")
    print("4. Remove student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == 2:
        if students:
            print("Student List:")
            for s in students:
                print(s)
        else:
            print("List is empty")

    elif choice == 3:
        name = input("Enter student name to search: ")
        if name in students:
            print("Student found!")
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
            print("Student removed successfully!")
        else:
            print("Student not found")

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice! Try again.")
