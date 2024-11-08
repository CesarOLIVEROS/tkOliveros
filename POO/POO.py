from tkinter import Tk, Button, Frame, Entry, Label

## clase master 

class MyVentana(Frame):

    ## creamos el constructor de la clase

    def __init__(self, master = None):
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.CrearWidtgets()


    ## funcion suma que recibe self extrae los datos con get, hace la operacion,
    ## borra los datos existentes e inserta los resultados nuevos
    def suma(self):
        n1 = self.txtNum1.get()
        n2 = self.txtNum2.get()
        r = float(n1) + float(n2)
        self.txtNum3.delete(0, 'end')
        self.txtNum3.insert(0, r)


    ## se crean y posicionan todos los widgets
    def CrearWidtgets(self):
        self.lbl1 = Label(self, text="primer numero: ", bg="yellow")
        self.txtNum1 = Entry(self, bg = "pink")
        
        self.lbl2 = Label(self, text="segundo numero: ", bg="yellow")
        self.txtNum2 = Entry(self, bg = "pink")

        self.btn1 = Button(self, text="Sumar", command=self.suma)

        self.lbl3 = Label(self, text="Resultado ", bg="yellow")
        self.txtNum3 = Entry(self, bg = "cyan")

        # Usar "x" y "y" en minúsculas 
        self.lbl1.place(x = 10, y = 10, width=100, height = 30)
        self.txtNum1.place(x = 120, y = 10, width=100, height = 30)

        self.lbl2.place(x = 10, y = 50, width=100, height = 30)
        self.txtNum2.place(x = 120, y = 50, width=100, height = 30)

        self.btn1.place(x = 230, y = 50, width=80, height=30)

        self.lbl3.place(x = 10, y = 120, width=100, height = 30)
        self.txtNum3.place(x = 120, y = 120, width=100, height = 30)


## creacion de ventana

root = Tk()
# forma de indicar un titulo a la ventana o clase
root.wm_title("Suma de numeros")
# se llama la clase para crear el frame
app = MyVentana(root)

# inicio de ciclo de ocurrencias del nuevo objeto creado
app.mainloop()
