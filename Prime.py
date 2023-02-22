n = 10
prime = []
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

Sum=0
for k in prime:
    Sum=Sum+k

print(Sum)