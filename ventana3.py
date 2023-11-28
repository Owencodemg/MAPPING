
import tkinter as tk
import speech_recognition as sr

from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import PhotoImage
from ventana5 import Ventana5 
import firebase_admin
from firebase_admin import db, credentials
from ventana_horario import VentanaHorario
import functools


#CLASE SALON ----------------
class Salon:
    def __init__(self, nombre, ubicacion, ruta, referencia):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.ruta = ruta
        self.referencia = referencia
        self.opciones_combobox = []
    def asignar_nombre(self, nombre):
        self.nombre = nombre

    def asignar_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def asignar_punto_referencia(self, referencia):
        self.referencia = referencia

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def mostrar_nombre(self):
        print(f"Nombre del salón: {self.nombre}")

    def mostrar_ubicacion(self):
        print(f"Ubicación del salón: {self.ubicacion}")

    def mostrar_punto_referencia(self):
        print(f"Punto de referencia del salón: {self.referencia}")

    def mostrar_ruta(self):
        if self.ruta:
            print(f"Ruta del salón {self.nombre}: {self.ruta}")
        else:
            print(f"No se ha asignado una ruta al salón {self.nombre}")
class AdministradorSalones:
    def __init__(self):
        self.salones = []
#METODO PARA LOS ATRIBUTOS DE LA CLASE----------------------------------------------
    def agregar_salon(self, nombre, ubicacion, ruta, referencia, opciones_combobox):
        nuevo_salon = Salon(nombre, ubicacion, ruta, referencia)
        nuevo_salon.opciones_combobox = opciones_combobox
        self.salones.append(nuevo_salon)



    def obtener_salon_por_nombre(self, nombre):
        for salon in self.salones:
            if salon.nombre == nombre:
                return salon
        return None

    def mostrar_salones(self):
        for salon in self.salones:
            salon.mostrar_nombre()
            salon.mostrar_ubicacion()
            salon.mostrar_punto_referencia()
            salon.mostrar_ruta()
            print()
