sides = [0 ,0, 1, 1, 4 ,5]  # list of side lengths
n = len(sides)
my_stack = []
i = 0

while (i < n):
    if sides[i] >= sides[n - 1]:
        my_stack.append(sides[i])
        i = i + 1
    else:
        my_stack.append(sides[n - 1])
        n = n - 1

flag = 0
i = 1
while i < len(my_stack):
    if (my_stack[i] > my_stack[i - 1]):
        flag = 1
    i += 1

if (not flag):
    print("Possible")
else:
    print("Impossible")