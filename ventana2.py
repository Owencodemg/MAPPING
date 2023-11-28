import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import firebase_admin
from ventana3 import obtener_admin_salones
from ventana3_estudiantes import AplicacionBusquedaSalas2
from ventana3 import AplicacionBusquedaSalas
from firebase_admin import credentials, db

class Ventana2:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana 2")
        self.master.geometry("425x680")
        self.master.configure(bg="#fff")
        
        self.master.resizable(False, False)

        self.image_path = 'celu22.png'
        self.img = self.load_thumbnail(self.image_path, (800, 800))
        self.label_img = tk.Label(self.master, image=self.img, bg="#fff")
        self.label_img.place(x=0, y=0)

        #espacios en blanco para tapar

        etiqueta_47 = tk.Label(master, text=f"                                    ", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_47.place(x=30,y=50)

        self.etiqueta_espacio= tk.Label(self.master, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=270)
        self.etiqueta_espacio= tk.Label(self.master, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=290)
        self.etiqueta_espacio= tk.Label(self.master, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=370)
        
        self.etiqueta_espacio= tk.Label(self.master, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=40, y=350)
        self.etiqueta_espacio= tk.Label(self.master, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=360)
        self.etiqueta_espacio= tk.Label(self.master, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=430)
        self.etiqueta_espacio= tk.Label(self.master, text="                                                                               ",bg="white")
        self.etiqueta_espacio.place(x=82, y=480)
        self.etiqueta_espacio= tk.Label(self.master, text="                                                                                ",bg="white")
        self.etiqueta_espacio.place(x=82, y=470)

        #guiones para debajo
        
        self.label_inicio2 = tk.Label(self.master, text="                                                                                                  ", fg="black", bg="black", font=("times", 30, "bold"))
        self.label_inicio2.place(x=2, y=650)
        self.label_inicio2 = tk.Label(self.master, text="                                                                                                  ", fg="black", bg="black", font=("times", 17, "bold"))
        self.label_inicio2.place(x=2, y=0)
        self.etiqueta_espacio= tk.Label(self.master, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=82, y=320)

        self.etiqueta_espacio= tk.Label(self.master, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=82, y=393)
        self.etiqueta_espacio= tk.Label(self.master, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=82, y=453)
        self.etiqueta_espacio= tk.Label(self.master, text="_________________________________________________",bg="black")
        self.etiqueta_espacio.place(x=82, y=513)


        self.user = self.create_entry("Nombre De Usuario", x=82, y=308)
        self.code_id = self.create_entry("ID",x=82 , y=380)
        self.code = self.create_entry("Contraseña", x=82, y=440)
        self.code_confirm = self.create_entry("Confirmar Contraseña", x=82, y=500)

  
        tk.Button(self.master, width=18, pady=20, text="REGISTRAR", bg="#222feb", fg="white", border=0, command=self.login).place(x=150,y=560)

        

        # self.open_third_button = ttk.Button(self.master, text="Abrir Tercera Ventana", command=self.open_third_window)
        # self.open_third_button.pack()

    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Mantén una referencia a la imagen

    def open_third_window(self):
        self.master.withdraw()
        third_window = tk.Toplevel()
        admin_salones = obtener_admin_salones()  # Obtén la instancia admin_salones
        usuario_actual = "nombre_usuario"  # Reemplaza con el usuario actual
        app = AplicacionBusquedaSalas(third_window, admin_salones, usuario_actual)
        third_window.mainloop()
    def open_third_window2(self):
        self.master.withdraw()
        third_window = tk.Toplevel()
        admin_salones = obtener_admin_salones()  # Obtén la instancia admin_salones
        usuario_actual = "nombre_usuario"  # Reemplaza con el usuario actual
        app = AplicacionBusquedaSalas2(third_window, admin_salones, usuario_actual)
        third_window.mainloop()



    def create_entry(self, default_text, x, y):
        entry = tk.Entry(self.master, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 15)) 
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

    def login(self):

        nombre_usuario = self.user.get()
        user_id = self.code_id.get()
        contraseña = self.code.get()
        confirm_password = self.code_confirm.get()

        if not nombre_usuario or not user_id or not contraseña or not confirm_password:
            messagebox.showwarning("Advertencia", "Por favor, llena todos los campos.")
        elif not user_id.isdigit():
            messagebox.showwarning("Advertencia", "El ID solo debe contener números.")
        elif contraseña != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
        else:
            if contraseña == "mappingprofesores":  # Verifica si la contraseña es igual a "mappingprofesores"
                ref = db.reference("/Registrados/Profesores/")
                ref.push({"Usuario": nombre_usuario, "Contraseña": contraseña})
                messagebox.showinfo("Éxito", "¡Registro exitoso como profesor!")
                self.open_third_window()

            else:
                ref = db.reference("/Registrados/Estudiantes/")
                ref.push({"Usuario": nombre_usuario, "Contraseña": contraseña})
                messagebox.showinfo("Éxito", "¡Registro exitoso como estudiante!")
   
            self.open_third_window2()

            self.master.destroy()


if __name__ == "__main__":
    firebase_sdk2 = credentials.Certificate("mapping-1a38f-firebase-adminsdk-8nf6d-117e271815.json")
    default_app2 = firebase_admin.initialize_app(firebase_sdk2, {"databaseURL": "https://mapping-1a38f-default-rtdb.firebaseio.com/"})
    root = tk.Tk()
    app = Ventana2(root)
    root.mainloop()