from tkinter import *
# -----------------Commands-----------------

def numCom7():
    display.insert(index=END, string="7")

def numCom8():
    display.insert(index=END, string="8")

def numCom9():
    display.insert(index=END, string="9")

def numComBS():
    display.delete(len(display.get())-1, END)

def numComAC():
    display.delete(0, END)

def numCom4():
    display.insert(index=END, string="4")

def numCom5():
    display.insert(index=END, string="5")

def numCom6():
    display.insert(index=END, string="6")

def numComMul():
    display.insert(index=END, string="*")

def numComDiv():
    display.insert(index=END, string="/")

def numCom1():
    display.insert(index=END, string="1")

def numCom2():
    display.insert(index=END, string="2")

def numCom3():
    display.insert(index=END, string="3")

def numComAdd():
    display.insert(index=END, string="+")

def numComSub():
    display.insert(index=END, string="-")

def numCom0():
    display.insert(index=END, string="0")

def numComDot():
    display.insert(index=END, string=".")

def numComEql():
    try:
        anzr = eval(display.get())
        display.delete(first=0, last=END)
        display.insert(index=0, string=anzr)

    except (ZeroDivisionError):
        display.delete(first=0, last=END)
        display.insert(index=0, string="MATH ERROR, Cannot devide by zero")
        
    except (SyntaxError):
        display.delete(first=0, last=END)
        display.insert(index=0, string="INVALID INPUT, Clear the screen and try again")

    except (NameError):
        display.delete(first=0, last=END)
        display.insert(index=0, string="INVALID INPUT, Clear the screen and try again")

# --------------------UI--------------------


window = Tk()
window.title("Calculator")

canvas = Canvas(width=250, height=60)
canvas.grid(row=0, column=0, columnspan=5)


# ------Entry------
display = Entry(window, justify="right", width=40)
display.place(height=10)
display.grid(row=0, column=0, columnspan=5)


# -----Buttons-----
num7 = Button(text="7", width=5, height=2, command=numCom7)
num7.grid(row=1, column=0)

num8 = Button(text="8", width=5, height=2, command=numCom8)
num8.grid(row=1, column=1)

num9 = Button(text="9", width=5, height=2, command=numCom9)
num9.grid(row=1, column=2)

numBS = Button(text="<--", width=5, height=2, command=numComBS)
numBS.grid(row=1, column=3)

numAC = Button(text="AC", width=5, height=2, command=numComAC)
numAC.grid(row=1, column=4)

num4 = Button(text="4", width=5, height=2, command=numCom4)
num4.grid(row=2, column=0)

num5 = Button(text="5", width=5, height=2, command=numCom5)
num5.grid(row=2, column=1)

num6 = Button(text="6", width=5, height=2, command=numCom6)
num6.grid(row=2, column=2)

numMul = Button(text="X", width=5, height=2, command=numComMul)
numMul.grid(row=2, column=3)

numDiv = Button(text="/", width=5, height=2, command=numComDiv)
numDiv.grid(row=2, column=4)

num1 = Button(text="1", width=5, height=2, command=numCom1)
num1.grid(row=3, column=0)

num2 = Button(text="2", width=5, height=2, command=numCom2)
num2.grid(row=3, column=1)

num3 = Button(text="3", width=5, height=2, command=numCom3)
num3.grid(row=3, column=2)

numAdd = Button(text="+", width=5, height=2, command=numComAdd)
numAdd.grid(row=3, column=3)

numSub = Button(text="-", width=5, height=2, command=numComSub)
numSub.grid(row=3, column=4)

num0 = Button(text="0", width=12, height=2, command=numCom0)
num0.grid(row=4, column=0, columnspan=2)

numDot = Button(text=".", width=5, height=2, command=numComDot)
numDot.grid(row=4, column=2)

numEql = Button(text="=", width=12, height=2, command=numComEql)
numEql.grid(row=4, column=3, columnspan=2)

name = Label(text="By: ~xcletus3", height=1)
name.grid(row=6, column=3, columnspan=2)


window.mainloop()
