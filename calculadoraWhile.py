# Projeto Criar Calculadora com While. Eliakim Ramos. Turma 11
def calculadora(operacao, num1, num2):
    contador = 0
    while contador == 0:

        if operacao == 0:
            print("Você saiu do programa!") 
        elif operacao == 1:
            #Calculo da soma
            resultado = num1 + num2

        elif operacao == 2:
            #Calculo da subtracao
            resultado = num1 - num2

        elif operacao == 3:
            #Calculo da multiplicação 
            resultado = num1 * num2

        elif operacao == 4:
            #Calculo da divisão
            resultado = num1 / num2
        elif (operacao <0) or (operacao >4):
            print("Essa opção não existe!")
 
        print(f"Seu resultado foi: {resultado}")
        #continuar no programa ou sair do loop e do programa
        print("Deseja continuar? \nDigite a opção adequada: \n1-SIM\n2-NÃO")
        exitLoop = int(input())
        if exitLoop == 1:
            #condição criada para continuar o loop. 
            print("\n-+-+- Programa Calculadora -+-+-")
            operacao = int(input("Digite a sua operação:\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n0- Sair\n\n"))
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
        else:    
            contador = 1
            print("Você saiu do programa!") 
    
print("-+-+- Programa Calculadora -+-+-")
operacao = int(input("Digite a sua operação:\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n0- Sair\n\n"))
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

#chamando a função
calculadora(operacao, num1, num2)