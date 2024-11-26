od = int(input('zadaj od: '))
do = int(input('zadaj do: '))
for i in range(od, do + 1):
    for j in range(od, do + 1):
        print(f'{i * j:4}',end =' ')
    print()

    
    
    

