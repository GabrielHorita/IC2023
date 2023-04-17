#Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it should print a message to that effect.
M_Impar = None

for i in range(10):
    number = int(input("Escreva alguns numeros inteiros. "))
    if number % 2 == 1:
        if M_Impar is None or number > M_Impar:
            M_Impar = number

if M_Impar is None:
    print("Nenhum numero impar foi digitado anteriormente.")
else:
    print("o maior impar", M_Impar)