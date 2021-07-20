#隣り合った数の絶対値の最大を求める

nums = [int(e) for e in input().split()]
    
max_abs = 0

for i in range(len(nums) - 1):
    list_abs = abs(nums[i] - nums[i + 1])
    if list_abs > max_abs :
        max_abs = list_abs

print(max_abs)