
from tkinter import *
import tkinter as tk
import speech_recognition as sr
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import PhotoImage

import firebase_admin
from firebase_admin import credentials, db


from ventana3 import obtener_admin_salones, AplicacionBusquedaSalas
from ventana2 import Ventana2
from ventana5 import Ventana5
from ventana_horario import VentanaHorario
from ventana_admin import VentanaAdmin




class VentanaAdmin1:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Admin 1")
        self.root.geometry("462x600")
        self.root.configure(bg="#fff")
        self.root.resizable(width=False, height=False)

        self.image_path2 = 'celular_png.png'
        self.img2 = self.load_thumbnail(self.image_path2, (700, 700))
        self.label_img2 = Label(self.root, image=self.img2, bg="#fff")
        self.label_img2.place(x=0, y=0)
        self.label_inicio = tk.Label(self.root, text="OPCIONES", fg="black", bg="white", font=("times", 30, "bold"))
        self.label_inicio.place(x=130, y=100)
        self.label_inicio2 = tk.Label(self.root, text="                                                ", fg="black", bg="black", font=("times", 30, "bold"))
        self.label_inicio2.place(x=10, y=570)
        # Agrega los botones sin funcionalidad aquí
        self.button1 = tk.Button(root, text=" BUSCADOR DE SALONES ",width=25, pady=10, bg="#222feb", fg="white", border=0,
                                  command=self.open_third_window,font=("times", 15)).place(x=100, y=180)

  

        self.button2 = tk.Button(root, text=" RUTAS GUARDADAS ",width=25, pady=10,bg="#222feb", fg="white", border=0,command=self.abrir_ventana5,font=("times", 15)).place(x=100, y=250)            




    #abrir buscador de salones
    def open_third_window(self):
        self.root.withdraw()
        third_window = tk.Toplevel()
        admin_salones = obtener_admin_salones()  # Obtén la instancia admin_salones
        usuario_actual = "nombre_usuario"  # Reemplaza con el usuario actual
        app = AplicacionBusquedaSalas(third_window, admin_salones, usuario_actual)
        third_window.mainloop()

    #abrir rutas guardadas
    def abrir_ventana5(self):

        ventana5_root = tk.Toplevel(self.root)
        ventana5 = Ventana5(ventana5_root)
        self.root.withdraw()


    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Mantén una referencia a la imagen


def main():
    root = tk.Tk()
    app = VentanaAdmin1(root)
    root.mainloop()

if __name__ == "__main__":
    main()
