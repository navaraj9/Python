n = 4
Alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
# Write your code below
for i in range(1,n+1):
    for j in range(n-i):
        print("__", end='')
    print(Alpha[n-i], end='')
    for k in range(n-i):
        print("__", end='')
    #for l in range

    print("")