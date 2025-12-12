words = {}

 
n = int(input("How many words do you want to add? "))

 
for i in range(n):
    key = input("Enter word: ")
    meaning = input("Enter meaning: ")
    words[key] = meaning

 
search = input("\nEnter a word to search: ")

if search in words:
    print("Meaning:", words[search])
else:
    print("Word not found!")


