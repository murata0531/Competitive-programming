import sys

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

#入力回数と各行複数（空白区切り）の入力値の標準入力の取得

#行毎にリストに取得する
N = int(input())
list_x = []
for i in range(N):
    array = list(map(int, input().split()))
    list_x.append(array)
print(list_x)

#列毎にリストに取得する
N = int(input())
list_x = []
list_y = []
for i in range(N):
    x, y = map(int,input().split())
    list_x.append(x)
    list_y.append(y)
print(list_x)
print(list_y)