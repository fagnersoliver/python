print("################################")
print("Bem vindo ao jogo de Adivinhação!")
print("################################")

numero_secreto = 42

chute = input("Digite um numero: ")
print("Você digitou ", chute)

if(numero_secreto == int(chute)):
    print("e você acertou")
else:
    print("e você Errou")