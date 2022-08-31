from msilib.schema import Font
import string
from tkinter import *
from turtle import color
from tkinter import font

expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	valeur.set(expression)

def clear1() :
    global expression
    expression = expression[0:(len(expression)-1)]
    valeur.set(expression)

def clear() :
    global expression
    expression = ""
    valeur.set(expression)
def eqaul() :
    try : 
        global expression
        total = str(eval(expression))
        valeur.set(total)
        expression = ""
    except Exception :
        valeur.set("Ereurr")

fenetre = Tk() 
fenetre.geometry("400x400")
fenetre.title("Calculatrice")
fenetre.resizable(False,False) 

valeur = StringVar()

fn = font.Font(size=20 )

screen1 = Entry(fenetre , textvariable=valeur, foreground="white" , width=400 , bg="#000E18" ,font=fn)

bouton_0 = Button(text="0", relief=SOLID,width=36 , bg="#000",foreground="#fff" , command=lambda : press(0)) 
bouton_1 = Button(text="1", relief=SOLID,width=11, bg="#000",foreground="#fff", command=lambda : press(1)) 
bouton_2 = Button(text="2", relief=SOLID,width=13, bg="#000",foreground="#fff", command=lambda : press(2)) 
bouton_3 = Button(text="3", relief=SOLID,width=11, bg="#000",foreground="#fff", command=lambda : press(3)) 
bouton_4 = Button(text="4", relief=SOLID,width=11, bg="#000",foreground="#fff", command=lambda : press(4)) 
bouton_5 = Button(text="5", relief=SOLID,width=13, bg="#000",foreground="#fff", command=lambda : press(5)) 
bouton_6 = Button(text="6", relief=SOLID,width=11, bg="#000",foreground="#fff", command=lambda : press(6)) 
bouton_7 = Button(text="7", relief=SOLID,width=11, bg="#000",foreground="#fff", command=lambda : press(7)) 
bouton_8 = Button(text="8", relief=SOLID,width=13, bg="#000",foreground="#fff", command=lambda : press(8)) 
bouton_9 = Button(text="9", relief=SOLID,width=11, bg="#000",foreground="#fff", command=lambda : press(9)) 
bouton_plus = Button(text="+", relief=SOLID,width=19, bg="#000",foreground="#fff", command=lambda : press("+")) 
bouton_sub = Button(text="-", relief=SOLID,width=19, bg="#000",foreground="#fff", command=lambda : press("-")) 
bouton_div = Button(text="/", relief=SOLID,width=19, bg="#000",foreground="#fff", command=lambda : press("/")) 
bouton_multi = Button(text="*", relief=SOLID,width=19, bg="#000",foreground="#fff", command=lambda : press("*")) 
bouton_clear = Button(text="C", relief=SOLID , width=26, bg="red",foreground="#fff",command=lambda :clear()) 
bouton_clear1 = Button(text="x", relief=SOLID , width=11, bg="red",foreground="#fff",command=lambda :clear1()) 
bouton_egal = Button(text="=", relief=SOLID ,width=19, bg="red",foreground="#fff",command=lambda:eqaul()) 

screen1.place(x=0 ,y=0 ,height=110) 
bouton_clear.place(x=0 , y=101 ,height=60) 
bouton_clear1.place(x=175 , y=101 ,height=60) 
bouton_0.place(x=0 , y=341 ,height=60) 
bouton_egal.place(x=262 , y=341 ,height=60) 
bouton_sub.place(x=262 , y=221 ,height=60) 
bouton_multi.place(x=262 , y=161 ,height=60) 
bouton_plus.place(x=262 , y=281 ,height=60) 
bouton_div.place(x=262 , y=101 ,height=60) 
bouton_1.place(x=0 , y=281 , height=60)
bouton_2.place(x=87 , y=281 , height=60)
bouton_3.place(x=175 , y=281 , height=60)
bouton_4.place(x=0 , y=221 , height=60)
bouton_5.place(x=87 , y=221 , height=60)
bouton_6.place(x=175 , y=221 , height=60)
bouton_7.place(x=0 , y=161 , height=60)
bouton_8.place(x=87 , y=161 , height=60)
bouton_9.place(x=175 , y=161 , height=60)
fenetre.mainloop()