import tkinter as tk
from tkinter import messagebox
from firebase_admin import db, credentials, initialize_app

class AplicacionBusquedaSalas:
    def __init__(self, parent, admin_salones, usuario_actual):
        self.parent = parent
        self.admin_salones = admin_salones
        self.usuario_actual = usuario_actual
        self.current_route_index = None

        self.entrada1 = tk.Entry(parent, width=40, fg="black", font=('Helvetica', 12))
        self.entrada1.place(x=904, y=230)

        self.boton_buscar = tk.Button(parent, width=50, height=2, text="Buscar", command=self.get_images, bg="#222feb", fg="white", border=0)
        self.boton_buscar.place(x=910, y=380) 

    def get_images(self):
        route_name = self.entrada1.get()
        
        if route_name in self.admin_salones.values():
            self.current_route_index = list(self.admin_salones.values()).index(route_name)
            self.show_images_window()
        else:
            tk.messagebox.showerror("Error", "Nombre de sala no encontrado.")

    def show_images_window(self):
        images_window = tk.Toplevel(self.parent)
        images_window.title("Imágenes de Ruta")
        images_window.geometry("810x650")
        images_window.resizable(False, False)
        # Aquí puedes cargar las imágenes relacionadas con la ruta actual.

if __name__ == "__main__":
    # Configuración de Firebase

    firebase_sdk2 = credentials.Certificate("mapping-1a38f-firebase-adminsdk-8nf6d-117e271815.json")
    initialize_app(firebase_sdk2, {"databaseURL": "https://mapping-1a38f-default-rtdb.firebaseio.com/"})
    # Obtener la referencia de la base de datos
    admin_salones = db.reference("/Salones")
    
    root = tk.Tk()
    usuario_actual = "nombre_usuario"
    app = AplicacionBusquedaSalas(root, admin_salones, usuario_actual)
    root.mainloop()
