# take input of the number here
Input_number = 6752343

# write code to reverse the number here
reverse_number =0
while Input_number != 0:
    reverse_number = (reverse_number*10) + Input_number % 10

    Input_number = Input_number // 10

# print reverse_number

print reverse_number
