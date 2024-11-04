class fraccion:

    ## declarar variables de clases
    ## pero si se desea al inicializarse con self no se necesitan crear 
    #numerador = 2
    #denominador = 3

    ## declarar constructor que siempre lleva self,
    # pasamos la funcion que sea e inicializamos los atributos a pasarle
    ## darle un valor inicial a las variables del constructor
    ## al usar self accedemos a las variables de clase no del constructor
    def __init__(self,  numerador, denominador):
        # inicializa el objeto antes recibidos y da varlor a las variables de clase 
        ## volviendolas accesibles desde cualquier lugar
        self.numerador = numerador
        self.denominador = denominador
        print("constructor")
        
    def imprime(self):
        print(self.numerador, "/", self.denominador)

    def multiplicar(self, b):
        # aca se llamo con self A: a y se multiplico por b
        n = self.numerador * b.numerador
        d = self.denominador * b.denominador
        r = fraccion(n,d)
        return r 



## apartir de la creacion de la clase anterior e inicializacion de los atributos o variables
## se da por entendido que se podran crear multiples objetos con los mismos atributos

def main():
    ## aca se llama a la clase y a su constructor pasandole todos los atributos q
    # trae consigo creando un nuevo objeto con todos sus atributos
   
    a = fraccion(5,2)
    a.imprime()
    # aca accedemos al objeto creado anteriormente y se le llama al
    # metodo imprime creado anteriormente
    
    b = fraccion(2,3)
    b.imprime()

    ## al llamar al objeto a y usar self se llama asi mismo al objeto a para que
    # que multiplique por el objeto b
    r = a.multiplicar(b)
    r.imprime()

if __name__ == "__main__":
    main()

