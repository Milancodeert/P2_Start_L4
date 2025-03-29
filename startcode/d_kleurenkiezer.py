import tkinter
from tkinter import colorchooser


window = tkinter.Tk()
window.titel = ("kies een kleur")
window.geometry("500x350")

def open_kleurkiezer():
    kleur = colorchooser.askcolor()[1]
    if kleur:
        knop.config(bg=kleur)

knop = tkinter.Button(window, text="Kies een kleur", command=open_kleurkiezer)
knop.pack()

window.mainloop()
