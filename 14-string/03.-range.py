#range() - je funkcia, ktorá vygeneruje nejakú postupnosť
#range(5)- postupnosť 0,1,2,2,4
#range(od,po-1,krok)
#range moze aj klesat  range(5,0,-1)

print(list(range(5)))
print(list(range(2,5,2)))
print(list(range(5,0,-1)))

ret = "ahoj"
for i in range(len(ret)-1,-1,-1):
    print(ret[i])

print(list(reversed(range(1,5))))

