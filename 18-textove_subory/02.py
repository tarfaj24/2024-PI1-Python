try:
    subor = open("subor.txt","r") 

    while True:
        riadok = subor.readline()
        if riadok == "":
            break 
        print(riadok.strip())

    subor.close()
except:
    print("súbor neexistuje")