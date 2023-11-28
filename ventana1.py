from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
import ventana2  # Importa el archivo de la segunda ventana
from ventana3 import obtener_admin_salones
from ventana3 import AplicacionBusquedaSalas
from ventana3_estudiantes import AplicacionBusquedaSalas2  



import firebase_admin
from firebase_admin import credentials, db
from ventana_admin import VentanaAdmin  
from tkinter import ttk, messagebox
# from ventana_mapping_admin1 import VentanaMappingAdmin


firebase_sdk = credentials.Certificate("mapping-1a38f-firebase-adminsdk-8nf6d-117e271815.json")
firebase_admin.initialize_app(firebase_sdk, {"databaseURL": "https://mapping-1a38f-default-rtdb.firebaseio.com/"})





class Ventana1:

    def __init__(self, master):
        self.master = master
        self.master.title("Ventana 1")
        self.master.attributes('-fullscreen', True)

        self.master.configure(bg="#fff")
        self.image_path = 'loginl.png'
        self.img = self.load_thumbnail(self.image_path, (700, 800))
        self.label_img = Label(self.master, image=self.img, bg="#fff")
        self.label_img.place(x=700, y=50)

        self.image_path2 = 'bienvenida1.png'
        self.img2 = self.load_thumbnail(self.image_path2, (600, 600))
        self.label_img2 = Label(self.master, image=self.img2, bg="#fff")
        self.label_img2.place(x=100, y=75)

        image2 = Image.open("web_link.png")
        image2.thumbnail((200, 200))
        self.photo2 = ImageTk.PhotoImage(image2)
        self.abrir_web= tk.Button(self.master, image=self.photo2, command=self.abrir_sitio_web, border=0)
        #con esta el boton
        self.abrir_web.place(x=940, y=565)

        self.create_login_widgets()

        image1 = Image.open("boton_cerrar.png")
        image1.thumbnail((80, 80))
        self.photo1 = ImageTk.PhotoImage(image1)
        self.cerrar = tk.Button(master, image=self.photo1, command=self.confirmar_cerrar_ventana, border=0)
        self.cerrar.place(x=20,y=20)



    def cerrar_ventana(self):
        self.master.destroy()

    def confirmar_cerrar_ventana(self):
        resultado = messagebox.askquestion("Confirmar Cierre", "¿Estás seguro de que quieres salir de MAPPING?")
        if resultado == "yes":
            self.cerrar_ventana()

    def abrir_ventana_admin(self):

        # Crea una instancia de la ventana de administración desde el archivo ventana_admin.py
        ventana_admin_root = tk.Toplevel(self.master)
        ventana_administracion = VentanaAdmin(ventana_admin_root)


    def create_login_widgets(self):
        self.heading = Label(self.master, text="                       ", fg="#222feb", bg="white",
                             font=("Microsoft YaHei UI Light ", 23, "bold"))
        self.heading.place(x=960, y=280)

        self.heading2 = Label(self.master, text="                    ", fg="#222feb", bg="white",
                             font=("Microsoft YaHei UI Light ", 23, "bold"))
        self.heading2.place(x=960, y=400)
        self.heading3 = Label(self.master, text="                    ", fg="#222feb", bg="white",
                             font=("Microsoft YaHei UI Light ", 23, "bold"))
        self.heading3.place(x=960, y=330)
        self.heading4 = Label(self.master, text="                    ", fg="#222feb", bg="white",
                             font=("Microsoft YaHei UI Light ", 23, "bold"))
        self.heading4.place(x=960, y=350)
        self.heading3 = Label(self.master, text="                    ", fg="#222feb", bg="white",
                             font=("Microsoft YaHei UI Light ", 23, "bold"))
        self.heading3.place(x=960, y=300)
        self.heading3 = Label(self.master, text="                    ", fg="#222feb", bg="white",
                             font=("Microsoft YaHei UI Light ", 23, "bold"))
        self.heading3.place(x=960, y=460)


        self.user = Entry(self.master, width=19, fg="black", border=0, bg="white",
                          font=("Microsoft YaHei UI Light ", 14))
        self.user.place(x=960, y=300)
        self.user.insert(0, 'Nombre de usuario')
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)
        Frame(self.master, width=200, height=2, bg="black").place(x=950, y=330)

        self.code = Entry(self.master, width=19, fg="black", border=0, bg="white",
                          font=("Microsoft YaHei UI Light ", 14))
        self.code.place(x=960, y=373)
        self.code.insert(0, 'Contraseña')
        self.code.bind('<FocusIn>', self.on_enter_code)
        self.code.bind('<FocusOut>', self.on_leave_code)
        Frame(self.master, width=200, height=2, bg="black").place(x=950, y=400)

        Button(self.master, width=25, pady=10, text="INICIAR",
               bg="#222feb", fg="white", border=0, command=self.signin).place(x=960, y=440)

        label = Label(self.master, text="¿No tienes cuenta? ",
                      fg="black", bg="white", font=("Microsoft YaHei UI Light ", 9))
        label.place(x=950, y=530)

        sign_up = Button(self.master, width=10, text="Registrate", border=0, command=self.registrar,
                         bg="white", cursor="hand2", fg="#222feb")
        sign_up.place(x=1060, y=530)


    def on_enter_user(self, e):
        self.user.delete(0, 'end')

    def on_leave_user(self, e):
        name = self.user.get()
        if name == '':
            self.user.insert(0, 'Nombre de usuario')

    def on_enter_code(self, e):
        self.code.delete(0, 'end')
        self.code.config(show="*")  

    def on_leave_code(self, e):
        password = self.code.get()
        if password == '':
            self.code.insert(0, 'Contraseña')
            self.code.config(show="*")  


    def nombre (self):
        nombre = self.user
        return nombre




    def open_third_window(self):
        usuario_actual = self.user.get()
        self.master.withdraw()
        third_window = tk.Toplevel()
        admin_salones = obtener_admin_salones()  # Obtén la instancia admin_salones
        app = AplicacionBusquedaSalas(third_window, admin_salones,usuario_actual)
        third_window.mainloop()

    def open_third_window2(self):
        self.master.withdraw()
        third_window = tk.Toplevel()
        admin_salones = obtener_admin_salones()  # Obtén la instancia admin_salones
        usuario_actual = "nombre_usuario"  # Reemplaza con el usuario actual
        app = AplicacionBusquedaSalas2(third_window, admin_salones, usuario_actual)
        third_window.mainloop()


    def signin(self):
        nombre_usuario = self.user.get()
        contraseña = self.code.get()

        usuarios_ref = db.reference("/Registrados/Admin/")
        usuarios_snapshot = usuarios_ref.get()

        usuario_encontrado = None
        for usuario_id, usuario_data in usuarios_snapshot.items():
            if usuario_data.get('Usuario') == nombre_usuario:
                usuario_encontrado = usuario_data
                break  # Detener la iteración una vez que se encuentre el usuario

        if usuario_encontrado:
            if usuario_encontrado.get('Contraseña') == contraseña:
                messagebox.showinfo("Éxito", "Bienvenido Admin")
                print("AD", usuario_data, "Con", usuario_encontrado)
                
                self.abrir_ventana_admin()
            else:
                messagebox.showwarning("Error", "Contraseña incorrecta")
            return  # Salir de la función después de abrir la ventana de administrador

        # Si no se encontró como administrador, verificar profesores
        usuarios_ref = db.reference("/Registrados/Profesores/")
        usuarios_snapshot = usuarios_ref.get()

        usuario_encontrado = None
        for usuario_id, usuario_data in usuarios_snapshot.items():
            if usuario_data.get('Usuario') == nombre_usuario:
                usuario_encontrado = usuario_data
                break

        if usuario_encontrado:
            if usuario_encontrado.get('Contraseña') == contraseña:
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
                print("PRO", usuario_data, "Con", usuario_encontrado)
                self.open_third_window()
            else:
                messagebox.showwarning("Error", "Contraseña incorrecta")
            return  # Salir de la función después de abrir la ventana de profesores

        # Si no se encontró como profesor, verificar estudiantes
        usuarios_ref = db.reference("/Registrados/Estudiantes/")
        usuarios_snapshot = usuarios_ref.get()

        usuario_encontrado = None
        for usuario_id, usuario_data in usuarios_snapshot.items():
            if usuario_data.get('Usuario') == nombre_usuario:
                usuario_encontrado = usuario_data
                break

        if usuario_encontrado:
            if usuario_encontrado.get('Contraseña') == contraseña:
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
                print("As", usuario_data, "Con", usuario_encontrado)
                self.open_third_window2()
            else:
                messagebox.showwarning("Error", "Contraseña incorrecta")
        else:
            messagebox.showwarning("Error", "Usuario no encontrado")







    def abrir_sitio_web(self):
        url = "https://mapping-oficcial.netlify.app"
        
        # Ruta de Chrome en tu sistema
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        
        # Abre la URL en Chrome
        import subprocess
        subprocess.Popen([chrome_path, url])



    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Mantén una referencia a la imagen

    def open_second_window(self):
        second_window = Toplevel()  # Usa Toplevel para la segunda ventana
        app = ventana2.Ventana2(second_window)  # Crea la instancia de la segunda ventana
        second_window.mainloop()

    def registrar(self):
        self.open_second_window()





if __name__ == "__main__":


    root = Tk()
    app = Ventana1(root)
    root.mainloop()

