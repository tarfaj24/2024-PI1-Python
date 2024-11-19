name = input ("Zadaj meno: ")

import tkinter
canvas = tkinter.Canvas(height=600, width=600)
canvas.pack()
def A (x,y):
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)
     
    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+30,x+20,y+40)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+30,x+40,y+40)

    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+30,x+50,y+40)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)
    canvas.create_rectangle(x+40,y+60,x+50,y+70)


def B (x,y):    
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+30,x+20,y+40)
    canvas.create_rectangle(x+10,y+60,x+20,y+70)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+30,x+40,y+40)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)
    
    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)
    
def C (x,y):
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+60,x+20,y+70)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)

    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)

def D (x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+60,x+20,y+70)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)

    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+30,x+50,y+40)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)

def E (x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+30,x+20,y+40)
    canvas.create_rectangle(x+10,y+60,x+20,y+70)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+30,x+40,y+40)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)

    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+60,x+50,y+70)

def F (x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+30,x+20,y+40)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)    

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+30,x+40,y+40)    

    canvas.create_rectangle(x+40,y,x+50,y+10)

def G (x,y):
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+60,x+20,y+70)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+40,x+40,y+50)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)

    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)

def H (x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y+30,x+20,y+40)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+30,y+30,x+40,y+40)

    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+30,x+50,y+40)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)
    canvas.create_rectangle(x+40,y+60,x+50,y+70)

def I (x,y):
    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+60,x+20,y+70)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+10,x+30,y+20)
    canvas.create_rectangle(x+20,y+20,x+30,y+30)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+20,y+40,x+30,y+50)
    canvas.create_rectangle(x+20,y+50,x+30,y+60)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)
 
def J (x,y):
    canvas.create_rectangle(x,y+50,x+10,y+60)
    
    canvas.create_rectangle(x+10,y+60,x+20,y+70)
    
    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+10,x+40,y+20)
    canvas.create_rectangle(x+30,y+20,x+40,y+30)
    canvas.create_rectangle(x+30,y+30,x+40,y+40)
    canvas.create_rectangle(x+30,y+40,x+40,y+50)
    canvas.create_rectangle(x+30,y+50,x+40,y+60)
   
    canvas.create_rectangle(x+40,y,x+50,y+10)

def K (x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y+30,x+20,y+40)

    canvas.create_rectangle(x+20,y+20,x+30,y+30)
    canvas.create_rectangle(x+20,y+40,x+30,y+50)

    canvas.create_rectangle(x+30,y+10,x+40,y+20)
    canvas.create_rectangle(x+30,y+50,x+40,y+60)

    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+60,x+50,y+70)

def L (x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y+60,x+20,y+70)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)
    canvas.create_rectangle(x+40,y+60,x+50,y+70)

def M(x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y+10,x+20,y+20)

    canvas.create_rectangle(x+20,y+20,x+30,y+30)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    
    canvas.create_rectangle(x+30,y+10,x+40,y+20)

    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+30,x+50,y+40)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)
    canvas.create_rectangle(x+40,y+60,x+50,y+70)

def N(x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y+20,x+20,y+30)

    canvas.create_rectangle(x+20,y+30,x+30,y+40)

    canvas.create_rectangle(x+30,y+40,x+40,y+50)

    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+30,x+50,y+40)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)
    canvas.create_rectangle(x+40,y+60,x+50,y+70)

def O(x,y):
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+60,x+20,y+70)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)

    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+30,x+50,y+40)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)

def P(x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+30,x+20,y+40)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)    

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+30,x+40,y+40)  

    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)

def R(x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+30,x+20,y+40)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)  
    canvas.create_rectangle(x+20,y+40,x+30,y+50)  

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+30,x+40,y+40) 
    canvas.create_rectangle(x+30,y+50,x+40,y+60) 

    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+60,x+50,y+70)

def S(x,y):
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+60,x+10,y+70)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+30,x+20,y+40)
    canvas.create_rectangle(x+10,y+60,x+20,y+70)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+30,x+40,y+40)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)

    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)

def T(x,y):
    canvas.create_rectangle(x,y,x+10,y+10)

    canvas.create_rectangle(x+10,y,x+20,y+10)
    
    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+10,x+30,y+20)
    canvas.create_rectangle(x+20,y+20,x+30,y+30)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+20,y+40,x+30,y+50)
    canvas.create_rectangle(x+20,y+50,x+30,y+60)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)
    
    canvas.create_rectangle(x+30,y,x+40,y+10)

    canvas.create_rectangle(x+40,y,x+50,y+10)

def U(x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)
    canvas.create_rectangle(x,y+40,x+10,y+50)
    canvas.create_rectangle(x,y+50,x+10,y+60)

    canvas.create_rectangle(x+10,y+60,x+20,y+70)
    
    canvas.create_rectangle(x+20,y+60,x+30,y+70)
    
    canvas.create_rectangle(x+30,y+60,x+40,y+70)

    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+30,x+50,y+40)
    canvas.create_rectangle(x+40,y+40,x+50,y+50)
    canvas.create_rectangle(x+40,y+50,x+50,y+60)

def V(x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x,y+20,x+10,y+30)
    canvas.create_rectangle(x,y+30,x+10,y+40)

    canvas.create_rectangle(x+10,y+40,x+20,y+50)
    canvas.create_rectangle(x+10,y+50,x+20,y+60)

    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y+40,x+40,y+50)
    canvas.create_rectangle(x+30,y+50,x+40,y+60)

    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+20,x+50,y+30)
    canvas.create_rectangle(x+40,y+30,x+50,y+40)

def Y(x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+10,x+10,y+20)

    canvas.create_rectangle(x+10,y+20,x+20,y+30)

    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+20,y+40,x+30,y+50)
    canvas.create_rectangle(x+20,y+50,x+30,y+60)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y+20,x+40,y+30)
    
    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y,x+50,y+10)

def Z(x,y):
    canvas.create_rectangle(x,y,x+10,y+10)
    canvas.create_rectangle(x,y+50,x+10,y+60)
    canvas.create_rectangle(x,y+60,x+10,y+70) 

    canvas.create_rectangle(x+10,y,x+20,y+10)
    canvas.create_rectangle(x+10,y+40,x+20,y+50)
    canvas.create_rectangle(x+10,y+60,x+20,y+70)

    canvas.create_rectangle(x+20,y,x+30,y+10)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

    canvas.create_rectangle(x+30,y,x+40,y+10)
    canvas.create_rectangle(x+30,y+20,x+40,y+30)
    canvas.create_rectangle(x+30,y+60,x+40,y+70)  

    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+40,y+60,x+50,y+70)


if name == "Bruno":
    B(10,10)
    R(70,10)
    U(130,10)
    N(190,10)
    O(250,10)
elif name == "Eva":
    E(10,10)
    V(70,10)
    A(130,10)
elif name == "David":
    D(10,10)
    A(70,10)
    V(130,10)
    I(180,10)
    D(230,10)







tkinter.mainloop()