#VENTANA PARA BUSCAR SALONES--------------------------
class AplicacionBusquedaSalas:


    rutas_guardadas = []
    def __init__(self, root, admin_salones,usuario_actual):

        self.root = root

        self.root.title("Aplicación de Búsqueda de Salas")
        self.usuario_actual = usuario_actual
        self.root.config(bg="white")
        self.root.attributes('-fullscreen', True)


        self.root.bind('<Escape>', self.cerrar_con_escape)
        self.image_path = 'menu44.png' 
        self.img = self.load_thumbnail(self.image_path, (500, 500))
        self.label_img = ttk.Label(self.root, image=self.img, background="#fff")
        self.label_img.place(x=200,y=100)
        self.admin_salones = admin_salones
        self.imagen_tk = None 



        image1 = Image.open("tuerca3.jpg")
        image1.thumbnail((80, 80))
        self.photo54 = ImageTk.PhotoImage(image1)

        self.bregresar = tk.Button(self.root, image=self.photo54, command=self.abrir_ventana2, border=0)
        self.bregresar.place(x=1200, y=560)


        #abrir ventana rutasguardadas

        etiqueta_2 = tk.Label(root, text=f"___________________", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_2.place(x=810,y=165)

        etiqueta_mapping = tk.Label(root, text=f"MAPPING", fg="black", bg="white",
                                    font=("times", 30, "bold"))
        etiqueta_mapping.place(x=910,y=150)



        self.etiqueta = tk.Label(root, text="ELIGE TU DESTINO", fg="blue", bg="white", font=("Microsoft YaHei UI Light ", 25, "bold"))
        self.etiqueta.place(x=850, y=230)




        self.entrada = tk.Entry(root, width=40, font=('Helvetica', 12))
        self.entrada.place(x=820, y=300)


        self.boton_buscar = tk.Button(root, width=50, height=2, text="BUSCAR", command=self.buscar_sala, bg="#222feb", fg="white", border=0)
        self.boton_buscar.place(x=830, y=500)

        self.autocomplete_list = ["D101", "D102", "D103", "D104", "D105","Zona verde", "C101", "C102", "C103", "C104", "C105", "A101", "A102", "A103", "A104", "Enfermería","Parqueadero", "Bienestar estudiantil", "Sala de profesores", "Auditorio", "C201", "C202", "C203", "C204", "Centro de fotocopiado", "Cafetería segundo piso", "Biblioteca", "C301", "C302", "C303", "C304", "D301", "D302", "D303", "F301", "F302", "F303", "F304", "D401", "D402", "D403", "F401", "F402", "F403", "F404", "F405", "C401", "C402", "C403", "C404", "Laboratorio", "F501", "F502", "F503", "F504", "F505", "D501", "D502", "D503", "D504", "C601", "C602", "C603", "C604", "Cafetería sexto piso"]

        self.suggestion_listbox = tk.Listbox(self.root, width=60, height=6)
        self.suggestion_listbox.place(x=820, y=325)
        self.suggestion_listbox.bind("<ButtonRelease-1>", self.on_suggestion_select)
        self.entrada.bind("<KeyRelease>", lambda event: self.update_autocomplete_options())



        self.image_path5 = 'userp2.png' 
        self.img5 = self.load_thumbnail(self.image_path5, (50, 50))
        self.label_img5 = ttk.Label(self.root, image=self.img5, background="#fff")
        self.label_img5.place(x=10,y=10)

        self.image_button = tk.Button(self.root, width=50, height=2, text="VER MIS RUTAS GUARDADAS", command=self.abrir_ventana5, bg="#222feb", fg="white", border=0)
        self.image_button.place(x=830, y=550)

  
        # Botón con la segunda imagen
        self.image_button_path2 = 'miro2.png'  # Ruta de la segunda imagen del botón
        self.img_button2 = self.load_image(self.image_button_path2)
        self.image_button2 = tk.Button(self.root, image=self.img_button2, command=self.microfono, bd=0, cursor="hand2")
        self.image_button2.place(x=1210, y=300)


        image1 = Image.open("boton_cerrar.png")
        image1.thumbnail((80, 80))
        self.photo1 = ImageTk.PhotoImage(image1)
        self.cerrar = tk.Button(root, image=self.photo1, command=self.confirmar_cerrar_ventana, border=0)
        self.cerrar.place(x=20,y=20)

#FUNCION PARA ABRIR VENTANA OPCIONES, PARA ACTUALIZAR INFORMACION Y CERRAR SESION--------------------------

    def abrir_ventana2(self):

        from ventana_opciones2 import VentanaOpciones2

        ventana_actualizar = VentanaOpciones2()

    def cerrar_ventana(self):
        self.root.destroy()

    def confirmar_cerrar_ventana(self):
        resultado = messagebox.askquestion("Confirmar Cierre", "¿Estás seguro de que quieres salir de MAPPING?")
        if resultado == "yes":
            self.cerrar_ventana()

    def cerrar_con_escape(self, event):
        self.root.destroy()
    def microfono(self):
        # Mapeo de palabras a números
        numero_palabra = {
            "cero": "0",
            "uno": "1",
            "dos": "2",
            "tres": "3",
            "cuatro": "4",
            "cinco": "5",
            "seis": "6",
            # Agrega más mapeos según sea necesario
        }

        # Mapeo de palabras a cambios
        mapeo_palabras = {
            "B101": "D101",
            "Deunocerodos": "D102",

            "Python": "lenguaje de programación",
            # Agrega más mapeos según sea necesario
        }

        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source)  # Ajustar para eliminar el ruido
                tk.messagebox.showinfo("Habla ahora", "presiona aceptar...")
                audio = recognizer.listen(source, timeout=5)  # Escuchar durante 5 segundos
                tk.messagebox.showinfo("Procesando", "presiona aceptar...")
                texto = recognizer.recognize_google(audio, language="es-ES")  # Reconocer el discurso

                # Convertir la primera letra en mayúscula
                texto = texto.capitalize()

                # Reemplazar palabras por números si están en el mapeo
                palabras = texto.split()  # Dividir el texto en palabras
                for i in range(len(palabras)):
                    palabra = palabras[i].lower()  # Convertir la palabra a minúscula
                    if palabra in numero_palabra:
                        palabras[i] = numero_palabra[palabra]  # Reemplazar por el número correspondiente

                # Unir las palabras nuevamente en una cadena
                texto = ' '.join(palabras)

                # Aplicar cambios según el mapeo de palabras
                for palabra, cambio in mapeo_palabras.items():
                    texto = texto.replace(palabra, cambio)

                # Agregar el texto reconocido al Entry
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, texto)

            except sr.WaitTimeoutError:
                tk.messagebox.showwarning("Tiempo de espera", "No se detectó ningún discurso.")
            except sr.UnknownValueError:
                tk.messagebox.showwarning("No se pudo entender", "No se pudo entender el discurso.")
            except sr.RequestError as e:
                tk.messagebox.showerror("Error de solicitud", f"Error al solicitar el reconocimiento: {e}")


    def load_image(self, path):
        img = Image.open(path)
        img = img.resize((50, 50))  # Ajusta el tamaño de la imagen a (10, 10)
        return ImageTk.PhotoImage(img)

    def load_thumbnail(self, path, size):
        img = Image.open(path)
        img.thumbnail(size)
        return ImageTk.PhotoImage(img)




