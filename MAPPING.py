from tkinter import *
from ventana1 import Ventana1
from turtle import *
import pyttsx3

def decir_mensaje_voz(mensaje):
    engine = pyttsx3.init()
    engine.say(mensaje)
    engine.runAndWait()

def mostrar_ventana_tkinter():
    root = Tk()
    app = Ventana1(root)
    root.mainloop()

def efecto():
    window = Screen()
    window.setup(width=1.0, height=1.0)
    title("LOGO MAPPING")
    setup(width=1200, height=700)
    bgcolor("black")
    position()
    (0.00, 0.00)
    backward(170)
    position()
    (-30.00, 0.00)
    sety(70)
    setheading(0)
    fillcolor("darkblue")
    begin_fill()
    
    pensize(3)
    speed(4)
    pencolor("darkblue")
    forward(100)
    right(45)
    forward(100)
    left(90)
    forward(100)
    right(45)
    forward(100)
    right(90)
    forward(100)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    left(90)
    left(137)
    forward(100)
    right(90)
    forward(100)
    left(132)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    forward(100)
    end_fill()
    bye()


if __name__ == "__main__":
    mensaje_voz = "BIENVENIDOS A MAPPING, SEARCH YOU PLEIS "
    decir_mensaje_voz(mensaje_voz)

    efecto()

    mostrar_ventana_tkinter()
    