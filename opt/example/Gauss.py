#4乗的ガウス

range_max= int(input("繰り返し数:"))
sum = 0
for num in range(1, range_max + 1):
    sum += num ** 4

print(sum)