import random

# Define KEY GENERATION FUNCTION
def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789 "
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key

# Define ENCRYPTION FUNCTION
def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def dencrypt(key, cipher):
    message = ""
    for c in cipher:
        if c in key:
            message += key[c]
        else:
            message += c
    return message

# Define GET DECRYPTION KEY
def get_decrypt_key(key):
    dkey ={}

    for k in key:
        dkey[key[k]]=k
    return dkey


# Write your code here

# MAIN BLOCK

# Generate Key
key = generate_key()

# Print Key
print("\nKey:"+ str(key) )

# PlainText Message
message = "WELCOME TO THE CYBER WORLD"

print("\nPlainText:"+ message )

# CipherText creation (encrypting the plaintext using the key)
cipher = encrypt(key, message)

print("\nCipher:"+cipher)

# Get & Print the Decryption Key
dkey = get_decrypt_key(key)
print("\nDecryption Key:"+ str(dkey) )

# Decryption
message = dencrypt(dkey, cipher)

print(message)

# END
