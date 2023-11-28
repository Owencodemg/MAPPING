import tkinter as tk
from PIL import Image, ImageTk

class VentanaActualizar:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana de Actualización")
        self.root.attributes('-fullscreen', True)
        self.image_path = 'actualizar_foto.png'
        self.img = self.load_thumbnail(self.image_path, (900, 900))
        self.label_img = tk.Label(self.root, image=self.img, bg="#fff")
        self.label_img.place(x=300, y=20)
        self.etiqueta_espacio = tk.Label(self.root, text="                                                                  ", bg="black")
        self.etiqueta_espacio.place(x=520, y=300)

        
        self.etiqueta_espacio2= tk.Label(self.root, text="                                                                  ",bg="black")
        self.etiqueta_espacio2.place(x=520, y=320)
        self.etiqueta_espacio3= tk.Label(self.root, text="                                                                  ",bg="black")
        self.etiqueta_espacio3.place(x=520, y=350)



        self.user = self.create_entry("Nombre De Usuario", x=520, y=280)
        self.code_id = self.create_entry("ID",x=520 , y=310)
        self.code = self.create_entry("Contraseña", x=520, y=339)
        self.code_confirm = self.create_entry("Confirmar Contraseña", x=520, y=369)

        boton_guardar = tk.Button(self.root, width=29, pady=5, text="ACTUALIZAR", bg="#222feb", fg="white", border=0, command=self.guardar_informacion)
        boton_guardar.place(x=520,y=392)
        boton_cerrar = tk.Button(self.root, text="Cerrar Ventana", command=self.cerrar_ventana)
        boton_cerrar.pack()
        


    def guardar_informacion(self):
        # Recopilar la información ingresada en las entradas
        informacion = [entrada.get() for entrada in self.entradas]

        # Imprimir la información en la consola
        print("Información guardada:")
        for dato in informacion:
            print(dato)

    def create_entry(self, default_text, x, y):
        entry = tk.Entry(self.root, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light ", 11), bd=2)
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
    def cerrar_ventana(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
