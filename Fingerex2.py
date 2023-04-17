#("Finger exercise: Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it should print a message to that effect.")

while True:
    try:
        numXs = int(input('Digite o numero de vezes que devo digitar a tecla X: '))
        break
    except ValueError:
        print('Digite um NUMERO.')
toPrint = ''
count = 0
while count < numXs:
    toPrint += 'X'
    count += 1
print(toPrint)
