# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
soma = 0

while True:
    numero = float(input("digite seus numeros: "))
    if numero == 0:
        break
    soma += numero

print("seu valor total:", soma)