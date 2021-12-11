import sys
import math
 
def eratosthenes(limit):
    nums = [i for i in range(2, limit+1)]
    primes = []
 
    while True:
        p = min(nums)
 
        if p > math.sqrt(limit):
            break
 
        primes.append(p)
 
        i = 0
        while i < len(nums):
            if nums[i] % p == 0:
                nums.pop(i)
                continue
            i += 1
 
    return primes + nums
 
def main(argv):
    if not argv[0].isdigit():
        print("error")
        return
 
    n = int(argv[0])
 
    if n < 1:
        print("error")
        return
 
    limit = 1000
    while True:
        primes = eratosthenes(limit)
 
        if len(primes) > n:
            print(primes[n-1])
            break
 
        limit *= 2
 
if __name__ == '__main__':
    main(sys.argv[1:])