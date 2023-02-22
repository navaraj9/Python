# Python program to explain os.makedirs() method

# importing os module
import os


def file_read_write(input_string):
    f = open("filename.txt", 'w+')
    f.write(input_string)
    f.close()

    f_r = open("filename.txt", "r")
    return f_r.read()


print(file_read_write("test"))
