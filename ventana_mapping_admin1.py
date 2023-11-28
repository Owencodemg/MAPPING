import tkinter as tk

class VentanaMappingAdmin:
    def __init__(self, root):
        self.root = root

    def crear_ventana_admin(self):
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Ventana de Administrador")
        admin_window.geometry("400x300")

        label = tk.Label(admin_window, text="¡Bienvenido, Administrador!")
        label.pack(pady=20)

        admin_window.mainloop()