#VENTANA PARA BUSCAR RUTAS GUARDADAS-------------------------

    def abrir_ventana5(self):

        ventana5_root = tk.Toplevel(self.root)
        ventana5 = Ventana5(ventana5_root)


#LOGICA PARA AUTOCOMPLETAR--------------------------

    def update_autocomplete_options(self):
        query = self.entrada.get() 
        autocomplete_options = [option for option in self.autocomplete_list if query.lower() in option.lower()]
        self.suggestion_listbox.delete(0, tk.END)
        for suggestion in autocomplete_options:
            self.suggestion_listbox.insert(tk.END, suggestion)



    def on_suggestion_select(self, event):
        selected_item = self.suggestion_listbox.get(self.suggestion_listbox.curselection())
        self.entrada.delete(0, tk.END) 
        self.entrada.insert(0, selected_item) 
        self.suggestion_listbox.delete(0, tk.END)


#REDIMENSIONAR LAS FOTOS--------------------------

    def load_thumbnail(self, image_path, size):
        image = Image.open(image_path)
        image.thumbnail(size)
        return ImageTk.PhotoImage(image)

    def buscar_sala(self):



        nombre_sala = self.entrada.get()
        sala = self.admin_salones.obtener_salon_por_nombre(nombre_sala)

        if sala:
            self.mostrar_informacion_sala(sala)
        else:
            self.mostrar_mensaje_error("Sala no encontrada.")

    def mostrar_mensaje_error(self, mensaje):
        messagebox.showerror("Error", mensaje)     

    def mostrar_informacion_sala(self, sala): 
            # self.root.withdraw()

            ventana_info_sala = tk.Toplevel()

            self.ventana_info_sala = ventana_info_sala
            self.ventana_info_sala.config(bg="white")

            self.ventana_info_sala.resizable(height=0, width=0)
            self.ventana_info_sala.config(bd=0)



            ventana_info_sala.geometry("1900x900")
            ventana_info_sala.title(f"Información de la Sala: {sala.nombre}")

                # Carga la imagen usando Pillow
            imagen_path = 'busca2.png'  # Cambia esto a la ruta de tu imagen
            imagen = Image.open(imagen_path)
            imagen = imagen.resize((500, 500))
            self.imagen_tk = ImageTk.PhotoImage(imagen)  # Mantén la referencia

                # Etiqueta para mostrar la imagen
            etiqueta_imagen = tk.Label(ventana_info_sala, image=self.imagen_tk)
            etiqueta_imagen.place(x=200, y=100)


        #logica para el nombre del usuario

            self.image_path5 = 'userp.png' 
            self.img5 = self.load_thumbnail(self.image_path5, (50, 50))
            self.label_img5 = ttk.Label(ventana_info_sala, image=self.img5, background="#fff")
            self.label_img5.place(x=10,y=10)

            titulo_salon = tk.Label(ventana_info_sala, text=f"{sala.nombre}", fg="blue", bg="white",
                                    font=("times", 30, "bold"))
            titulo_salon.place(x=830,y=80)

            etiqueta_nombre = tk.Label(ventana_info_sala, text=f"Nombre: {sala.nombre}", fg="black", bg="white",
                                    font=("times", 30, "bold"))

            etiqueta_ = tk.Label(ventana_info_sala, text=f"___________________", fg="black", bg="white",
                                    font=("times", 30, "bold"))
            etiqueta_.place(x=810,y=165)

            etiqueta_ubicacion = tk.Label(ventana_info_sala, text=f"CEDESARROLLO", fg="black", bg="white",
                                    font=("times", 30, "bold"))
            etiqueta_ubicacion.place(x=830,y=150)



            if sala.ruta:
                etiqueta_ruta = tk.Label(ventana_info_sala, text=f"Ruta: {sala.ruta}", fg="black", bg="white",
                                        font=("times", 30, "bold"))


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

            self.route_names = {


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



            self.current_route_index = 0
            self.current_image_index = 0
#entry para rutassssssss
            self.dte_label = tk.Label(ventana_info_sala,text="Punto de partida",fg="#222feb", bg="white", font=("Microsoft YaHei UI Light ", 25, "bold"))
            self.dte_label.place(x=865,y=250)
            self.route_name_entry = tk.Entry(ventana_info_sala, width=40, font=('Helvetica', 12))
            self.route_name_entry.place(x=815, y=310)




            self.get_images_button = tk.Button(ventana_info_sala, width=60, height=2,text="Mostrar ruta", command=self.get_images, bg="#222feb", fg="white", border=0)
            self.get_images_button.place(x=800,y=480)

            self.hoarios_button = tk.Button(ventana_info_sala, width=60, height=2,text="Horario de disponibilidad", command=functools.partial(self.abrir_ventana_horario, sala), bg="#222feb", fg="white", border=0)
            self.hoarios_button.place(x=800,y=535)

            image1 = Image.open("regresar44.png")
            image1.thumbnail((80, 80))
            self.photo1 = ImageTk.PhotoImage(image1)
            self.bregresar = tk.Button(ventana_info_sala, image=self.photo1, command=self.regresar, border=0)
            self.bregresar.place(x=10, y=600)



            self.image_label = None  # Inicializar el atributo de la etiqueta de la imagen
            self.combobox = tk.Listbox(ventana_info_sala, width=60, height=6)
            self.combobox.place(x=815,y=330)


            #este es pa seleccionar 
            self.combobox.bind("<ButtonRelease-1>", self.on_combobox_select)
            self.route_name_entry.bind("<KeyRelease>", lambda event: self.update_autocomplete_options2())

    def abrir_ventana_horario(self, sala):
        if sala:
            ventana_horario = VentanaHorario(sala)
        self.root.withdraw()

    def update_autocomplete_options2(self):

        texto_ingres = self.entrada.get()
        #piso 1
        if texto_ingres == "D101":
            salond101 = db.reference("/Salones/D101")


            salon_d101 = salond101.get()
            for a in salon_d101.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "C101":
            salon = db.reference("/Salones/C101")


            salones = salon.get()
            for b in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in b if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)
        elif texto_ingres == "C102":
            salon = db.reference("/Salones/C102")


            salones = salon.get()
            for b in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in b if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)
        elif texto_ingres == "C104":
            salon = db.reference("/Salones/C104")


            salones = salon.get()
            for b in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in b if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)
        elif texto_ingres == "C105":
            salon = db.reference("/Salones/C105")


            salones = salon.get()
            for b in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in b if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "D102":
            salon = db.reference("/Salones/D102")


            salones = salon.get()
            for b in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in b if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "D103":
            salon = db.reference("/Salones/D103")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "D104":
            salon = db.reference("/Salones/D104")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    

        elif texto_ingres == "D105":
            salon = db.reference("/Salones/D105")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)  


        elif texto_ingres == "Auditorio":
            salon = db.reference("/Salones/Auditorio")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)  


        elif texto_ingres == "Bienestar estudiantil":
            salon = db.reference("/Salones/Bienestar Estudiantil")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)  

        elif texto_ingres == "Parqueadero":
            salon = db.reference("/Salones/Parqueadero")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "Zona verde":
            salon = db.reference("/Salones/Zona Verde")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)  

        elif texto_ingres == "Centro de fotocopiado":
            salon = db.reference("/Salones/Centro de Fotocopiado")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 


        elif texto_ingres == "A101":
            salon = db.reference("/Salones/A101")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    

        elif texto_ingres == "A102":
            salon = db.reference("/Salones/A102")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    

        elif texto_ingres == "A103":
            salon = db.reference("/Salones/A103")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)   

        elif texto_ingres == "A104":
            salon = db.reference("/Salones/A104")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    

        elif texto_ingres == "C201":
            salon = db.reference("/Salones/C201")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 

        elif texto_ingres == "C202":
            salon = db.reference("/Salones/C202")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 


        elif texto_ingres == "C203":
            salon = db.reference("/Salones/C203")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 

        elif texto_ingres == "C204":
            salon = db.reference("/Salones/C204")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    


        elif texto_ingres == "C301":
            salon = db.reference("/Salones/C301")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    


        elif texto_ingres == "C302":
            salon = db.reference("/Salones/C302")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    



        elif texto_ingres == "C303":
            salon = db.reference("/Salones/C303")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    


        elif texto_ingres == "C304":
            salon = db.reference("/Salones/C304")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    



        elif texto_ingres == "D301":
            salon = db.reference("/Salones/D301")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)    


        elif texto_ingres == "D302":
            salon = db.reference("/Salones/D302")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 


        elif texto_ingres == "D303":
            salon = db.reference("/Salones/D303")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 



        elif texto_ingres == "F301":
            salon = db.reference("/Salones/F301")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 

        elif texto_ingres == "F302":
            salon = db.reference("/Salones/F302")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "F303":
            salon = db.reference("/Salones/F303")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "F304":
            salon = db.reference("/Salones/F304")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "D401":
            salon = db.reference("/Salones/D401")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "D402":
            salon = db.reference("/Salones/D402")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "D403":
            salon = db.reference("/Salones/D403")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "F401":
            salon = db.reference("/Salones/F401")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "F402":
            salon = db.reference("/Salones/F402")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "F403":
            salon = db.reference("/Salones/F403")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "F404":
            salon = db.reference("/Salones/F404")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)



        elif texto_ingres == "C401":
            salon = db.reference("/Salones/C401")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "C402":
            salon = db.reference("/Salones/C402")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "C403":
            salon = db.reference("/Salones/C403")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "C404":
            salon = db.reference("/Salones/C404")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "F501":
            salon = db.reference("/Salones/F501")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "F502":
            salon = db.reference("/Salones/F502")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "F503":
            salon = db.reference("/Salones/F503")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)



        elif texto_ingres == "F504":
            salon = db.reference("/Salones/F504")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "F505":
            salon = db.reference("/Salones/F505")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "D501":
            salon = db.reference("/Salones/D501")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "D502":
            salon = db.reference("/Salones/D502")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "D503":
            salon = db.reference("/Salones/D503")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "C601":
            salon = db.reference("/Salones/C601")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "C602":
            salon = db.reference("/Salones/C602")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "C603":
            salon = db.reference("/Salones/C603")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)


        elif texto_ingres == "C604":
            salon = db.reference("/Salones/C604")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "Cafetería segundo piso":
            salon = db.reference("/Salones/Cafeteria 2 piso")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion)

        elif texto_ingres == "Cafetería sexto piso":
            salon = db.reference("/Salones/Cafeteria 6 piso")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 

        elif texto_ingres == "Enfermería":
            salon = db.reference("/Salones/Enfermeria")


            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 

        elif texto_ingres == "Sala de profesores":
            salon = db.reference("/Salones/Sala de profesores")
            salones = salon.get()
            for a in salones.values():
                query = self.route_name_entry.get()       
                autocomplete_options = [option for option in a if query.lower() in option.lower()]
                self.combobox.delete(0, tk.END)
                for suggestion in autocomplete_options:
                    self.combobox.insert(tk.END, suggestion) 

    def on_combobox_select(self, event):
        selected_item = self.combobox.get(self.combobox.curselection())
        self.route_name_entry.delete(0, tk.END)
        self.route_name_entry.insert(0, selected_item)

    def get_images(self):
            route_name = self.route_name_entry.get()
            if route_name in self.route_names.values():
                self.current_route_index = list(self.route_names.values()).index(route_name)
                self.show_images_window()
            else:
                tk.messagebox.showerror("Error", "Nombre de ruta no encontrado.")

    def show_images_window(self):
            images_window = tk.Toplevel(self.root)
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
            self.image1 = self.load_and_resize_image("igg1.png", (50, 50))
            self.image2 = self.load_and_resize_image("igg33.png", (50, 50))

            # Crea el botón con la primera imagen
            self.button = tk.Button(images_window, image=self.image1, command=self.toggle_button)
            self.button.image = self.image1
            self.button.place(x=10,y=10)




    def toggle_button(self):
        if self.button_state == 0:
            self.button.config(image=self.image2)
            self.button_state = 1
            self.guardar_ruta()

        else:
            self.button.config(image=self.image1)
            self.button_state = 0
            self.administracion()



    def load_and_resize_image(self, filename, size):
                img = Image.open(filename)
                img.thumbnail(size)
                return ImageTk.PhotoImage(img)


    def guardar_ruta(self):
        usuarios_ref = db.reference("/Registrados")
        usuarios_snapshot = usuarios_ref.get()

        for usuario_id in usuarios_snapshot:
            self.usuario_actual2 = usuario_id         

        ruta = self.route_name_entry.get()
        if ruta:
            ruta_ref = db.reference(f"/RutasGuardadas/{self.usuario_actual2}")

            rutas_snapshot = ruta_ref.get()
            if rutas_snapshot:
                rutas_lista = list(rutas_snapshot.values())
                if ruta in rutas_lista:
                    messagebox.showinfo("Ruta Existente", "Ya guardaste esta ruta.")
                    return  


            ruta_ref.push().set(ruta)

 
            print("SI", self.usuario_actual2)
        
 













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

    def regresar(self):
        self.root.deiconify()  
        self.ventana_info_sala.destroy()


