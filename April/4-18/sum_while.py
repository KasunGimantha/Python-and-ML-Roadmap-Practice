# while loop that sums numbers until total exceeds 1000
total = 0
count = 0
sum_num = 1
while total < 1000:
    total = total + sum_num
    sum_num = sum_num+1
    count = count + 1


print(f'Total Exceeds {total}')
print(f'it took {count} numbers')
