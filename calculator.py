from tkinter import *

root = Tk()
root.geometry("285x290")
root.title("simple calculator using gui")



def click(num):
    
    field.insert(END, str(num))


def result():
    try:
       
        show=field.get("1.0","end-1c")
        total = str(eval(show))
        field.delete("1.0", END)
        field.insert(END, total)

        

    except:
        field.delete("1.0", END)
        field.insert(END, "error")
        


def clear():
   

    field.delete("1.0", END)
    


def backslash():
    present = field.get("1.0", "end-1c")
    newshow = present[:-1]
    field.delete("1.0", END)
    field.insert(END, newshow)


field = Text(root, width=32, height=2)

btn7 = Button(root, text="7", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("7")).place(x=0, y=45)
btn8 = Button(root, text="8", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("8")).place(x=80, y=45)
btn9 = Button(root, text="9", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("9")).place(x=160, y=45)
btn4 = Button(root, text="4", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("4")).place(x=0, y=90)
btn5 = Button(root, text="5", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("5")).place(x=80, y=90)
btn6 = Button(root, text="6", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("6")).place(x=160, y=90)
btn1 = Button(root, text="1", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("1")).place(x=0, y=135)
btn2 = Button(root, text="2", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("2")).place(x=80, y=135)
btn3 = Button(root, text="3", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("3")).place(x=160, y=135)
btn0 = Button(root, text="0", bg="light blue", foreground="white", width=10, height=1,
              command=lambda: click("0")).place(x=0, y=180)
btnplus = Button(root, text="+", bg="light blue", foreground="white", width=10, height=1,
                 command=lambda: click("+")).place(x=80, y=180)
btnminus = Button(root, text="-", bg="light blue", foreground="white", width=10, height=1,
                  command=lambda: click("-")).place(x=160, y=180)
btnmul = Button(root, text="X", bg="light blue", foreground="white", width=10, height=1,
                command=lambda: click("*")).place(x=0, y=225)
btndiv = Button(root, text="/", bg="light blue", foreground="white", width=10, height=1,
                command=lambda: click("/")).place(x=80, y=225)
btnequal = Button(root, text="=", bg="light blue", foreground="white", width=10, height=1, command=result).place(x=160,
                                                                                                                 y=225)
btnclear = Button(root, text="AC", bg="light blue", foreground="white", width=10, height=1, command=clear).place(x=0,
                                                                                                                 y=260)
btnback = Button(root, text="<-", bg="light blue", foreground="white", width=10, height=1, command=backslash).place(
    x=80, y=260)

field.place(x=0, y=0)
root.mainloop()
