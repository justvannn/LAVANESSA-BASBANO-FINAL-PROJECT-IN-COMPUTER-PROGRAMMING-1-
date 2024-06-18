print('Number 8.')
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = 8  # You can change the length as per your requirement
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)

