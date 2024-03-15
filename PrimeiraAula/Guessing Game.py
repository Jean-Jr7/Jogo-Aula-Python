import random

print('*********************************************************')
print('    Seja Bem Vindo ao Jogo De Adivinhacao de numero')
print('*********************************************************')

numero_aleatorio = random.randint(1, 2)
acertou = False

while not acertou:
    numeroEscolhidoUsuario = int(input("Digite Seu numero: "))

    if numero_aleatorio == numeroEscolhidoUsuario:
        print('Voce acertou')
        acertou = True
    else:
        print('Voce Errou, Tente denovo:')
