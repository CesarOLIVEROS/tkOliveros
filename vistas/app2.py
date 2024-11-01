## ejemplo de tkinter con grid
from tkinter import Tk, Button, Frame


ventana = Tk()
ventana.title("ejemplo 2 de frames")
ventana.geometry("400x200")


## frame  1
frm = Frame(ventana, bg="black")
frm.pack(expand= True, fill= "both")


## frame 2
frm1 = Frame(ventana, bg="white")
frm1.pack(expand= True, fill= "both")
frm1.config(cursor="heart")


##butom

redbutton = Button(frm, text="Rojo", fg="red", background="gray")
grenbutton = Button(frm, text="Verde", fg="green", background="gray")
bluebutton = Button(frm, text="Azul", fg="blue", background="gray")

## ubicacion boton
redbutton.place(relx=.05,rely=.05,relwidth=.25,relheight=.9)
grenbutton.place(relx=.35,rely=.05,relwidth=.25,relheight=.9)
bluebutton.place(relx=.65,rely=.05,relwidth=.25,relheight=.9)

blackbutton = Button(frm1, text="Negro", fg="white", background="black")
blackbutton.place(relx=.35,rely=.05,relwidth=.25,relheight=.9)



ventana.mainloop()

