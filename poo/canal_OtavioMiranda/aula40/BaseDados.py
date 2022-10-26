from lib2to3.pytree import Base


class BaseDeDados:
    def __init__(self):
        self.__dados = {} #dic vazio
    
    @property
    def dados(self):
        return self.__dados
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)    
        
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]
    
    
bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.__dados = 'Outra coisa'
print(bd.__dados)
print(bd._BaseDeDados__dados) #para acessar realmente a classe
bd.apaga_cliente(2)
bd.lista_clientes()

#Se tentarmos modificar, por ex:
#bd.dados = 'Uma outra coisa'
#A classe toda quebra, dá erro em todos os métodos!