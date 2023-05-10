import customtkinter as ctk
import random

app = ctk.CTk()
app.geometry('500x500')
app.title('Rock Paper Scissors')

computer = random.choice['r', 'p', 's']

label = ctk.CTkLabel(app, text='Enter rock, paper or scissors')
label.grid(row = 0, column = 0)

entry = ctk.CTkEntry(app)
entry.grid(row = 0, column = 1, padx = 2, pady = 2)

btn = ctk.CTkButton(app, text='go')
btn.grid(row = 0, column = 2, padx = 2, pady = 2)



app.mainloop()