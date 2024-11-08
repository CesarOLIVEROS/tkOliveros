

class Fraccion:

## Variables de clase
    # num = 2 
    # den = 3

## METODO CONSTRUCTOR
    def __init__(self, n, d):

## INICIALIZAR LAS VARIABLES
# PARA REFERIRSE A LAS VARIABLES DE CLASE SE LLAMAN SELF
        self.num = n
        self.den = d


# FORMATEO DEL RESULTADO
    def imprime(self):
        print(self.num, "/", self.den)

# MULTIPLICACION 
    def multiplicar(self, b):
        n = self.num * b.num
        d = self.den * b.den
        r = Fraccion(n,d)
        return r
    
# Método para sumar dos fracciones
    def sumar(self, b):
        # Para sumar fracciones, debemos tener el mismo denominador.
        n = (self.num * b.den) + (b.num * self.den)  # Sumar los numeradores
        d = self.den * b.den  # El denominador es el producto de los denominadores
        r = Fraccion(n, d)
        return r


 # Método para restar dos fracciones
    def restar(self, b):
        # Para restar fracciones, debemos tener el mismo denominador.
        n = (self.num * b.den) - (b.num * self.den)  # Restar los numeradores
        d = self.den * b.den  # El denominador es el producto de los denominadores
        r = Fraccion(n, d)
        return r

    # Método para dividir dos fracciones
    def dividir(self, b):
        # Para dividir fracciones, multiplicamos por el inverso de la segunda fracción
        n = self.num * b.den  # Numerador es el numerador de 'a' por el denominador de 'b'
        d = self.den * b.num  # Denominador es el denominador de 'a' por el numerador de 'b'
        r = Fraccion(n, d)
        return r

def main():
# SE LLAMA AL OBJETO Y SE LE PASASN LAS VARIABLES INICIALIZADAS
    a = Fraccion(3,2)
    a.imprime()

    b = Fraccion(7,4)
    b.imprime()

# DESDE a LLAMAN MULTIPLICAR POR b Y LO ALMACENAN EN r
    # Realizamos la multiplicación
    r_multiplicacion = a.multiplicar(b)
    #  Si no hubieras usado end="" y hubieras utilizado el 
    # comportamiento por defecto (que es end="\n"), 
    # la salida sería algo como:Si no hubieras usado end="" 
    # y hubieras utilizado el comportamiento por defecto (que es end="\n"),
    #  la salida sería algo como:
    # El resultado de la división es:
    # 12 / 14
    print("El resultado de la multiplicación es: ", end="")
    r_multiplicacion.imprime()

    # Realizamos la suma
    r_suma = a.sumar(b)
    print("El resultado de la suma es: ", end="")
    r_suma.imprime()

    # Realizamos la resta
    r_resta = a.restar(b)
    print("El resultado de la resta es: ", end="")
    r_resta.imprime()

    # Realizamos la división
    r_division = a.dividir(b)
    print("El resultado de la división es: ", end="")
    r_division.imprime()
if __name__=="__main__":
    main()