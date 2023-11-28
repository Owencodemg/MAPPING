import tkinter as tk
from tkinter import ttk

class VentanaModificacion(tk.Toplevel):
    def __init__(self, parent, rutas_guardadas, route_names, routes):
        super().__init__(parent)
        self.title("Modificar Listas")
        self.geometry("400x400")

        self.rutas_guardadas = rutas_guardadas
        self.route_names = route_names
        self.routes = routes

        self.label_rutas = ttk.Label(self, text="Lista de Rutas:")
        self.label_rutas.pack()

        self.listbox_rutas = tk.Listbox(self)
        self.listbox_rutas.pack()

        for nombre_ruta in self.rutas_guardadas:
            self.listbox_rutas.insert(tk.END, nombre_ruta)

        self.label_imagenes = ttk.Label(self, text="Lista de Imágenes:")
        self.label_imagenes.pack()

        self.listbox_imagenes = tk.Listbox(self)
        self.listbox_imagenes.pack()

        for nombre_imagen in self.routes:
            self.listbox_imagenes.insert(tk.END, nombre_imagen)

        self.entry_nueva_ruta = ttk.Entry(self)
        self.entry_nueva_ruta.pack()

        self.button_agregar_ruta = ttk.Button(self, text="Agregar Ruta", command=self.agregar_ruta)
        self.button_agregar_ruta.pack()

        self.entry_nuevo_nombre_ruta = ttk.Entry(self)
        self.entry_nuevo_nombre_ruta.pack()

        self.button_modificar_ruta = ttk.Button(self, text="Modificar Ruta", command=self.modificar_ruta)
        self.button_modificar_ruta.pack()

        self.button_eliminar_ruta = ttk.Button(self, text="Eliminar Ruta", command=self.eliminar_ruta)
        self.button_eliminar_ruta.pack()

        self.entry_nueva_imagen = ttk.Entry(self)
        self.entry_nueva_imagen.pack()

        self.button_agregar_imagen = ttk.Button(self, text="Agregar Imagen", command=self.agregar_imagen)
        self.button_agregar_imagen.pack()

        self.button_eliminar_imagen = ttk.Button(self, text="Eliminar Imagen", command=self.eliminar_imagen)
        self.button_eliminar_imagen.pack()

    def agregar_ruta(self):
        nueva_ruta = self.entry_nueva_ruta.get()
        if nueva_ruta:
            self.rutas_guardadas.append(nueva_ruta)
            self.listbox_rutas.insert(tk.END, nueva_ruta)
            self.entry_nueva_ruta.delete(0, tk.END)

    def modificar_ruta(self):
        indice_seleccionado = self.listbox_rutas.curselection()
        nuevo_nombre_ruta = self.entry_nuevo_nombre_ruta.get()
        if indice_seleccionado and nuevo_nombre_ruta:
            indice = indice_seleccionado[0]
            self.rutas_guardadas[indice] = nuevo_nombre_ruta
            self.listbox_rutas.delete(indice)
            self.listbox_rutas.insert(indice, nuevo_nombre_ruta)
            self.entry_nuevo_nombre_ruta.delete(0, tk.END)

    def eliminar_ruta(self):
        indice_seleccionado = self.listbox_rutas.curselection()
        if indice_seleccionado:
            indice = indice_seleccionado[0]
            del self.rutas_guardadas[indice]
            self.listbox_rutas.delete(indice)

    def agregar_imagen(self):
        nueva_imagen = self.entry_nueva_imagen.get()
        if nueva_imagen:
            self.routes.append(nueva_imagen)
            self.listbox_imagenes.insert(tk.END, nueva_imagen)
            self.entry_nueva_imagen.delete(0, tk.END)

    def eliminar_imagen(self):
        indice_seleccionado = self.listbox_imagenes.curselection()
        if indice_seleccionado:
            indice = indice_seleccionado[0]
            del self.routes[indice]
            self.listbox_imagenes.delete(indice)

if __name__ == "__main__":
    root = tk.Tk()
    
    rutas_guardadas = ["Ruta 1", "Ruta 2", "Ruta 3"]
    routes = [
        ["imagen1.png", "imagen2.png"],
        ["imagen3.png", "imagen4.png"]
    ]
    route_names = {
        0: "Nombre Ruta 1",
        1: "Nombre Ruta 2"
    }

    ventana_modificacion = VentanaModificacion(root, rutas_guardadas, route_names, routes)
    root.mainloop()
