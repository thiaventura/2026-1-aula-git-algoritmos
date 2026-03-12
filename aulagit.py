num 1 = float(input("Digite o primeiro número: "))
op = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

If op == '+':
    resultado = num1 + num2
elif op == '-':
    resultado = num1 - num2
elif op == '*':
    resultado = num1 * num2
el if op == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero."
elsa:
    resultado = "Operação inválida"

print("Resultado:", resultado