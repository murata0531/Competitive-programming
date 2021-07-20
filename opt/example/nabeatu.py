def nabeatu(num):
    if num % 3 == 0 or "3" in str(num):
        return True
    else:
        return False

q = 0
range_crazy = int(input("いくつまでアホになりたいですか?:"))
for num in range(1, range_crazy + 1):
    if nabeatu(num) == True :
        q += num
    

print(q)