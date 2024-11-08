class Lampara :
    ESTADOS = ['''
            .
      .     |   .
          ;    ;
    --- (       ) ---
          |___|
    ''',
    '''
        ,-.
       (   )
        |_|
    ''']

    ## iniciamos el constructor
    def __init__(self, esta_encedida):
        self.esta_encendida = esta_encedida

    ## Imprime lampara de acuerdo al atributo recibido en el llamado del objeto
    def muestra_Lampara(self):
        if self.esta_encendida == True:
            print(self.ESTADOS[0])
        else:
            print(self.ESTADOS[1])

    # Enciende lampara 
    def encender_lampara(self):
        self.esta_encendida == True
        self.muestra_Lampara()
        
    ## Apagar lmpara
    def apagar_lampara(self):
        self.esta_encendida == False
        self.muestra_Lampara()


def main():
    a = Lampara(False)
    a.muestra_Lampara()


if __name__ == "__main__":
    main()