import customtkinter as ctk

app = ctk.CTk()
app.geometry('500x500')
app.title('Volume Calculator')


        

def calculate():
    option = optionmenu.get()
    length1 = length.get()
    width1 = width.get()
    height1 = height.get()
    length2 = float(length1)
    width2 = float(width1)
    height2 = float(height1)
    if option == 'rectangular prism':
        answer = length2 * width2 * height2
    elif option == 'pyramid':
        answer = (length2 * width2 * height2) / 3

    label.configure(text=answer)




frame = ctk.CTkFrame(app)
frame.grid(row = 0, column = 0)

optionmenu = ctk.CTkOptionMenu(frame, values=['rectangular prism', 'pyramid'])
optionmenu.grid(row = 0, column = 0, padx = 5, pady = 5)

length = ctk.CTkEntry(frame, placeholder_text='enter the length', width=120, height=40)
length.grid(row = 1, column = 0, padx = 5, pady = 5)

width = ctk.CTkEntry(frame, placeholder_text='enter the width', width=120, height=40)
width.grid(row = 1, column = 1, padx = 5, pady = 5)

height = ctk.CTkEntry(frame, placeholder_text='enter the height', width=120, height=40)
height.grid(row = 1, column = 2, padx = 5, pady = 5)



label = ctk.CTkLabel(frame, text = '')
label.grid(row = 3, column = 0, padx = 5, pady = 5)

btn = ctk.CTkButton(frame, text = 'calculate', command = calculate)
btn.grid(row = 4, column = 0, padx = 5, pady = 5)

app.mainloop()
