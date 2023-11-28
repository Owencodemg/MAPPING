import tkinter as tk
import webbrowser

def abrir_sitio_web():
    url = "mapping-oficcial.netlify.app"  # Reemplaza con la URL que desees abrir
    webbrowser.open_new(url)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Apertura de Sitio Web")

# Crear un label
label = tk.Label(ventana, text="Presiona el botón para abrir el sitio web en Google Chrome")
label.pack(pady=10)

# Crear un botón
boton = tk.Button(ventana, text="Abrir Sitio Web", command=abrir_sitio_web)
boton.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
