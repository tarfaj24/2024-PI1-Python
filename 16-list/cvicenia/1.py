def sucin(zoznam):
    suc = 1
    for i in range(len(zoznam)):
            suc = suc * zoznam[i]
    print("Súčin čísel v zozname je: ", suc)
          

    return suc


    

zoznam1 = [12,8,6,21]

sucin(zoznam1)