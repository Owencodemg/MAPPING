import tkinter as tk
import tkinter as ttk
from PIL import Image, ImageTk
from firebase_admin import db, credentials


class VentanaHorario:
    def __init__(self, salon):
        self.root = tk.Toplevel()
        

        self.root.configure(bg="#fff")

        self.root.title(f"Horario de {salon.nombre}")
        self.image_path = 'calendario_miguel.png'
        self.img = self.load_thumbnail(self.image_path, (800, 800))
        self.label_img = tk.Label(self.root, image=self.img, bg="#fff")
        self.label_img.place(x=300, y=0)

        
        # image2 = Image.open("web_link.png")
        # image2.thumbnail((80, 80))
        # self.photo2 = ImageTk.PhotoImage(image2)
        # self.abrir_web= tk.Button(self.root, image=self.photo2, command=self.abrir_sitio_web, border=0)
        # #con esta el boton
        # self.abrir_web.place(x=0, y=0)





        # etiqueta_ = tk.Label(self.root, text=f"________________________", fg="black", bg="white",
        #                             font=("times", 30, "bold"))
        # etiqueta_.place(x=460,y=60)
            
        # etiqueta2 = tk.Label(self.root, text=f"HORARIO DE DISPONIBILIDAD", fg="black", bg="white",
        #                             font=("times", 30, "bold"))
        # etiqueta2.place(x=500,y=50)
    #logica para el nombre del usuario
        usuarios_ref = db.reference("/Registrados")
        usuarios_snapshot = usuarios_ref.get()

        usuario_encontrado = None
        for usuario_id, usuario_data in usuarios_snapshot.items():
            nom = usuario_data.get('Usuario')

      
        label_usuario = tk.Label(self.root, text=f"{nom}", fg="black", bg="white", font=("times", 17))
        label_usuario.place(x=8,y=55)  #

        self.image_path5 = 'userp2.png' 
        self.img5 = self.load_thumbnail(self.image_path5, (50, 50))
        self.label_img5 = ttk.Label(self.root, image=self.img5, background="#fff")
        self.label_img5.place(x=10,y=10)




        # Crea un frame con borde sin fondo

        horarios = {
            "D101": {
                "  ": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": ""
            },
            "D102": {
                "Lunes": "",
                " ": " ",
                "Martes": "9:30 AM - 11:30 AM",
                " ": " ",
                "Miércoles": "",
                " ": " ",
                "Jueves": "9:00 AM - 11:00 AM",
                " ": " ",
                "Viernes": "",
                " ": " ",
                "Sábado": ""
            },
            "D103": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "D104": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "D105": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },

            "C101": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "C102": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "C103": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "C104": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "C105": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "A101": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "A102": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "A103": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "A104": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "Auditorio": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "C201": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
             "C202": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",

 },            "C203": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",

 },           
               "C204": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",

 },      
            "C301": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "C302": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "C303": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "C304": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "D301": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "D302": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "D303": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "F301": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "F302": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "F303": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "F304": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "D401": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "D402": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "D403": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "F401": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "F402": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "F403": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "F404": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "F405": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
 },
            "C401": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "C402": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "C403": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "C404": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "F501": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "F502": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "F503": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "F504": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "F505": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "D501": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "D502": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "D503": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "D504": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "C601": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "C602": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "C603": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",
},
            "C604": {
                "Lunes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Martes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Miércoles": "7:00 PM - 8:00 PM",
                " ": " ",
                "Jueves": "7:00 PM - 8:00 PM",
                " ": " ",
                "Viernes": "7:00 PM - 8:00 PM",
                " ": " ",
                "Sábado": "7:00 PM - 8:00 PM",

            }
            
            
            # Agrega más salones y sus horarios aquí
        }
        image1 = Image.open("regresar44.png")
        image1.thumbnail((80, 80))
        self.photo1 = ImageTk.PhotoImage(image1)
        self.bregresar = tk.Button(self.root, image=self.photo1, command=self.regresar, border=0)
        self.bregresar.place(x=10, y=710)
        # Variable para controlar si el salón está ocupado o no
        self.ocupado = False
        self.etiqueta_estado = tk.Label(self.root, text="", fg="red")


        # Crea una etiqueta para mostrar el estado del salón
        self.etiqueta_estado = tk.Label(self.root, text="", fg="red", bg="white", font=("times", 16))
 
        self.boton_estado = tk.Button(self.root, text="Cambiar Estado", command=self.cambiar_estado)
   
        
        self.boton_estado2 = tk.Button(self.root, text="Cambiar Estado", command=self.cambiar_estado)
     


        self.boton_estado3 = tk.Button(self.root, text="Cambiar Estado", command=self.cambiar_estado)
     
        self.boton_estado4 = tk.Button(self.root, text="Cambiar Estado", command=self.cambiar_estado)


        self.boton_estado5 = tk.Button(self.root, text="Cambiar Estado", command=self.cambiar_estado)
    


        self.boton_estado6 = tk.Button(self.root, text="Cambiar Estado", command=self.cambiar_estado)
    








        horario = horarios.get(salon.nombre, {})

        horario_texto = ""

        dias_semana = ["  "," ", "Martes"," ", "Miércoles"," ", "Jueves"," ", "Viernes"," ", "Sábado"]
        for dia in dias_semana:
            horario_dia = horario.get(dia, "")
            if horario_dia:
                horario_texto += f"{dia}: {horario_dia}\n"


        if  horario_texto == "Zona verde":
            horario_texto = "Horario no disponible"


        # Crea una etiqueta para mostrar el horario
        etiqueta_horario = tk.Label(self.root, text=horario_texto, fg="black", bg="white", font=("times", 16))
        etiqueta_horario.place(x=530, y=80)

    def regresar(self):
        from ventana3 import AplicacionBusquedaSalas, obtener_admin_salones
        usuario_actual = 0
    
        admin_salones = obtener_admin_salones()  
    
        root = tk.Toplevel()
        root.deiconify()
        app = AplicacionBusquedaSalas(root, admin_salones, usuario_actual)
        self.root.withdraw()
        

    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Mantén una referencia a la imagen

    def cambiar_estado(self):
        self.ocupado = not self.ocupado
        if self.ocupado:
            # Usar place() para definir la posición de la etiqueta
            self.etiqueta_estado.config(text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", fg="dark blue", font=("times", 16))
            self.etiqueta_estado.place(x=410, y=200)
            

        else:
            self.etiqueta_estado.config(text="", fg="red")
 