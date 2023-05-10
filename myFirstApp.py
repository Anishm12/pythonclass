import customtkinter as ctk

app = ctk.CTk()
app.geometry('500x300')
app.title('My First App')

def enter_clicked():
    name = nameEntry.get()
    address = addressEntry.get()
    age = ageEntry.get()
    list = [name, address, age]
    list2 = '\n'.join(list)
    label.configure(text=list2)
nameLabel = ctk.CTkLabel(app, text='Name: ')
nameLabel.grid(row=0, column=0)

nameEntry = ctk.CTkEntry(app, placeholder_text='Enter your name: ')
nameEntry.grid(row = 0, column = 1)

addressLabel = ctk.CTkLabel(app, text='Address: ')
addressLabel.grid(row=1, column=0)

addressEntry = ctk.CTkEntry(app, placeholder_text='Enter your address: ')
addressEntry.grid(row = 1, column = 1)

enterButton = ctk.CTkButton(app, text = 'Enter', command=enter_clicked)
enterButton.grid(row = 3, column = 1)

Agelabel = ctk.CTkLabel(app, text='Age: ')
Agelabel.grid(row=2, column=0)

ageEntry = ctk.CTkEntry(app, placeholder_text='Enter your age: ')
ageEntry.grid(row = 2, column = 1)

label = ctk.CTkLabel(app, text = '')
label.grid(row = 4, column = 1)

app.mainloop()