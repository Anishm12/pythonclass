import customtkinter as ctk

app = ctk.CTk()
app.geometry('500x500')
app.title('Volume Calculator')

frame = ctk.CTkFrame(app)
frame.grid(row = 0, column = 0)



length = ctk.CTkEntry(frame, placeholder_text='enter the length', width=120, height=40)
length.grid(row = 0, column = 0, padx = 5, pady = 5)



app.mainloop()