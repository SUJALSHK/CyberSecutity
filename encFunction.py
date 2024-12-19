import random
import string

def generate_cipher_key():
    """Generate a shuffled cipher key from the list of characters."""
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    return chars, key

def encrypt_message(plain_text, chars, key):
    """Encrypt a given plain text using the cipher key."""
    cipher_text = ""
    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter  # Leave characters not in chars as-is
    return cipher_text

def decrypt_message(cipher_text, chars, key):
    """Decrypt a cipher text using the cipher key."""
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += chars[index]
        else:
            plain_text += letter  # Leave characters not in key as-is
    return plain_text

def main():
    """Main function to execute the program."""
    chars, key = generate_cipher_key()
    #print(f"chars: {chars}")
    #print(f"key: {key}")
    
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = encrypt_message(plain_text, chars, key)
    print(f"Original message: {plain_text}")
    print(f"Cipher text: {cipher_text}")
    
    decrypted_text = decrypt_message(cipher_text, chars, key)
    print(f"Decrypted text: {decrypted_text}")



if __name__ == "__main__":
    main()
