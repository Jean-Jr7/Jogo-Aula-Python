import random

print('*********************************************************')
print('    Seja Bem Vindo ao Jogo De Adivinhacao de numero')
print('*********************************************************')

numero_aleatorio = random.randint(0, 100)

numeroEscolhidoUsuario = int(input("Digite Seu numero: "))

if numero_aleatorio == numeroEscolhidoUsuario:
    print('Voce acertou')
else:
    print('Voce Errou. O número correto era:', numero_aleatorio)
