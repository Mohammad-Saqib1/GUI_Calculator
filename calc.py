from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.configure(background='brown')

root.title("Calculator By Mohammad Saqib")
root.geometry('400x700')
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold",
               relief=SUNKEN, bg='cyan', borderwidth=5)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg='grey')
for i in range(7, 10):
    b = Button(f, text=str(i), padx=28, pady=18,
               font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg='grey')
for i in range(4, 7):
    b = Button(f, text=str(i), padx=28, pady=18,
               font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg='grey')
for i in range(1, 4):
    b = Button(f, text=str(i), padx=28, pady=18,
               font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg='grey')
b = Button(f, text="0", padx=26, pady=18,
           font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=4)
b.pack(side=LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=26, pady=18,
           font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=4)
b.pack(side=LEFT, ipadx=2,padx=18, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=26, pady=18,
           font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
b.pack(side=LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)
f.pack()
f = Frame(root, bg='grey')
b = Button(f, text="-", padx=28, pady=18,
           font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
b.pack(side=LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=28, pady=18,
           font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
b.pack(side=LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=28, pady=18,
           font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
b.pack(side=LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg='grey')
b = Button(f, text="/", padx=28, pady=18,
           font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
b.pack(side=LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=28, pady=18,
           font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
b.pack(side=LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=28, pady=18,
           font="lucida 15 bold", relief=SUNKEN, bg='violet',borderwidth=5)
b.pack(side=LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg='grey')
b = Button(f, text="C", padx=38, pady=35,
           font="lucida 15 bold", relief=SUNKEN, bg='red',borderwidth=5)
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()
