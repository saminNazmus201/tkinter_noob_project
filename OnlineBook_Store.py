
from tkinter import *
import webbrowser
from tkinter import messagebox as mb
root=Tk()
root.geometry("300x350")
root.config(bg="#E26161")
email_var=StringVar()
user_name_var= StringVar()
passw=StringVar()

def show():

    email=email_var.get()
    name=user_name_var.get()
    password=passw.get()
    print("his email is " +email)
    print("his name is " +name)
    email_var.set("")
    user_name_var.set("")

    passw.set("")

    top1 = Toplevel()
    top1.geometry("750x750")
    top1.config(bg="#F5D0D0")
    lebel5=Label(top1, text=f"Welcome Mr. {name}",font="Roboto 20 bold",bg="pink",fg="black").place(x=5,y=20)
    menubar=Menu(top1)
    file=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Book Fair",menu=file)
    file.add_command(label="BookFair2022")
    file.add_command(label="BookFair2021")
    author = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Author", menu=author)
    author.add_command(label="Bangladesh")
    author.add_command(label="West Bengal")
    offer=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="OFFER",menu=offer)
    offer.add_command(label="Blck Friday!!")
    offer.add_command(label="OLD BOOK")
    entry4=Entry(top1).place(x=580,y=0)
    btn2=Button(top1, text="Search").place(x=700,y=0)
    top1.config(menu=menubar)
    canvas1=Canvas(top1,width=650, height=200)
    canvas1.place(x=35,y=60)
    img=PhotoImage(file=r"C:\Users\HP\Downloads\book3.ppm")
    canvas1.create_image(0,0,image=img,anchor=NW)
    def callback2():
        top2=Toplevel()
        top2.geometry("750x750")
        label5=Label(top2,text="Best selling books", font="Roboto 20 bold").place(x=10,y=0)
        def yesnoques():
            res = mb.askquestion('question',
                                 'Do you really want to buy it')

            if res == 'yes':
                mb.showinfo('Return', 'Thanks for buying')

            else:
                top2.destroy()

        top2label1 =Label(top2, text="Sapiens", font="Roboto 14 bold",cursor="hand1")
        top2label1.place(x=10, y=55)
        top2label2 =Label(top2, text="Murder on the orient Express", font="Roboto 14 bold").place(x=10, y=85)
        top2label1.bind("<Button-1>", lambda e: yesnoques())
    def callback3():
        top3=Toplevel()
        top3.geometry("750x750")
        label6=Label(top3,text="HORROR books", font="Roboto 20 bold").place(x=10,y=0)
        top2label1 = Label(top3, text="Death", font="Roboto 14 bold", cursor="hand1")
        top2label1.place(x=10, y=55)
        top2label2 = Label(top3, text="Murder by the sea", font="Roboto 14 bold").place(x=10, y=85)
    def callback4():
        top4=Toplevel()
        top4.geometry("750x750")
        label7=Label(top4,text="HISTORY books", font="Roboto 20 bold").place(x=10,y=0)
        top2label1 = Label(top4, text="Habit", font="Roboto 14 bold", cursor="hand1")
        top2label1.place(x=10, y=55)
        top2label2 = Label(top4, text="Done and Dusted", font="Roboto 14 bold").place(x=10, y=85)
    def callback5():
        top5=Toplevel()
        top5.geometry("750x750")
        label8=Label(top5,text="CHILDREEN Books", font="Roboto 20 bold").place(x=10,y=0)
        top2label1 = Label(top5, text="Spider Man", font="Roboto 14 bold", cursor="hand1")
        top2label1.place(x=10, y=55)
        top2label2 = Label(top5, text="Mr. Bean", font="Roboto 14 bold").place(x=10, y=85)
    btn3=Button(top1,text="Best Selling books", font="Roboto 16 bold",cursor="hand2",command=callback2).place(x=55, y= 350)
    btn4=Button(top1,text="Horror books", font="Roboto 16 bold",cursor="hand2",command=callback3).place(x=55, y= 425)
    btn5 = Button(top1, text=" History books", font="Roboto 16 bold",cursor="hand2",command=callback4).place(x=375, y=350)
    btn6 = Button(top1, text="Children zone", font="Roboto 16 bold",cursor="hand2",command=callback5).place(x=375, y=425)
    canvas2=Canvas(top1, width=100, height=100,cursor="hand2")
    canvas2.place(x=55,y=490)
    img2=PhotoImage(file=r"C:\Users\HP\Downloads\omerta.ppm")
    canvas2.create_image(0,0, image=img2,anchor=NW)
    def callback():
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Omert%C3%A0")
    canvas2.bind("<Button-1>", lambda e: callback())
    canvas3 = Canvas(top1, width=100, height=100,cursor="hand2")
    canvas3.place(x=190, y=490)
    canvas3.create_image(0,0,image=img2, anchor=NW)
    canvas3.bind("<Button-1>",lambda e:callback())
    canvas4 = Canvas(top1, width=100, height=100,cursor="hand2")
    canvas4.place(x=330, y=490)
    canvas4.create_image(0,0,image=img2, anchor=NW)
    canvas4.bind("<Button-1>", lambda e: callback())
    canvas5 = Canvas(top1, width=100, height=100,cursor="hand2")
    canvas5.place(x=470, y=490)
    canvas5.create_image(0, 0, image=img2, anchor=NW)
    canvas5.bind("<Button-1>", lambda e: callback())

    top1.mainloop()

label1=Label(root, text="LOGIN FIRST", bg="#291C1C",fg="#F1E5E5",font="Roboto 16 bold").pack()
label2=Label(root, text="Email :", bg="#291C1C",fg="#F1E5E5").place(x=40, y=100)
label3=Label(root, text="Password :", bg="#291C1C",fg="#F1E5E5").place(x=40,y=140)
label4=Label(root, text="User Name :", bg="#291C1C",fg="#F1E5E5").place(x=40, y=180)
entry1=Entry(root,textvariable=email_var).place(x=83,y=100)
entry2=Entry(root,show="*",textvariable=passw).place(x=105,y=140)
entry3=Entry(root,textvariable=user_name_var).place(x=112,y=180)
btn1=Button(root, text="LOG IN", bg="#291C1C",fg="#F1E5E5",command=show).place(x=120,y=250)


root.mainloop()