import random
import string

def generate_password(length: int=10):
    word= string.ascii_lettersp + string.digits +string.punctuation
    password=''.join(random.choice(word) for i in range(length))
    return password 
password = generate_password()
print(f"generated password:{password}")