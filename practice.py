# stored username and password
correct_username = "admin"
correct_password = "1234"

 
username = input("Enter username: ")
password = input("Enter password: ")

# login check
if username == correct_username and password == correct_password:
    print("Login successful! Welcome,", username)
else:
    print("Login failed! Invalid username or password")



correct_username = "SHIVAM"
correct_password = "SHIVAM1234"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Wrong details! Attempts left:", attempts)

if attempts == 0:
    print("Account locked!")
