#トリボナッチ数列 は直前 3 項の和で生成される数列

#Tn+3 = Tn + Tn+1 + Tn+2

# トリボナッチ数列生成関数
def tribonacci_list(n, t0, t1, t2):
    tri = [t0, t1, t2]
    if n == 1:
        tri = [t0]
    elif n == 2:
        tri = [t0, t1]
    else:
        for k in range(3, n):
            tri.append(tri[k-1]+tri[k-2]+tri[k-3])
    return tri

# 1,1,2から始まる10項のトリボナッチ数列
tri = tribonacci_list(10, 1, 1, 2)

print(tri)