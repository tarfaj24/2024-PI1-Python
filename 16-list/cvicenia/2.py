def zostupne(zoznam):
    for i in range(len(zoznam)-1):
        if zoznam[i] < zoznam[i+1]:
            return False
    return True
            
                
            
list1 = [5,5,6,3,3,2,1]
print(zostupne(list1))