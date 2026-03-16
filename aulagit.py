num1 = float(input("Digite o primeiro número: "))
op = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if op == '+':
    resultado = num1 + num2
elif op == '-':
    resultado = num1 - num2
elif op == '*':
    resultado = num1 * num2
elif op == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero."
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)
