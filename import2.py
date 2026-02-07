 
import math
import random
import datetime
import os

 
def area_of_circle():
    r = float(input("Enter radius: "))
    area = math.pi * r * r
    print("Area of Circle =", area)

 
def random_number():
    print("Random number between 1 and 100:", random.randint(1, 100))

 
def show_datetime():
    now = datetime.datetime.now()
    print("Current Date and Time:", now)

 
def create_file():
    name = input("Enter your name: ")
    with open("student.txt", "w") as file:
        file.write("Student Name: " + name)
    print("File created successfully!")

 
def read_file():
    if os.path.exists("student.txt"):
        with open("student.txt", "r") as file:
            print(file.read())
    else:
        print("File does not exist!")

 
def menu():
    while True:
        print("\n===== STUDENT UTILITY SYSTEM =====")
        print("1. Area of Circle")
        print("2. Generate Random Number")
        print("3. Show Date and Time")
        print("4. Create File")
        print("5. Read File")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            area_of_circle()
        elif choice == 2:
            random_number()
        elif choice == 3:
            show_datetime()
        elif choice == 4:
            create_file()
        elif choice == 5:
            read_file()
        elif choice == 6:
            print("Exiting Program... Thank you!")
            break
        else:
            print("Invalid choice! Try again.")

 
menu()
