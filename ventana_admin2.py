import tkinter as tk
from tkinter import *
import firebase_admin
from firebase_admin import credentials, db
from tkinter import messagebox
from PIL import Image, ImageTk


class VentanaAdmin2:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Admin 2")
        self.root.geometry("700x500")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg="#fff")


        self.label_inicio2 = tk.Label(self.root, text="                                                                                                                                                                                          ", fg="black", bg="black", font=("times", 15, "bold"))
        self.label_inicio2.place(x=0, y=0)
        self.label_inicio2 = tk.Label(self.root, text="                                                                                                                                                                     ", fg="black", bg="black", font=("times", 15, "bold"))
        self.label_inicio2.place(x=0, y=473)




        etiqueta_nombre = tk.Label(root, text="ADMINISTRADORES", fg="black", bg="white",
                                   font=("times", 15, "bold"))
        etiqueta_nombre.place(x=5, y=0)

        etiqueta_nombre2 = tk.Label(root, text="PROFESORES", fg="black", bg="white",
                                    font=("times", 15, "bold"))
        etiqueta_nombre2.place(x=295, y=0)

        etiqueta_nombre3 = tk.Label(root, text="ESTUDIANTES", fg="black", bg="white",
                                    font=("times", 15, "bold"))
        etiqueta_nombre3.place(x=525, y=0)






        # Listbox
        self.listbox1 = tk.Listbox(root, width=30)
        self.listbox1.place(x=10, y=119)

        self.listbox2 = tk.Listbox(root, width=30)
        self.listbox2.place(x=270, y=119)

        self.listbox3 = tk.Listbox(root, width=30)
        self.listbox3.place(x=500, y=119)

        # Entry
        self.entry1 = tk.Entry(root, width=30)
        self.entry1.place(x=10, y=100)

        self.entry2 = tk.Entry(root, width=30)
        self.entry2.place(x=270, y=100)

        self.entry3 = tk.Entry(root, width=30)
        self.entry3.place(x=500, y=100)

        # Configura la función para actualizar el Entry al seleccionar un elemento en la Listbox
        self.listbox1.bind('<<ListboxSelect>>', self.actualizar_entry1)
        self.listbox2.bind('<<ListboxSelect>>', self.actualizar_entry2)
        self.listbox3.bind('<<ListboxSelect>>', self.actualizar_entry3)

        # Configura la función para autocompletar el Entry en función de la entrada
        self.entry1.bind('<KeyRelease>', self.autocompletar_entry1)
        self.entry2.bind('<KeyRelease>', self.autocompletar_entry2)
        self.entry3.bind('<KeyRelease>', self.autocompletar_entry3)

        # Botones agregar y borrar
        self.boton_agregar_admin = tk.Button(self.root, text="AGREGAR", command=lambda: self.agregar_admin(root), width=10, height=2, bg="#222feb", fg="white", border=0)
        self.boton_agregar_admin.place(x=10, y=300)




        self.boton_agregar_profesor = tk.Button(self.root, text="AGREGAR", command=lambda: self.agregar_profesor(self.root), width=10, height=2, bg="#222feb", fg="white", border=0)
        self.boton_agregar_profesor.place(x=270, y=300)

        self.boton_agregar_estudiante = tk.Button(self.root, text="AGREGAR", command=lambda:self.agregar_estudiante(self.root), width=10, height=2, bg="#222feb", fg="white", border=0)
        self.boton_agregar_estudiante.place(x=500, y=300)

        self.boton_eliminar_admin = tk.Button(self.root, text="ELIMINAR", command=self.eliminar_admin, width=10, height=2, bg="red", fg="white", border=0)
        self.boton_eliminar_admin.place(x=120, y=300)

        self.boton_eliminar_profesor = tk.Button(self.root, text="ELIMINAR", command=self.eliminar_profesor, width=10, height=2, bg="red", fg="white", border=0)
        self.boton_eliminar_profesor.place(x=380, y=300)

        self.boton_eliminar_estudiante = tk.Button(self.root, text="ELIMINAR", command=self.eliminar_estudiante, width=10, height=2, bg="red", fg="white", border=0)
        self.boton_eliminar_estudiante.place(x=610, y=300)





    def agregar_admin(self, master):
        # Crea una nueva ventana

        nueva_ventana = tk.Toplevel(master)
        nueva_ventana.title("agregar admin")
        nueva_ventana.geometry("425x680")
        nueva_ventana.configure(bg="#fff")
        nueva_ventana.resizable(False, False)

        self.image_path = 'celu22.png'
        self.img = self.load_thumbnail(self.image_path, (800, 800))
        self.label_img = tk.Label(nueva_ventana, image=self.img, bg="#fff")
        self.label_img.place(x=0, y=0)

        # Espacios en blanco para tapar
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=270)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=290)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=370)

        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=40, y=350)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=360)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=430)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                                                                               ", bg="white")
        etiqueta_espacio.place(x=82, y=480)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                                                                                ", bg="white")
        etiqueta_espacio.place(x=82, y=470)

        # Guiones para debajo
        label_inicio2 = tk.Label(nueva_ventana, text="                                                                                                  ", fg="black", bg="black", font=("times", 30, "bold"))
        label_inicio2.place(x=2, y=650)
        label_inicio2 = tk.Label(nueva_ventana, text="                                                                                                  ", fg="black", bg="black", font=("times", 17, "bold"))
        label_inicio2.place(x=2, y=0)
        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=320)

        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=393)
        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=453)
        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=513)

        self.user1 = self.create_entry(nueva_ventana, "Nombre De Usuario", x=82, y=308)
        self.code_id1 = self.create_entry(nueva_ventana, "ID", x=82, y=380)
        self.code1 = self.create_entry(nueva_ventana, "Contraseña", x=82, y=440)
        self.code_confirm1 = self.create_entry(nueva_ventana, "Confirmar Contraseña", x=82, y=500)

        boton_guardar = tk.Button(nueva_ventana, width=18, pady=20, text="AGREGAR ADMIN", bg="#222feb", fg="white", border=0, command=self.guardar_informacion1)
        boton_guardar.place(x=150, y=560)
        etiqueta_rol = tk.Label(nueva_ventana, text="ADMIN",fg="black" ,bg="white",  font=("times", 30, "bold"))
        etiqueta_rol.place(x=140, y=250)

    def create_entry(self, master, default_text, x, y):
        entry = tk.Entry(master, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 15)) 
        entry.place(x=x, y=y)
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', lambda event, widget=entry, text=default_text: self.on_enter(event, widget, text))
        entry.bind('<FocusOut>', lambda event, widget=entry, text=default_text: self.on_leave(event, widget, text))

        return entry

    def guardar_informacion1(self):
        nombre_usuario = self.user1.get()
        user_id = self.code_id1.get()
        contraseña = self.code1.get()
        confirm_password = self.code_confirm1.get()

        if not nombre_usuario or not user_id or not contraseña or not confirm_password:
            messagebox.showwarning("Advertencia", "Por favor, llena todos los campos.")
        elif not user_id.isdigit():
            messagebox.showwarning("Advertencia", "El ID solo debe contener números.")
        elif contraseña != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
        else:
            ref = db.reference("/Registrados/Admin/")
            ref.push({"Usuario": nombre_usuario, "Contraseña": contraseña})
            messagebox.showinfo("Éxito", "¡Registro exitoso!")
            main()
    def on_enter(self, event, entry_widget, default_text):
        entry_widget.delete(0, 'end')

    def on_leave(self, event, entry_widget, default_text):
        name = entry_widget.get()
        if name == '':
            entry_widget.insert(0, default_text)


    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Maintain a reference to the image















    def agregar_profesor(self, master):
        nueva_ventana = tk.Toplevel(master)
        nueva_ventana.title("agregar profesor")
        nueva_ventana.geometry("425x680")
        nueva_ventana.configure(bg="#fff")
        nueva_ventana.resizable(False, False)



        self.image_path = 'celu22.png'
        self.img = self.load_thumbnail(self.image_path, (800, 800))
        self.label_img = tk.Label(nueva_ventana, image=self.img, bg="#fff")
        self.label_img.place(x=0, y=0)

        # Espacios en blanco para tapar
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=270)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=290)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=370)

        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=40, y=350)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=360)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=430)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                                                                               ", bg="white")
        etiqueta_espacio.place(x=82, y=480)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                                                                                ", bg="white")
        etiqueta_espacio.place(x=82, y=470)

        # Guiones para debajo
        label_inicio2 = tk.Label(nueva_ventana, text="                                                                                                  ", fg="black", bg="black", font=("times", 30, "bold"))
        label_inicio2.place(x=2, y=650)
        label_inicio2 = tk.Label(nueva_ventana, text="                                                                                                  ", fg="black", bg="black", font=("times", 17, "bold"))
        label_inicio2.place(x=2, y=0)
        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=320)

        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=393)
        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=453)
        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=513)

        self.user2 = self.create_entry(nueva_ventana, "Nombre De Usuario", x=82, y=308)
        self.code_id2 = self.create_entry(nueva_ventana, "ID", x=82, y=380)
        self.code2 = self.create_entry(nueva_ventana, "Contraseña", x=82, y=440)
        self.code_confirm2 = self.create_entry(nueva_ventana, "Confirmar Contraseña", x=82, y=500)

        boton_guardar = tk.Button(nueva_ventana, width=18, pady=20, text="AGREGAR PROFESOSR", bg="#222feb", fg="white", border=0, command=self.guardar_informacion2)
        boton_guardar.place(x=150, y=560)
        etiqueta_rol = tk.Label(nueva_ventana, text="PROFESOR",fg="black" ,bg="white",  font=("times", 30, "bold"))
        etiqueta_rol.place(x=100, y=250)

    def create_entry(self, master, default_text, x, y):
        entry = tk.Entry(master, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 15)) 
        entry.place(x=x, y=y)
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', lambda event, widget=entry, text=default_text: self.on_enter(event, widget, text))
        entry.bind('<FocusOut>', lambda event, widget=entry, text=default_text: self.on_leave(event, widget, text))

        return entry

    def guardar_informacion2(self):
        nombre_usuario = self.user2.get()
        user_id = self.code_id2.get()
        contraseña = self.code2.get()
        confirm_password = self.code_confirm2.get()

        if not nombre_usuario or not user_id or not contraseña or not confirm_password:
            messagebox.showwarning("Advertencia", "Por favor, llena todos los campos.")
        elif not user_id.isdigit():
            messagebox.showwarning("Advertencia", "El ID solo debe contener números.")
        elif contraseña != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
        else:
            ref = db.reference("/Registrados/Profesores/")
            ref.push({"Usuario": nombre_usuario, "Contraseña": contraseña})
            messagebox.showinfo("Éxito", "¡Registro exitoso!")
            main()

    def on_enter(self, event, entry_widget, default_text):
        entry_widget.delete(0, 'end')

    def on_leave(self, event, entry_widget, default_text):
        name = entry_widget.get()
        if name == '':
            entry_widget.insert(0, default_text)


    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Maintain a reference to the image






















    def agregar_estudiante(self, master):
        nueva_ventana = tk.Toplevel(master)
        nueva_ventana.title("agregar estudiante")
        nueva_ventana.geometry("425x680")
        nueva_ventana.configure(bg="#fff")
        nueva_ventana.resizable(False, False)



        self.image_path = 'celu22.png'
        self.img = self.load_thumbnail(self.image_path, (800, 800))
        self.label_img = tk.Label(nueva_ventana, image=self.img, bg="#fff")
        self.label_img.place(x=0, y=0)

        # Espacios en blanco para tapar
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=270)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=290)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=370)

        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=40, y=350)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=360)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                              ", bg="white")
        etiqueta_espacio.place(x=82, y=430)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                                                                               ", bg="white")
        etiqueta_espacio.place(x=82, y=480)
        etiqueta_espacio = tk.Label(nueva_ventana, text="                                                                                ", bg="white")
        etiqueta_espacio.place(x=82, y=470)

        # Guiones para debajo
        label_inicio2 = tk.Label(nueva_ventana, text="                                                                                                  ", fg="black", bg="black", font=("times", 30, "bold"))
        label_inicio2.place(x=2, y=650)
        label_inicio2 = tk.Label(nueva_ventana, text="                                                                                                  ", fg="black", bg="black", font=("times", 17, "bold"))
        label_inicio2.place(x=2, y=0)
        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=320)

        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=393)
        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=453)
        etiqueta_espacio = tk.Label(nueva_ventana, text="_________________________________________________", bg="black")
        etiqueta_espacio.place(x=82, y=513)

        self.user3 = self.create_entry(nueva_ventana, "Nombre De Usuario", x=82, y=308)
        self.code_id3 = self.create_entry(nueva_ventana, "ID", x=82, y=380)
        self.code3 = self.create_entry(nueva_ventana, "Contraseña", x=82, y=440)
        self.code_confirm3 = self.create_entry(nueva_ventana, "Confirmar Contraseña", x=82, y=500)

        boton_guardar = tk.Button(nueva_ventana, width=18, pady=20, text="AGREGAR ESTUDIANTE", bg="#222feb", fg="white", border=0, command=self.guardar_informacion)
        boton_guardar.place(x=150, y=560)
        etiqueta_rol = tk.Label(nueva_ventana, text="ESTUDIANTE",fg="black" ,bg="white",  font=("times", 30, "bold"))
        etiqueta_rol.place(x=75, y=250)

    def create_entry(self, master, default_text, x, y):
        entry = tk.Entry(master, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 15)) 
        entry.place(x=x, y=y)
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', lambda event, widget=entry, text=default_text: self.on_enter(event, widget, text))
        entry.bind('<FocusOut>', lambda event, widget=entry, text=default_text: self.on_leave(event, widget, text))

        return entry

    def guardar_informacion(self):
        nombre_usuario = self.user3.get()
        user_id = self.code_id3.get()
        contraseña = self.code3.get()
        confirm_password = self.code_confirm3.get()

        if not nombre_usuario or not user_id or not contraseña or not confirm_password:
            messagebox.showwarning("Advertencia", "Por favor, llena todos los campos.")
        elif not user_id.isdigit():
            messagebox.showwarning("Advertencia", "El ID solo debe contener números.")
        elif contraseña != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
        else:
            ref = db.reference("/Registrados/Estudiantes/")
            ref.push({"Usuario": nombre_usuario, "Contraseña": contraseña})
            messagebox.showinfo("Éxito", "¡Registro exitoso!")
            main()

    def on_enter(self, event, entry_widget, default_text):
        entry_widget.delete(0, 'end')

    def on_leave(self, event, entry_widget, default_text):
        name = entry_widget.get()
        if name == '':
            entry_widget.insert(0, default_text)


    def load_thumbnail(self, image_path, size):
        imagen = Image.open(image_path)
        imagen.thumbnail(size)
        return ImageTk.PhotoImage(imagen)  # Maintain a reference to the image









    def eliminar_admin(self):
        admin = self.entry1.get()
        usuarios_ref = db.reference("/Registrados/Admin/")
        usuarios_snapshot = usuarios_ref.get()
        
        if admin:
            encontrado = False  # Bandera para verificar si se encuentra al administrador
            for usuario_id, usuario_data in usuarios_snapshot.items():
                if usuario_data.get('Usuario') == admin:
                    a = usuario_id
                    respuesta = messagebox.askyesno("Advertencia", "¿Seguro que quieres eliminar a este administrador?")
                    if respuesta:
                        messagebox.showinfo("Admin eliminado", "El admin ha sido eliminado exitosamente.")
                        usuarios_ref.child(a).delete()
                        main()
                    encontrado = True  # Se encontró al administrador
                    break  # Terminar el bucle ya que se encontró al administrador
            
            if not encontrado:
                messagebox.showinfo("Error", "No se encontró al administrador")



    def eliminar_profesor(self):
        profe = self.entry2.get()
        usuarios_ref = db.reference("/Registrados/Profesores/")
        usuarios_snapshot = usuarios_ref.get()
        if profe:       
            for usuario_id, usuario_data in usuarios_snapshot.items():
                if usuario_data.get('Usuario') == profe:
                    a = usuario_id
                    respuesta = messagebox.askyesno("Advertencia", "¿Seguro que quieres eliminar a este profesor?")
                    if respuesta:
                        messagebox.showinfo("Profesor eliminado", "El profesor ha sido eliminado exitosamente.")
                        usuarios_ref.child(a).delete()
                        main()
                    else:
                        messagebox.showinfo("No se eliminó al profesor")

    def eliminar_estudiante(self):
        estu = self.entry3.get()
        usuarios_ref = db.reference("/Registrados/Estudiantes/")
        usuarios_snapshot = usuarios_ref.get()
        if estu:
            for usuario_id, usuario_data in usuarios_snapshot.items():
                if usuario_data.get('Usuario') == estu:
                    a = usuario_id
                    respuesta = messagebox.askyesno("Advertencia", "¿Seguro que quieres eliminar a este estudiante?")
                    if respuesta:
                            messagebox.showinfo("Estudiante eliminado", "El estudiante ha sido eliminado exitosamente.")
                            usuarios_ref.child(a).delete()
                            main()
                    else:
                            messagebox.showinfo("No se eliminó al estudiante")







    def autocompletar_entry1(self, event):
        texto_ingresado = self.entry1.get().lower()
        if texto_ingresado:
            usuarios_ref = db.reference("/Registrados/Admin/")
            usuarios_snapshot = usuarios_ref.get()
            for a in usuarios_snapshot.values():
                self.lista_usuarios1 = [usuario["Usuario"] for usuario in usuarios_snapshot.values() if "Usuario" in usuario and texto_ingresado.lower() in usuario["Usuario"].lower()]
                self.listbox1.delete(0, tk.END)
                for sugerencia in self.lista_usuarios1:
                    self.listbox1.insert(tk.END, sugerencia)

    def autocompletar_entry2(self, event):
        texto_ingresado = self.entry2.get().lower()
        if texto_ingresado:
            usuarios_ref = db.reference("/Registrados/Profesores/")
            usuarios_snapshot = usuarios_ref.get()

            self.lista_usuarios2 = [usuario["Usuario"] for usuario in usuarios_snapshot.values() if "Usuario" in usuario and texto_ingresado.lower() in usuario["Usuario"].lower()]

            self.listbox2.delete(0, tk.END)
            for sugerencia in self.lista_usuarios2:
                self.listbox2.insert(tk.END, sugerencia)


    def autocompletar_entry3(self, event):
        texto_ingresado = self.entry3.get().lower()
        if texto_ingresado:
            usuarios_ref = db.reference("/Registrados/Estudiantes/")
            usuarios_snapshot = usuarios_ref.get()
            for a in usuarios_snapshot.values():
                self.lista_usuarios3 = [usuario["Usuario"] for usuario in usuarios_snapshot.values() if texto_ingresado.lower() in usuario["Usuario"].lower()]

                self.listbox3.delete(0, tk.END)
                for sugerencia in self.lista_usuarios3:
                    self.listbox3.insert(tk.END, sugerencia)



    def actualizar_entry1(self, event):
        selected_index = self.listbox1.curselection()
        if selected_index:
            selected_user = self.lista_usuarios1[selected_index[0]]
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, selected_user)

    def actualizar_entry2(self, event):
        selected_index = self.listbox2.curselection()
        if selected_index:
            selected_user = self.lista_usuarios2[selected_index[0]]
            self.entry2.delete(0, tk.END)
            self.entry2.insert(0, selected_user)

    def actualizar_entry3(self, event):
        selected_index = self.listbox3.curselection()
        if selected_index:
            selected_user = self.lista_usuarios3[selected_index[0]]
            self.entry3.delete(0, tk.END)
            self.entry3.insert(0, selected_user)




def main():
    root = tk.Tk()
    app = VentanaAdmin2(root)
    root.mainloop()

if __name__ == "__main__":
    firebase_sdk = credentials.Certificate("mapping-1a38f-firebase-adminsdk-8nf6d-117e271815.json")
    firebase_admin.initialize_app(firebase_sdk, {"databaseURL": "https://mapping-1a38f-default-rtdb.firebaseio.com/"})
    main()
