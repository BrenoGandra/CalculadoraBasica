print("Bem-vindo(a)!\n")
print("Com esta calculadora você poderá efetuar cálculos básicos entre 2 números!\n")

while True:
    print("\nEscolha um tipo de operador para começar a calcular!")
    print("\n soma (+) \n subtração (-) \n divisão (/) \n multiplicação (*) \n ou digite (sair) para encerrar o programa.")


    operador = input("Digite o operador desejado: ")
    
    if operador.lower() == 'sair':
       print("Encerrando programa...")
       break
    
    if operador not in ['+', '-', '*', '/']:
       print("Você digitou um valor incorreto. Tente novamente.")
       continue
    
    primeiroNum = float(input("Digite um primeiro numero:"))
    segundoNum = float(input("Digite um segundo numero:"))

    if operador == '+':
       resultado = primeiroNum + segundoNum
       print("Você escolheu a adição!")
       

    elif operador == '-':
       resultado = primeiroNum - segundoNum
       print("Você escolheu a subtração!")
 
    elif operador == '/':
       if segundoNum != 0:
           resultado = primeiroNum / segundoNum  
           print("Você escolheu a divisão!") 
           
       else:
          resultado = "Não é possível dividir por zero."

    elif operador == '*':
       resultado = primeiroNum * segundoNum
       print("Você escolheu a multiplicação!")
       
    print(f'O resultado da sua conta é: {resultado}\n')  

