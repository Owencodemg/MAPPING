import tkinter as tk
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials, db
from tkinter import messagebox,ttk


class Ventana5:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Ventana 5")    
        self.parent.geometry("425x680")
        self.parent.configure(bg="#fff")
        
        #self.root.resizable(False, False)

        self.image_path = 'celu22.png'
        self.img = self.load_thumbnail(self.image_path, (800, 800))
        self.label_img = tk.Label(self.parent, image=self.img, bg="#fff")
        self.label_img.place(x=0, y=0)





        #espacios en blanco para tapar
        self.etiqueta_espacio= tk.Label(self.parent, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=270)
        self.etiqueta_espacio= tk.Label(self.parent, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=290)
        self.etiqueta_espacio= tk.Label(self.parent, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=370)
        
        self.etiqueta_espacio= tk.Label(self.parent, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=40, y=350)
        self.etiqueta_espacio= tk.Label(self.parent, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=360)
        self.etiqueta_espacio= tk.Label(self.parent, text="                              ",bg="white")
        self.etiqueta_espacio.place(x=82, y=430)
        self.etiqueta_espacio= tk.Label(self.parent, text="                                                                               ",bg="white")
        self.etiqueta_espacio.place(x=82, y=480)
        self.etiqueta_espacio= tk.Label(self.parent, text="                                                                                ",bg="white")
        self.etiqueta_espacio.place(x=82, y=470)

        #guiones para debajo
        
        self.label_inicio2 = tk.Label(self.parent, text="                                                                                                  ", fg="black", bg="black", font=("times", 30, "bold"))
        self.label_inicio2.place(x=2, y=650)
        self.label_inicio2 = tk.Label(self.parent, text="                                                                                                  ", fg="black", bg="black", font=("times", 17, "bold"))
        self.label_inicio2.place(x=2, y=0)







        self.parent.bind('<Escape>', self.cerrar_con_escape)

        self.rutas = [] 
        self.rutapisos = {}

   

        self.entrada1 = tk.Entry(parent, width=40, fg="black",font=('Helvetica', 12))
        self.entrada1.place(x=45, y=325)

        self.boton_buscar = tk.Button(parent, width=20, height=3, text="Buscar", command=self.get_images, bg="#222feb", fg="white", border=0)
        self.boton_buscar.place(x=150, y=552)
        
        # # Carga la imagen usando Pillow
        # self.image_path = 'guardadas2.png'
        # self.img = self.load_thumbnail(self.image_path, (900, 900))
        # self.label_img = tk.Label(self.parent, image=self.img, bg="#fff")
        # self.label_img.place(x=0, y=90)
        etiqueta_ = tk.Label(parent, text=f"________________", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_.place(x=65,y=265)
        etiqueta_ = tk.Label(parent, text=f"                                    ", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_.place(x=30,y=50)
        etiqueta_ = tk.Label(parent, text=f"                                ", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_.place(x=65,y=273)
        etiqueta2 = tk.Label(parent, text=f"RUTAS GUARDADAS", fg="black", bg="white",
                                    font=("times", 20, "bold"))
        etiqueta2.place(x=90,y=270)
 #logica para el nombre del usuario


        self.suggestion_listbox = tk.Listbox(parent, width=50, height=10,font=("arial", 10, "bold"))
        self.suggestion_listbox.place(x=45, y=350)

        # Obtiene las rutas guardadas y las agrega a la Listbox
        rutas_db = self.rutas_guardadas()
        for ruta in rutas_db:
            self.suggestion_listbox.insert(tk.END, ruta)
        self.suggestion_listbox.bind("<ButtonRelease-1>", self.on_suggestion_select)
        self.entrada1.bind("<KeyRelease>", lambda event: self.update_autocomplete_options())
        self.rutapisos = {


              #PRIMER PISO NOMBRE RUTAS


              #PRIMER PISO NOMBRE RUTAS

                0: "Entrada a Enfermería",
                1: "Entrada a Sala de Profesores",
                2: "Entrada a A101",
                3: "Entrada a A102",
                4: "Entrada a A103",
                5: "Entrada a C101",
                6: "Entrada a C102",
                7: "Entrada a C104",
                8: "Entrada a D101",

              #SEGUNDO PISO NOMBRE RUTAS
                9: "Entrada a Cafeteria Segundo Piso",



              #TERCER PISO NOMBRE RUTAS
                10: "Entrada a F304",
              #CUARTO PISO NOMBRE RUTAS
                11: "Entrada a F404",
                12: "Entrada a F405",
              #quinto PISO NOMBRE RUTAS
                13: "Entrada a F504",
                14: "Entrada a F505",
              #SEXTO PISO NOMBRE RUTAS
                15: "Entrada a Cafeteria Sexto Piso",
                16: "Entrada a C603",
                17: "Entrada a C604",

              
                # Define los nombres de las rutas aquí
            }
        self.routes = [

                #primer piso
                #fotos sala de enfermeria
                ["enfermeria_inicio.png","pre_entrada.png","foto_entradaz.png","foto2.png","foto3.png","foto_enfermeria.png","llegaste.png","fin.png"],
                #fotos sala de profesores
                ["salaprofesores_inicio.png","pre_entrada.png","foto_entradaz.png","foto2.png","foto3.png","foto_sala_de_profesores.png","llegaste.png","fin.png"],
                #fotos A101
                ["pre_entrada.png","foto_entradaz.png","foto2.png","foto4.png","foto5.png","foto_A101.png","llegaste.png","fin.png"],
                #fotos A102
                ["pre_entrada.png","foto_entradaz.png","foto2.png","foto4.png","foto5.peng","foto_A102.png","llegaste.png","fin.png"],
                #fotos A103
                ["pre_entrada.png","foto_entradaz.png","foto2.png","foto4.png","foto5.png","foto_A103.png","llegaste.png","fin.png"],
                #fotos C101
                ["c101_inicio.png","pre_entrada.png","foto_entradaz.png","foto2.png","foto6.png","foto7.png","foto_C101.png","llegaste.png","fin.png"],
                #fotos C102
                ["c102_inicio.png","pre_entrada.png","foto_entradaz.png","foto2.png","foto6.png","foto7.png","foto_C102.png","llegaste.png","fin.png"],
                #fotos C104
                ["c104_inicio.png","pre_entrada.png","foto_entradaz.png","foto2.png","foto6.png","foto7.png","foto_C104.png","llegaste.png","fin.png"],
                #fotos D101
                ["d101_inicio.png","pre_entrada.png","foto8.png","foto9.png","foto10.png","foto_D101.png","llegaste.png","fin.png"],

                #segundo piso
                ["cafeteria_segundo_inicio2.png","pre_entrada.png","foto8.png","foto11.png","tomar2.png","foto30.png","foto31.png","foto32.png","foto33.png","llegaste.png","fin.png"],


                #tercer piso
                ["f304_inicio.png","pre_entrada.png","foto8.png","foto11.png","tomar3.png","foto17.png","foto18.png","foto_f304.png","llegaste.png","fin.png"],
                #cuarto piso
               
                ["f404_inicio.png","pre_entrada.png","foto8.png","foto11.png","tomar4.png","foto19.png","foto18.png","foto_f304.png","llegaste.png","fin.png"],
                ["f404_inicio.png","pre_entrada.png","foto8.png","foto11.png","tomar4.png","foto19.png","foto18.png","foto_f304.png","llegaste.png","fin.png"],
                #quinto piso

                ["f504_inicio.png","pre_entrada.png","foto8.png","foto11.png","tomar5.png","foto20.png","foto_diagonal5.png","foto21.png","foto_f504.png","llegaste.png","fin.png"],
                ["f505_inicio.png","pre_entrada.png","foto8.png","foto11.png","tomar5.png","foto20.png","foto_diagonal5.png","foto21.png","foto_f505.png","llegaste.png","fin.png"],
                #sexto piso

                ["cafeteria_sexto_inicio.png","pre_entrada.png","foto8.png","foto11.png","tomar6.png","foto22.png","foto23.png","foto24.png","foto_cafeteria_sexto_piso.png","llegaste.png","fin.png"],
                ["c603_inicio.png","pre_entrada.png","foto8.png","foto11.png","tomar6.png","foto22.png","foto23.png","foto24.png","foto25.png","foto26.png","foto_c603.png","llegaste.png","fin.png"],
                ["c604_inicio.png","pre_entrada.png","foto8.png","foto11.png","tomar6.png","foto22.png","foto23.png","foto24.png","foto25.png","foto26.png","foto_c604.png","llegaste.png","fin.png"],
            


            ]

       

        self.current_route_index = 0
        self.current_image_index = 0
    def cerrar_con_escape(self, event):
        self.parent.destroy()
    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Mantén una referencia a la imagen


    def on_suggestion_select(self, event):
        selected_item = self.suggestion_listbox.get(self.suggestion_listbox.curselection())
        self.entrada1.delete(0, tk.END) 
        self.entrada1.insert(0, selected_item) 
        self.suggestion_listbox.delete(0, tk.END)
        



    def update_autocomplete_options(self, event=None):
        rutas_db = self.rutas_guardadas()  
        query = self.entrada1.get().lower()
        autocomplete_options = [ruta for ruta in rutas_db if query in ruta.lower()]
        self.suggestion_listbox.delete(0, tk.END)
        for suggestion in autocomplete_options:
            self.suggestion_listbox.insert(tk.END, suggestion)

   

    def mostrar_informacion_sala(self, sala):
        if not hasattr(self, "ventana_info_sala") or not self.ventana_info_sala:
            self.ventana_info_sala = tk.Toplevel(self.parent)
            self.ventana_info_sala.config(bg="white")
            self.ventana_info_sala.resizable(height=0, width=0)
            self.ventana_info_sala.config(bd=0)
            self.ventana_info_sala.geometry("1900x900")
            self.ventana_info_sala.title(f"Mis rutas guardadas")

                # Carga la imagen usando Pillow
            imagen_path = "im1.png"  # Cambia esto a la ruta de tu imagen
            imagen = Image.open(imagen_path)
            imagen = imagen.resize((500, 500))
            self.imagen_tk = ImageTk.PhotoImage(imagen)  # Mantén la referencia

                # Etiqueta para mostrar la imagen
            etiqueta_imagen = tk.Label(self.ventana_info_sala, image=self.imagen_tk)
            etiqueta_imagen.place(x=200, y=100)

                

            etiqueta_ubicacion = tk.Label(self.ventana_info_sala, text=f"CEDESARROLLO", fg="black", bg="white",
                                    font=("times", 30, "bold"))
            etiqueta_ubicacion.place(x=830,y=150)



            

    #entry para rutassssssss
            self.dte_label = tk.Label(self.ventana_info_sala,text="¿Desde donde quieres ir?",fg="#222feb", bg="white", font=("Microsoft YaHei UI Light ", 25, "bold"))
            self.dte_label.place(x=800,y=250)
            self.route_name_entry = tk.Entry(self.ventana_info_sala, width=40, font=('Helvetica', 12))
            self.route_name_entry.place(x=815, y=310)
                



            self.image_label = None  # Inicializar el atributo de la etiqueta de la imagen
            self.combobox = tk.Listbox(self.ventana_info_sala, width=60, height=6)
            self.combobox.place(x=815,y=330)


    def get_images(self):
        route_name = self.entrada1.get()
   
        
        if route_name in self.rutapisos.values():
            self.current_route_index = list(self.rutapisos.values()).index(route_name)
            self.show_images_window()
        else:
            tk.messagebox.showerror("Error", "Nombre de sala no encontrado.")


    def show_images_window(self):
            images_window = tk.Toplevel(self.parent)
            images_window.title("Imágenes de Ruta")
            images_window.geometry("1280x970")

            images_window.resizable(False, False)


            canvas = tk.Canvas(images_window, width=400, height=400)
            canvas.pack()

            self.image_label = tk.Label(canvas)
            self.image_label.pack()

            self.update_image_label()  # Llama al método local para actualizar la etiqueta de la imagen


            image1 = Image.open("regresar41.png")
            image1.thumbnail((80, 80))
            self.photo1 = ImageTk.PhotoImage(image1)
            self.bregresar = tk.Button(images_window, image=self.photo1, command=self.show_previous_image, border=0)
        #con esta el boton
            self.bregresar.place(x=0, y=600)

        




            image2 = Image.open("adelantar41.png")
            image2.thumbnail((80, 80))
            self.photo2 = ImageTk.PhotoImage(image2)
            self.adelantar = tk.Button(images_window, image=self.photo2, command=self.show_next_image, border=0)
        #con esta el boton
            self.adelantar.place(x=1200, y=600)



            self.button_state = 0  

            # Carga y redimensiona las imágenes
            # self.image1 = self.load_and_resize_image("igg1.png", (50, 50))
            # self.image2 = self.load_and_resize_image("igg33.png", (50, 50))

            # # Crea el botón con la primera imagen
            # self.button = tk.Button(images_window, image=self.image1, command=self.toggle_button)
            # self.button.image = self.image1
            # self.button.place(x=10,y=10)


    def update_image_label(self):
        image_path = self.routes[self.current_route_index][self.current_image_index]
        img = Image.open(image_path)
        img.thumbnail((1900, 1900))
        photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def show_next_image(self):
            self.current_image_index = (self.current_image_index + 1) % len(self.routes[self.current_route_index])
            self.update_image_label()

    def show_previous_image(self):
            self.current_image_index = (self.current_image_index - 1) % len(self.routes[self.current_route_index])
            self.update_image_label()

    def rutas_guardadas(self):
        usuarios_ref = db.reference("/Registrados")
        usuarios_snapshot = usuarios_ref.get()

        rutas = []  # Lista para almacenar las rutas

        for usuario_id in usuarios_snapshot:
            self.usuario_actual = usuario_id
            if self.usuario_actual:
                rutas_ref = db.reference(f"/RutasGuardadas/{self.usuario_actual}")
                rutas_snapshot = rutas_ref.get()

                if rutas_snapshot:
                    rutas += list(rutas_snapshot.values())  # Agrega las rutas a la lista

        return rutas
        


         
        


if __name__ == "__main__":
    firebase_sdk3 = credentials.Certificate("mapping-1a38f-firebase-adminsdk-8nf6d-117e271815.json")
    firebase_admin.initialize_app(firebase_sdk3, {"databaseURL": "https://mapping-1a38f-default-rtdb.firebaseio.com/"})

    root = tk.Tk()
    ventana5 = Ventana5(root)
    
    root.mainloop()