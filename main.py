import pyperclip
import os

FILE_NAME = "passwords.txt"

def save_password():
    website = input("Enter the website: ")
    password = input("Enter the password: ")
    with open(FILE_NAME, 'a') as f:
        f.write(f"{website}<||>{password}\n")

def get_password():
    website = input("Enter the website: ")
    found = False

    with open(FILE_NAME, 'r') as f:
        for line in f:
            parts = line.split("<||>")
            if parts[0].strip() == website:
                password = parts[1].strip()
                pyperclip.copy(password)
                print("Password copied to clipboard!")
                found = True
                break
    if not found:
        print("Website not found.")
        
def main():
    while True:
        print("1. Save a password")
        print("2. Get a password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            save_password()
        elif choice == '2':
            get_password()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()