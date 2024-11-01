import tkinter as tk
from tkinter import *

def miFuncion():
    print("MENSAJE DEL BOTON")

# iniciamos la ventana 
ventana = Tk()
#carateristicas de la ventana
ventana.title("Hola que tal")
ventana.geometry("400x200")

# creacion de un label 
lbl = tk.Label(ventana, text="Este es un label" )
# empaquetado para mostrar el label dentro de la ventana creada
lbl.pack()

# boton agregado
btn = Button(ventana,  text= "presionar", bg="red", fg="blue", command=miFuncion)
btn.pack()



# TRES FORMAS DE CONFIGURAR LOS WIDGTES
# constructor:
# miBoton = Button(self, fg="red", bg="blue")

# config
# miBoton.config(fg="red", bg ="blue")

# accesando  a la propiedad ( como un diccionario clave / valor)
# miBoton["fg"] = "red"
# miBoton["bg"] = "blue"

ventana.mainloop()