# fibbonaci
#saberi poslednja dva broja

# sabiraj do 100
# [0,1]
# 0 + 1 = 1 , [0,1,1]
# 1 + 1 = 2, [0,1,1,2]
# 1 + 2 = 3, [0,1,1,2,3]
# 2 + 3 = 5, [0,1,1,2,3,5] ...

fib = [0,1]

fib_len = len(fib)
print(fib_len)
desired_output = 100

while fib[-1] <= desired_output:
    next_number = fib[-1] + fib[-2]
    if next_number > desired_output:
        break
    fib.append(next_number)

print(fib)