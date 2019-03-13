import tkinter
 
window = tkinter.Tk()
window.wm_title("Bin / Oct / Dec / Hex")
base_number = ""

def evaluate(event):
    if base_number == "Binary":
        try:
            dec = int(Myentry.get(), 2)
            myhex = hex(dec)
            myoct = oct(dec)
            result1.configure(text="Decimal is: " + str(dec))
            result2.configure(text="Hex is: " + str.upper(myhex))
            result3.configure(text="Octal is: "+ str(myoct))
        except ValueError:
            result1.configure(text="Please enter valid binary")
            result2.configure(text="")
            result3.configure(text="")

    elif base_number == "Decimal":
            try:
                dec = int(Myentry.get(), 10)
                mybin = bin(dec)
                myhex = hex(dec)
                myoct = oct(dec)
                result1.configure(text = "Binary is: "+str(mybin))
                result2.configure(text = "Hex is: "+str.upper(myhex))
                result3.configure(text = "Octal is: "+str(myoct))
            except ValueError:
                result1.configure(text = "Please enter valid decimal")
                result2.configure(text = "")
                result3.configure(text = "")

    elif base_number == "Octal":
        try:
            dec = int(Myentry.get(), 8)
            mybin = bin(dec)
            myhex = hex(dec)
            myoct = oct(dec)
            result1.configure(text ="Decimal is: "+str(dec))
            result2.configure(text ="Binary is: "+str(mybin))
            result3.configure(text ="Hexadecimal is"+str.upper(myhex))
        except ValueError:
            result1.configure(text ="Please senter valid octal number")
            result2.configure(text ="")
            result3.configure(text ="")

    elif base_number == "Hex":
        try:
            dec =int(Myentry.get(), 16)
            mybin = bin(dec)
            myoct = oct(dec)
            myhex = hex(dec)
            result1.configure(text = "Decimal is: "+str(dec))
            result2.configure(text = "Binary is: "+str(mybin))
            result3.configure(text="Octal is: "+str(myoct))
        except ValueError:
            result1.configure(text = "Please enter valid hexadecimal")
            result2.configure(text = "")
            result3.configure(text = "")

    else:
        result1.configure(text = "Please select a BASE!")


def calcStyle():
    global base_number
    base_number = base.get()
    print(base.get())


MyTitle = tkinter.Label(window, text="Decimal (10) / Binary (2) / Octal (8) / Hexadecimal (16) / ")
MyTitle.pack()
 
Myentry = tkinter.Entry(window)
Myentry.bind("<Return>", evaluate)
Myentry.pack()
 
result1 = tkinter.Label(window, text="1. Choose a base")
result1.pack()
 
result2 = tkinter.Label(window, text="2. Enter a number and press<enter>")
result2.pack()

result3 = tkinter.Label(window, text="3. Oct")
result3.pack()
 
base = tkinter.StringVar()
tkinter.Radiobutton(window, text="Binary", variable=base, value="Binary", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Decimal", variable=base, value="Decimal", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Hex", variable=base, value="Hex", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Octal", variable=base, value="Octal", command=calcStyle).pack()
 
window.mainloop()