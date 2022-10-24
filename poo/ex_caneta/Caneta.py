class Caneta:
    #Construtor:
    def __init__(self, m, c, t):
        self.marca = m
        self.cor = c
        self.t = t
    

    def escrever(self, texto):
        print(texto + "(na cor " + self.cor + ")")

#Exemplos são objetos:
exemplo1 = Caneta("Bic", "Vermelha", True)
exemplo2 = Caneta("Faber Castell", "Azul", False)

exemplo2.escrever("Hoje é um dia feliz.")
exemplo2.escrever("Bora")
exemplo1.escrever("RS")