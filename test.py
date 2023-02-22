n=3
def Series(num1, num2):
    # Converting the number to string
    str_n = str(num1)

    # Initializing result as number and string
    sums = num1
    sum_str = str(num1)

    # Adding remaining terms
    for i in range(1, num2):
        # Concatenating the string making n, nn, nnn...
        sum_str = sum_str + str_n

        # Before adding converting back to integer
        sums = sums + int(sum_str)

    return sums


# Driver Code
num1 = n
num2 = n
total = Series(num1, num2)
print(total)