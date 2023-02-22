import onetimepad

plaintext = 'Learning with UPGRAD is cool'

# Set the OTP KEY which is typically >= length of plaintext
key = "CyberSecurity keeps the digital world safer and happier"

print("\n plaintext1: " + plaintext)

# Generate CIPHER & Print
cipher = onetimepad.encrypt(plaintext, key)

print("\n cipher1: " + cipher)

# DECRYPTE CIPHER & Print

#cipher = onetimepad. (cipher, key)
