import random as rand
rows, cols = (5, 5)
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(rand.randrange(7)) # 0 если надо 2д масс из нулей 
    arr.append(col)
print(arr)
print(arr[1:])