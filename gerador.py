import random
import string

lista = ""
tamanho = input("Qual o tamanho da senha que deseja?")
for i in range(int(tamanho)):
    caractere = [random.choice(string.ascii_uppercase), random.choice(string.digits), random.choice(string.punctuation), random.choice(string.ascii_lowercase)]
    caractere = random.choice(caractere)
    lista = str(lista) + str(caractere)
print(lista)