def obtener_admin_salones():
    admin_salones = AdministradorSalones()

     #piso 1
    opciones_d101 = ["D101"]
    opciones_d102 = ["D102"]
    opciones_d103 = ["D103"]
    opciones_d104 = ["D104"]
    opciones_d105 = ["D105"]

    opciones_c101 = ["C101"]
    opciones_c102 = ["C102"]
    opciones_c103 = ["C105"]
    opciones_c104 = ["C104"]
    opciones_c105 = ["C105"]

    opciones_a101 = ["A101"]
    opciones_a102 = ["A102"]
    opciones_a103 = ["A102"]
    opciones_a104 = ["A103"]

    #piso 2

    opciones_c201 = ["C201"]
    opciones_c202 = ["C202"]
    opciones_c203 = ["C203"]
    opciones_c204 = ["C204"]

    #piso 3
    opciones_c301 = ["C301"]
    opciones_c302 = ["C302"]
    opciones_c303 = ["C303"]
    opciones_c304 = ["C304"]


    opciones_d301 = ["D301"]
    opciones_d302 = ["D302"]
    opciones_d303 = ["D303"]

    opciones_f301 = ["F301"]
    opciones_f302 = ["F302"]
    opciones_f303 = ["F303"]
    opciones_f304 = ["F304"]

    #piso 4

    opciones_d401 = ["D401"]
    opciones_d402 = ["D402"]
    opciones_d403 = ["D403"]

    opciones_f401 = ["F401"]
    opciones_f402 = ["F402"]
    opciones_f403 = ["F403"]
    opciones_f404 = ["F404"]

    opciones_c401 = ["C401"]
    opciones_c402 = ["C402"]
    opciones_c403 = ["C403"]
    opciones_c404 = ["C404"]

    #piso 5

    opciones_f501 = ["F501"]
    opciones_f502 = ["F502"]
    opciones_f503 = ["F503"]
    opciones_f504 = ["F504"]
    opciones_f505 = ["F505"]

    opciones_d501 = ["D501"]
    opciones_d502 = ["D502"]
    opciones_d503 = ["D503"]
    opciones_d504 = ["D504"]

    #piso 6
    opciones_C601 = ["C601"]
    opciones_c602 = ["C602"]
    opciones_c603 = ["C603"]
    opciones_c604 = ["C604"]
    opciones_Zona_verde = ["Zona verde"]

    opciones_Parqueadero = ["Parqueadero"]

    opciones_Auditorio = ["Auditorio"]
    opciones_Cafeteria_segundo_piso = ["Cafeteria segundo piso"]
    opciones_Cafeteria_sexto_piso = ["Cafeteria sexto piso"]
    opciones_enfermeria = ["Enfermería "]
    opciones_Bienestar_estudiantil =  ["Bienestar Estudiantil"]
    opciones_Centro_fotocopiado = ["Centro de fotocopiado"]
    opciones_Sala_de_profesores = ["Sala de profesores"]


    #lugares especiales 
    admin_salones.agregar_salon("Zona verde","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_Zona_verde)
    admin_salones.agregar_salon("Parqueadero","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_Parqueadero)
    admin_salones.agregar_salon("Auditorio","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_Auditorio)
    admin_salones.agregar_salon("Cafetería segundo piso","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_Cafeteria_segundo_piso)
    admin_salones.agregar_salon("Cafetería sexto piso","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_Cafeteria_sexto_piso)
    admin_salones.agregar_salon("Enfermería","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_enfermeria)
    admin_salones.agregar_salon("Bienestar Estudiantil","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_Bienestar_estudiantil)

    admin_salones.agregar_salon("Centro de fotocopiado","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_Centro_fotocopiado)
    admin_salones.agregar_salon("Sala de profesores","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_Sala_de_profesores)





#piso 1
    admin_salones.agregar_salon("D101", "Edificio A", "Ruta 1", "Referencia 1", opciones_d101)
    admin_salones.agregar_salon("D102", "Edificio PEPEPEPE", "Ruta 2", "Referencia 77", opciones_d102)
    admin_salones.agregar_salon("D103","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_d103) 
    admin_salones.agregar_salon("D104","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_d104)
    admin_salones.agregar_salon("D105","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_d105)




    admin_salones.agregar_salon("C101","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c101)
    admin_salones.agregar_salon("C102","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c102)
    admin_salones.agregar_salon("C103","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c103)
    admin_salones.agregar_salon("C104","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c104)
    admin_salones.agregar_salon("C105","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c105)

    admin_salones.agregar_salon("A101","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_a101)
    admin_salones.agregar_salon("A102","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_a102)
    admin_salones.agregar_salon("A103","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_a103)
    admin_salones.agregar_salon("A104","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_a104)


    #piso 2
    admin_salones.agregar_salon("C201","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c201)
    admin_salones.agregar_salon("C202","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c202)
    admin_salones.agregar_salon("C203","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c203)
    admin_salones.agregar_salon("C204","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c204)

    #piso 3
    admin_salones.agregar_salon("C301","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c301)
    admin_salones.agregar_salon("C302","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c302)
    admin_salones.agregar_salon("C303","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c303)
    admin_salones.agregar_salon("C304","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c304)

    admin_salones.agregar_salon("D301", "Edificio A", "Ruta 1", "Referencia 1", opciones_d301)
    admin_salones.agregar_salon("D302", "Edificio PEPEPEPE", "Ruta 2", "Referencia 77", opciones_d302)
    admin_salones.agregar_salon("D303","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_d303) 

    admin_salones.agregar_salon("F301","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f301)
    admin_salones.agregar_salon("F302","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f302)
    admin_salones.agregar_salon("F303","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f303)
    admin_salones.agregar_salon("F304","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f304)

    #piso 4

    admin_salones.agregar_salon("D401","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_d401)
    admin_salones.agregar_salon("D402","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_d402)
    admin_salones.agregar_salon("D403","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_d403)

    admin_salones.agregar_salon("F401","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f401)
    admin_salones.agregar_salon("F402","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f402)
    admin_salones.agregar_salon("F403","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f403)
    admin_salones.agregar_salon("F404","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f404)

    admin_salones.agregar_salon("C401","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c401)
    admin_salones.agregar_salon("C402","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c402)
    admin_salones.agregar_salon("C403","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c403)
    admin_salones.agregar_salon("C404","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c404)


    #piso 5

    admin_salones.agregar_salon("F501","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f501)
    admin_salones.agregar_salon("F502","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f502)
    admin_salones.agregar_salon("F503","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f503)
    admin_salones.agregar_salon("F504","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f504)
    admin_salones.agregar_salon("F505","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_f505)

    admin_salones.agregar_salon("D501", "Edificio A", "Ruta 1", "Referencia 1", opciones_d501)
    admin_salones.agregar_salon("D502", "Edificio PEPEPEPE", "Ruta 2", "Referencia 77", opciones_d502)
    admin_salones.agregar_salon("D503","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_d503) 
    admin_salones.agregar_salon("D504","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_d504) 


    #piso 6
    admin_salones.agregar_salon("C601","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_C601)
    admin_salones.agregar_salon("C602","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c602)
    admin_salones.agregar_salon("C603","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c603)
    admin_salones.agregar_salon("C604","Edificio PEPEPEPE", "Ruta 3", "Referencia 77", opciones_c604)



    return admin_salones

if __name__ == "__main__":
    firebase_sdk2 = credentials.Certificate("mapping-1a38f-firebase-adminsdk-8nf6d-117e271815.json")
    firebase_admin.initialize_app(firebase_sdk2, {"databaseURL": "https://mapping-1a38f-default-rtdb.firebaseio.com/"})
    admin_salones = obtener_admin_salones()
    root = tk.Tk()
    usuario_actual = "nombre_usuario"
    app = AplicacionBusquedaSalas(root, admin_salones, usuario_actual)

    root.mainloop()


