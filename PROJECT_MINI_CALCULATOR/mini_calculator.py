#import everything from tkinter
from tkinter import *

app = Tk()
app.title("Mini  Calculator") #Title 
app.geometry("300x400")   #window size 

display = Entry(app, font=("Arial", 20, "bold"), justify=RIGHT)              
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew") 

def press(val):
    display.insert(END, val)

def reset():
    display.delete(0, END)

def solve():
    try:
        ans = eval(display.get())
        display.delete(0, END)
        display.insert(END, ans)
    except:
        display.delete(0, END)
        display.insert(END, "Err")



#keys = ("button",row,column")
keys = [
    ("9",1,0), ("8",1,1), ("7",1,2), ("/",1,3),
    ("6",2,0), ("5",2,1), ("4",2,2), ("*",2,3),
    ("3",3,0), ("2",3,1), ("1",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
]

for k, r, c in keys:
    Button(
        app,
        text=k,
        font=("Arial", 14, "bold"),
        command=solve if k == "=" else lambda x=k: press(x)
    ).grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

Button(
    app,
    text="CLR",
    font=("Arial", 14, "bold"),
    command=reset
).grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

for i in range(6):
    app.rowconfigure(i, weight=1)

for j in range(4):
    app.columnconfigure(j, weight=1)

app.mainloop()
