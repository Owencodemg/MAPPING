import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

class VentanaAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana de Administración")
        self.root.geometry("1200x900")
        self.image_path = 'loginl.png'
        self.img = self.load_thumbnail(self.image_path, (700, 800))
        self.label_img = tk.Label(self.root, image=self.img, bg="#fff")
        self.label_img.place(x=700, y=50)

        label = tk.Label(root, text="Bienvenido a la Ventana de Administración", font=("Arial", 16))
        label.pack(pady=20)

        # Ejemplo de sala (supongamos que tienes una instancia de Sala llamada 'sala')
        self.sala = Sala(nombre="Sala de Ejemplo", ruta="Ruta de Ejemplo")

        # Botones para modificar, agregar y eliminar rutas
        boton_modificar_ruta = tk.Button(self.root, text="Modificar Ruta", command=self.modificar_ruta)
        boton_modificar_ruta.pack()
        
        boton_agregar_ruta = tk.Button(self.root, text="Agregar Ruta", command=self.agregar_ruta)
        boton_agregar_ruta.pack()
        
        boton_eliminar_ruta = tk.Button(self.root, text="Eliminar Ruta", command=self.eliminar_ruta)
        boton_eliminar_ruta.pack()

        # Etiqueta para mostrar la ruta de la sala
        etiqueta_ruta = tk.Label(self.root, text=f"Ruta: {self.sala.ruta}", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_ruta.pack()

    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Mantén una referencia a la imagen

    def modificar_ruta(self):
        # Obtener la ruta actual de la sala
        ruta_actual = self.sala.ruta

        # Mostrar un cuadro de diálogo para que el usuario ingrese la nueva ruta
        nueva_ruta = simpledialog.askstring("Modificar Ruta", "Ingrese la nueva ruta:")

        # Actualizar la ruta de la sala con la nueva ruta ingresada por el usuario
        if nueva_ruta is not None:
            self.sala.ruta = nueva_ruta

    def agregar_ruta(self):
        # Mostrar un cuadro de diálogo para que el usuario ingrese la nueva ruta
        nueva_ruta = simpledialog.askstring("Agregar Ruta", "Ingrese la nueva ruta:")

        # Verificar si se ingresó una ruta y si es válida
        if nueva_ruta is not None and nueva_ruta != "":
            # Agregar la nueva ruta a la lista de rutas de la sala (supongamos que tienes una lista de rutas)
            self.sala.ruta = nueva_ruta

    def eliminar_ruta(self):
        # Mostrar una lista de rutas disponibles para que el usuario elija cuál eliminar
        ruta_a_eliminar = simpledialog.askinteger("Eliminar Ruta", "Seleccione la ruta a eliminar:",
                                                  minvalue=0, maxvalue=len(self.sala.rutas) - 1)

        if ruta_a_eliminar is not None:
            # Eliminar la ruta seleccionada (supongamos que tienes una lista de rutas)
            del self.sala.rutas[ruta_a_eliminar]


class Sala:
    def __init__(self, nombre, ruta):
        self.nombre = nombre
        self.ruta = ruta


if __name__ == "__main__":
    root = tk.Tk()
    ventana_admin = VentanaAdmin(root)
    root.mainloop()
