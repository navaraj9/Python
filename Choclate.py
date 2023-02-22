# take input here
input_date = "15,2".split(",")
m = int(input_date[0])
c = int(input_date[1])
# start writing your code here
choc = m // c
w = choc
while (w // 3 != 0):
    choc = choc + w // 3
    w = w % 3 + w // 3

# dont forget to print the number of chocolates Sanjay can eat
print(choc)