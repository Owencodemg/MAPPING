import tkinter as tk
import firebase_admin
from firebase_admin import db, credentials
from tkinter import messagebox

from PIL import Image, ImageTk

class VentanaSeguridad2:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Ventana de Seguridad")
        self.ventana.geometry("300x300")
        self.ventana.configure(bg="#fff")
        self.ventana.resizable(0,0)




        self.etiqueta_espacio= tk.Label(self.ventana, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=32, y=100)

        self.etiqueta_espacio= tk.Label(self.ventana, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=32, y=173)



        self.user = self.create_entry("Nombre De Usuario", x=32, y=88)
        self.code = self.create_entry("Contraseña", x=32, y=160)



        self.boton_actualizar1 = tk.Button(self.ventana, text="COMPROBAR", command=self.comprobar, width=20, height=2, bg="#222feb", fg="white", border=0)
        self.boton_actualizar1.place(x=80, y=210)


    def comprobar(self):
        self.nombre_usuario1 = self.user.get()
        self.contraseña1 = self.code.get()

        usuarios_ref = db.reference("/Registrados/Profesores/")
        usuarios_snapshot = usuarios_ref.get()

        usuario_encontrado = None
        for usuario_id, usuario_data in usuarios_snapshot.items():
            if usuario_data.get('Usuario') == self.nombre_usuario1:
                usuario_encontrado = usuario_data

                if usuario_encontrado:
                    if usuario_encontrado.get('Contraseña') == self.contraseña1:
                        messagebox.showinfo("Éxito", "Ya puedes actualizar")
                        self.abrir(self.ventana)
                    else:
                        messagebox.showwarning("Error", "Contraseña incorrecta")
                if not usuario_encontrado:
                    messagebox.showwarning("Error", "Usuario no encontrado en la base de datos")




    def abrir(self,root):

        self.root = root
        self.root.title("Ventana de Actualización")
        self.root.geometry("425x680")
        self.root.configure(bg="#fff")

        self.root.resizable(False, False)

        self.image_path = 'celu22.png'
        self.img = self.load_thumbnail(self.image_path, (800, 800))
        self.label_img = tk.Label(self.root, image=self.img, bg="#fff")
        self.label_img.place(x=0, y=0)


        etiqueta_ = tk.Label(root, text=f"                                    ", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_.place(x=30,y=50)

        #espacios en blanco para tapar
        self.etiqueta_espacio= tk.Label(self.root, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=270)
        self.etiqueta_espacio= tk.Label(self.root, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=290)
        self.etiqueta_espacio= tk.Label(self.root, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=370)

        self.etiqueta_espacio= tk.Label(self.root, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=40, y=350)
        self.etiqueta_espacio= tk.Label(self.root, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=360)
        self.etiqueta_espacio= tk.Label(self.root, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=430)
        self.etiqueta_espacio= tk.Label(self.root, text="                                                                               ",bg="white")
        self.etiqueta_espacio.place(x=82, y=480)
        self.etiqueta_espacio= tk.Label(self.root, text="                                                                                ",bg="white")
        self.etiqueta_espacio.place(x=82, y=470)

        #guiones para debajo

        self.label_inicio2 = tk.Label(self.root, text="                                                                                                  ", fg="black", bg="black", font=("times", 30, "bold"))
        self.label_inicio2.place(x=2, y=650)
        self.label_inicio2 = tk.Label(self.root, text="                                                                                                  ", fg="black", bg="black", font=("times", 17, "bold"))
        self.label_inicio2.place(x=2, y=0)
        self.etiqueta_espacio= tk.Label(self.root, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=82, y=320)

        self.etiqueta_espacio= tk.Label(self.root, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=82, y=393)
        self.etiqueta_espacio= tk.Label(self.root, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=82, y=453)
        self.etiqueta_espacio= tk.Label(self.root, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=82, y=513)


        self.user1 = self.create_entry("Nombre De Usuario", x=82, y=308)
        self.code_id = self.create_entry("ID",x=82 , y=380)
        self.code1 = self.create_entry("Contraseña", x=82, y=440)
        self.code_confirm = self.create_entry("Confirmar Contraseña", x=82, y=500)









        boton_guardar = tk.Button(self.root, width=18, pady=20, text="ACTUALIZAR", bg="#222feb", fg="white", border=0, command=self.guardar_informacion)
        boton_guardar.place(x=150,y=560)




    def guardar_informacion(self):        
        usuarios_ref = db.reference("/Registrados/Profesores/")
        usuarios_snapshot = usuarios_ref.get()
        for usuario_id, usuario_data in usuarios_snapshot.items():
            if usuario_data.get('Usuario') == self.nombre_usuario1 and usuario_data.get('Contraseña') == self.contraseña1:
                nuevos_datos = {
                    "Usuario": self.user1.get(), "Contraseña": self.code1.get(), }
                usuarios_ref.child(usuario_id).update(nuevos_datos)
                messagebox.showinfo("Éxito", "Información actualizada exitosamente")


    def create_entry(self, default_text, x, y):
        entry = tk.Entry(self.root, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 15)) 
        entry.place(x=x, y=y)
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', lambda event, widget=entry, text=default_text: self.on_enter(event, widget, text))
        entry.bind('<FocusOut>', lambda event, widget=entry, text=default_text: self.on_leave(event, widget, text))

        return entry

    def on_enter(self, event, entry_widget, default_text):
        entry_widget.delete(0, 'end')

    def on_leave(self, event, entry_widget, default_text):
        name = entry_widget.get()
        if name == '':
            entry_widget.insert(0, default_text)

        # Agrega los elementos de la ventana aquí







    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Maintain a reference to the image








    def create_entry(self, default_text, x, y):
        entry = tk.Entry(self.ventana, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 15)) 
        entry.place(x=x, y=y)
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', lambda event, widget=entry, text=default_text: self.on_enter(event, widget, text))
        entry.bind('<FocusOut>', lambda event, widget=entry, text=default_text: self.on_leave(event, widget, text))

        return entry

    def on_enter(self, event, entry_widget, default_text):
        entry_widget.delete(0, 'end')

    def on_leave(self, event, entry_widget, default_text):
        name = entry_widget.get()
        if name == '':
            entry_widget.insert(0, default_text)


if __name__ == "__main__":
    firebase_sdk = credentials.Certificate("mapping-1a38f-firebase-adminsdk-8nf6d-117e271815.json")
    firebase_admin.initialize_app(firebase_sdk, {"databaseURL": "https://mapping-1a38f-default-rtdb.firebaseio.com/"})


