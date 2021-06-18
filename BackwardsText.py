#run in terminal: python3 BackwardsText.py
from tkinter import *

root = Tk()
root.title("BackwardsText")
root.geometry("420x150")

entre = Entry(root, width = 50)
outcome = Entry(root, width = 50)
text = Label(root, text = "Text to drawkcaB, Backward ot txeT")

text.place(relx = 0.5, rely = 0.05, anchor = "center")
entre.place(relx = 0.5, rely = 0.25, anchor = "center")
outcome.place(relx = 0.5, rely = 0.67, anchor = "center")

def con():
    outcome.delete(0, END)
    tran = entre.get()
    num = 0

    for letter in tran:
        outcome.insert(0, tran[num])
        num += 1

convert = Button(root, text = "Convert", command = lambda: con())
convert.place(relx = 0.5, rely = 0.45, anchor = "center")

root.mainloop()