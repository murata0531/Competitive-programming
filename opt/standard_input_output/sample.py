#2つの数字だけ標準入力を行う
a,b=map(int,input().split())

print(a)

#入力回数を決める
N=int(input())

#内包表記で数値を入れる
a,b,c=[int(input()) for i in range(N)]
print(a,b,c)

#普通のfor文で数値を入れる
list=[]
for i in range(N):
    list.append(int(input()))

print(list)