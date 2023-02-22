# input n taken here
n = 13

# we will make a list of lists with just [1] in it. We will run a for loop from i= 2 to n and in each iteration
# we will add [i]*(2i-3) in top of the list and and in bottom
# then add i on both sides of all sub_lists

answer = [[1]]
for i in range(2, n + 1):
    t = [i] * ((2 * i) - 3)
    answer.insert(0, t)
    answer.append(t)

    for a in answer:
        a.insert(0, i)
        a.append(i)
        if a[len(a) // 2] != 1:
            continue
        else:
            break

for a in answer:
    for i in a:
        print(i, end="")
    print()
