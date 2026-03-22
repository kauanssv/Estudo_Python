n1 = float(input("Digite um numero\n"))
n2 = float(input("Digite outro numero\n"))
op = str(input("Escolha uma operacao: + - * /\n"))

if(op == "+"):
    r = n1 + n2
    print("O resultado é: ",r)
elif(op == "-"):
    r = n1 - n2
    print("O resultado é: ",r)
elif(op == "*"):
     r = n1 * n2
     print("O resultado é: ",r)
elif(op == "/"):
     r = n1 / n2
     print("O resultado é: ",r)
else:
     print("ERRO")