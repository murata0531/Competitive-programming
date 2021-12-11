def fibonacci_list(n):
    fib = [1, 1]
    if n == 1:
        fib = [1]
    else:
        for k in range(2, n):
            fib.append(fib[k-1]+fib[k-2])
    return fib

# フィボナッチ数列を第10項まで求める
fib = fibonacci_list(10)

print(fib)

import sympy

# 10番目のフィボナッチ数を生成
fib = sympy.fibonacci(10)

print(fib)

# フィボナッチ数列を生成
fib = [sympy.fibonacci(x) for x in range(-5, 5)]

print(fib)