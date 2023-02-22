n = 3233
e = 17
d = 2753
x = 123

# Calculate the cipher = ENCRYPTION
cipher = pow(x, e) % n
# TEST DECRYPTION and print decrypted value
decrypted = pow(cipher, d) % n
print(decrypted)