import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    num_passwords = int(input("How many passwords would you like to generate? "))
    password_length = int(input("What length would you like the passwords to be? "))

    for i in range(num_passwords):
        print(f"Password {i+1}: {generate_password(password_length)}")

if __name__ == "__main__":
    main()
