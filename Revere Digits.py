# take input of the number here
Input_number = '123'

# write code to reverse the number here
reverse_number = ""
i = len(Input_number) - 1

while i >= 0:
    reverse_number = reverse_number + Input_number[i]
    i = i - 1

#print reverse_number

print int(reverse_number)
