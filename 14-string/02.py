inp = input("zadaj retazec: ")
dlzka = len(inp)
print(f"dlzka retazca je {dlzka} ")
for znak in inp:
    print(znak)

# for i in range(len(inp)-1,-1,-1):
#      print(inp[i])


for znak in reversed(inp):
    print(znak)


for znak in inp:
    print(f"{3*znak}")  #zretazenie