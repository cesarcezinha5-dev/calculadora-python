calculadora.py

import math

print('Seja bem vindo a calculadora\n')
while True:
    try:
        n1=int(input("Digite o primeiro numero: "))
        n2=int(input("Digite o segundo numero: "))
    except ValueError:
        print("//ERRO\\ Por favor digite um numero\n")
        continue
    escolha=input('Escolha a operaçao que deseja:\n1-Adição\n2-Multiplicação\n3-Divisão\n4-Subtração\n5-Sair\n')
    if escolha == "adição" or escolha == "Adição" or escolha == "1":
        print("O resultado da adição é: ", n1+n2)
    elif escolha == "multiplicação" or escolha == "Multiplicação" or escolha == "2":
        print("O resultado da multiplicação é: ", n1*n2)
    elif escolha == "subtração" or escolha == "Subtração" or escolha == "3":
        print("O resultado da subtração é: ", n1-n2)
    elif escolha == "divisao" or escolha == "Divisão" or escolha == "4":
        print("O resultado da divisão é: ", n1/n2)
    elif escolha == "sair" or escolha == "Sair" or escolha == "5":
        print("Obrigado, saindo...")
        break
    else:
        print("error error error")
