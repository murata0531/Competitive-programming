import sys

r_flag = "D"
w_flag = "D"
winner = "Simon"
result = False

r = input().split()
for i in range(len(r)) :
    if (r[i] == "RU" and r_flag == "U") or (r[i] == "RD" and r_flag == "D") or (r[i] == "WU" and w_flag == "U") or (r[i] == "WD" and w_flag == "D") :
        winner = "Alice"
        result = True
    if r[i] == "RU" :
        r_flag = "U"
    elif r[i] == "RD" :
        r_flag = "D"
    elif r[i] == "WU" :
        w_flag = "U"
    elif r[i] == "WD" :
        w_flag = "D"

    if result == True :
        break

print(winner)

if winner != "Alice" :
    print(r_flag + w_flag)
    
