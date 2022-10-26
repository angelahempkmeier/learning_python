import random

class Pessoa:
    ano_atual = 2022 

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
        #cls refere-se à classe, no caso, Pessoa
    
    @staticmethod
    def gera_id():
        rand = random.randint(10000, 19999)
        return rand

#versão 1 - usando o método de instância
p1 = Pessoa('João', 25)
print(p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
#também é possível fazer do jeito da pessoa 2

#agora, criando uma pessoa em determinado ano de nascimento
p2 = Pessoa.por_ano_nascimento('Angela', 1995)
print(p2.idade)
p2.get_ano_nascimento()
print(p2.gera_id())
