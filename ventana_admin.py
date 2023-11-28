import tkinter as tk
from firebase_admin import db, credentials
import tkinter as ttk
import ventana1  # Asegúrate de importar el módulo ventana1

from tkinter import *
from PIL import Image, ImageTk


class VentanaAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Admin")
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
               
        self.label_inicio2 = tk.Label(self.root, text="                                                                                                  ", fg="black", bg="black", font=("times", 30, "bold"))
        self.label_inicio2.place(x=2, y=650)
        self.label_inicio2 = tk.Label(self.root, text="                                                                                                  ", fg="black", bg="black", font=("times", 17, "bold"))
        self.label_inicio2.place(x=2, y=0)
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


        etiqueta_2 = tk.Label(root, text=f"_________________", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_2.place(x=40,y=43)

        etiqueta2 = tk.Label(root, text=f"MENU ADMINISTRADOR", fg="black", bg="white",
                                    font=("times", 20, "bold"))
        etiqueta2.place(x=50,y=50)

        etiqueta_espacio = tk.Label(root, text=f"                  ", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_espacio.place(x=50,y=310)

        etiqueta_espacio2 = tk.Label(root, text=f"                              ", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_espacio2.place(x=50,y=370)

        etiqueta_espacio2 = tk.Label(root, text=f"                              ", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_espacio2.place(x=50,y=490)


        etiqueta_espacio2 = tk.Label(root, text=f"                              ", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        
        etiqueta_espacio2.place(x=50,y=560)

        etiqueta_espacio2 = tk.Label(root, text=f"                               ", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_espacio2.place(x=50,y=450)
        Button(self.root, width=22, pady=12, text="ADMINISTRAR VENTANAS",
        bg="#222feb", fg="white", border=0, command=self.ventanas_admin,font=("times", 15, "bold")).place(x=80, y=300)
  

        Button(self.root, width=22, pady=12, text="USUARIOS REGISTRADOS",
        bg="#222feb", fg="white", border=0, command=self.ver_usuarios,font=("times", 15, "bold")).place(x=80, y=400)





















    def ventanas_admin(self):
        from ventana_admin1 import VentanaAdmin1
        admin_window = tk.Toplevel(self.root)
        VentanaAdmin1(admin_window)
    def ver_usuarios(self):
        from ventana_admin2 import VentanaAdmin2
        admin_window = tk.Toplevel(self.root)
        VentanaAdmin2(admin_window)
        

    def ver_creditos (self):
        pass
     

    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Mantén una referencia a la imagen

if __name__ == "__main__":
    root = tk.Tk()
    ventana_admin = VentanaAdmin(root)
    root.mainloop()
