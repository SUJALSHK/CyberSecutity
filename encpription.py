import random
import string


chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars:{chars}")
print(f"key:{key}")

#encription
 
plan_text = input("enter an message")
cipher_text=""

for letter in plan_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plan_text}")
print(f"cipher text : {cipher_text}") 