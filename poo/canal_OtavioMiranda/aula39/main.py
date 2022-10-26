class A:
    vc = 123


a1 = A()
a2 = A()
a3 = A()

#a3.vc = 321 #estamos criando um novo vc com o valor 321

#Para mudar todos os valores vc de todas as instâncias:
A.vc = 'Alterado'

print(a1.vc)
print(a2.vc)
print(a3.vc)