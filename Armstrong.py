n = 40

n1 = n // 100
n2 = (n - (n1 * 100)) // 10
n3 = n - ((n // 10) * 10)

Arm = (n1 ** 3) + (n2 ** 3) + (n3 ** 3)
if n == Arm:
    print("True")
else:
    print("False")
