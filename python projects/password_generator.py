import random
import string


def generate_password(length, use_special_chars=False):
    all_characters = string.ascii_letters + string.digits
    if use_special_chars:
        all_characters += string.punctuation

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


def password_generator():
    print("Password Generator")

    length = int(input("Enter the desired password length: "))
    special_chars = input("Include special characters? (yes/no): ").lower()

    if special_chars == 'yes':
        password = generate_password(length, use_special_chars=True)
    else:
        password = generate_password(length)

    print(f"Your generated password is: {password}")


password_generator()
