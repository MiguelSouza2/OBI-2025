n = int(input()) # col de mesma altura
brr = []
arr = []
for a in (map(int, input().split())):
    arr.append(a)

for i in arr:
    while i <= 0:
        i -= 1
        if i <= 0:
            brr.append(0)
        brr.append(1)
    # depois guardar em um array e inverter
print(arr)
    