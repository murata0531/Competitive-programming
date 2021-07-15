N = 6
sum = 0


#6つの食べ物のカロリーを入れる
list1 = list(map(int, input().strip().split()))

#3人の人を格納する
list2 = list(input().strip().split())


for i in range(N):
    if list2[i] == 'Alice' :
        sum += list1[i]

print(sum)