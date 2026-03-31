import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Mode dark
ctk.set_default_color_theme("dark-blue")  # Teme

app = ctk.CTk()
app.title("Tela Moderna")
app.geometry("600x300")

label = ctk.CTkLabel(app, text="Interface Moderna")
label.pack(pady=20)

button = ctk.CTkButton(app, text="Clique")
button.pack()

app.mainloop()
