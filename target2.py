def pertence_fibonacci(n):
    if n < 0:
        return False  # Números negativos não pertencem à sequência de Fibonacci

    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

while True:
    try:
        numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
        break
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
