import datetime

class Osoba: #triedy vždy píšeme veľkým prvým písmenom
    def __init__(self, meno, priezvisko, rok_narodenia): #"Konštruktor", zavolá sa pri vzniku objektu
        self.meno = meno #atribút objektu (vlastnosť)
        self.priezvisko = priezvisko
        self.rok_narodenia = rok_narodenia
        self.vek = datetime.date.today().year - self.rok_narodenia
    def pozdrav(self): #"metóda" (čo vie objekt robiť /činnosť)
        print(f"Ahoj, ja som {self.meno} {self.priezvisko} a narodil som sa v roku {self.rok_narodenia} a mám {self.vek} rokov.")

    def vypis_meno(self):
        print(self.meno,self.priezvisko)

    def vypis_vek(self):
        print(self.vek)
    
    def vypis_rok(self):
        print(self.rok_narodenia)

class Student(Osoba): #trieda Student zdedí atribúty a metódy od triedy Osoba
    def __init__(self, meno, priezvisko, rok_narodenia,trieda):
        super().__init__(meno, priezvisko, rok_narodenia) #super - znamená, že použije atribúty z rodičovskej triedy(Osoba)
        # Osoba.__init__(meno, priezvisko, rok_narodenia) to isté
        self.trieda = trieda
    def pozdrav(self):
        super().pozdrav()
        print(f"Som študentom {self.trieda} triedy.")
        #polymorfizmus - meníme metódu pozdrav z rodičovskej triedy
# Jano = Osoba("Ján","Suchý",1966) #vznikne objekt "Jano" vytvorený pomocou triedy Osoba
# Jano.pozdrav()#voláme metódu objektu pozdrav
# Fero = Osoba("František","Mikloško",1990)
# Fero.pozdrav()

# Jano.vypis_meno()
# Jano.vypis_rok()
# Jano.vypis_vek()

student = Student("Ján",  "Študent",2008,"1.AT")
student.pozdrav()
student.vypis_meno()
student.vypis_rok()
student.vypis_vek()

clovek = Osoba("Jurko","Mrkvička",2000)
clovek.pozdrav()