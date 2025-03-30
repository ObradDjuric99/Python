#bubble sort

#sortira elemente

# comparison
# swap (mijenjanje)
# multiplepasses (radi sve dok ne zavrsi te prve dvije akcije)


#pass: 1 compare 5 and 1 -> 5 1,5,4,2,8 -> 5 and 4 -> 1,4,5,2,8

# pass: 2 compare 1 and 4 -> 1,4,5,2,8

numbers = [5,1,4,2,8]

numbers_length = len(numbers)

for i in range(numbers_length):
    swapped = False

    for j in range(0, numbers_length-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            swapped = True
    if not swapped:
        break

print(numbers)
