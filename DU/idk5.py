od = int(input('zadaj od: '))
do = int(input('zadaj do: '))
print('     |', end=' ')
for j in range(od, do + 1):
    print(f'{j: 4}', end=' ')
print()
print('=====|=' + '=' * (do - od + 1) * 5)
for i in range(od, do + 1):
    print(f'{i: 4} |', end=' ')
    for j in range(od, do + 1):
        print(f'{i * j:4}', end=' ')
    print()