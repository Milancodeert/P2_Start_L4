import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.titel = ("messagebox")
window.geometry("100x50")

def open_messagebox():
    titel_messagebox = "coole messagebox :)"
    bijtext_messagebox = "stukje tekst"
    messagebox.showinfo(titel_messagebox, bijtext_messagebox)

buttonDitIsKnop = tkinter.Button(window, text="Dit is een knop ;)",  command=open_messagebox)
buttonDitIsKnop.pack()


window.mainloop()