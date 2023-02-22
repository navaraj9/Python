# m rupees
# c price
# k chocolates
# w wrappers
inp="15, 2, 3, 1"
mcwk = list(inp.split(","))

m = int(mcwk[0])
c = int(mcwk[1])
w = int(mcwk[2])
k = int(mcwk[3])

choc = m // c

wrapper = choc

while wrapper >= w:
    choc = choc + ((wrapper // w)*k)
    wrapper = ((wrapper // w)*k) +wrapper % w

print(choc)