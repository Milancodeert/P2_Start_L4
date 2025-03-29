from tkinter import messagebox

titels = ["1", "2", ";)", "4", "5" ]
messages = ["1", "2", ":o", "4",  "5"]
for i in range(len(messages)):
    messagebox.showinfo(titels[i], messages[i])