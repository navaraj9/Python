n = 5

i = 1
fib_list = [0, 1]
while(i<n):

    fib_list.append(fib_list[i - 1] + fib_list[i])
    i = i + 1
for i in range(len(fib_list)-1):
    print(fib_list[i])