import tkinter as tk
from tkinter import *
import ventana1

from ventana5 import Ventana5
from ventana_seguridad2 import VentanaSeguridad2  
class VentanaOpciones2:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Ventana de Actualización")
        self.ventana.geometry("400x400")
        self.ventana.configure(bg="#fff")

        # Etiqueta inicial
        self.label_inicio = tk.Label(self.ventana, text="OPCIONES", fg="black", bg="white", font=("times", 30, "bold"))
        self.label_inicio.place(x=100, y=30)

        # Botón "Actualizar Información"

        self.boton_actualizar22 = tk.Button(self.ventana, text="CERRAR SESION", command=self.cerrar_sesion, width=50, height=3, bg="#222feb", fg="white", border=0)
        self.boton_actualizar22.place(x=30, y=240)

        self.boton_actualizar1 = tk.Button(self.ventana, text="ACTUALIZAR INFORMACION", command=self.abrir_ventana_seguridad, width=50, height=3, bg="#222feb", fg="white", border=0)
        self.boton_actualizar1.place(x=30, y=150)


    def abrir_ventana_seguridad(self):
    # Crear una instancia de la ventana de seguridad
     ventana_seguridad = VentanaSeguridad2() 




    def abrir_ventana5(self):

        ventana5_root = tk.Toplevel(self.ventana)
        ventana5 = Ventana5(ventana5_root)



        self.ventana.withdraw()
    def cerrar_sesion(self):

        # Crear y mostrar la ventana1 al cerrar la sesión

        self.ventana.withdraw()  # Oculta la ventana actual
        ventana1_root = tk.Toplevel(self.ventana)  # Crea una nueva ventana
        ventana_uno = ventana1.Ventana1(ventana1_root)  # Crea la instancia de la ventana1
        ventana1_root.mainloop()  # Muestra la ventana

if __name__ == "__main__":
    app = VentanaOpciones2()
    app.ventana.mainloop()
