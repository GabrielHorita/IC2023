print("O codigo pode analisar tres numeros distintos e te dizer qual e o maior impar ,e se caso nao houver, ele tambem lhe dira")


x = int(input("Digite um valor para a variavel X e depois confirme: "))
y = int(input("Digite um valor para a variavel Y e depois confirme: "))
z = int(input("Digite um valor para a variavel Z e depois confirme: "))


#Quando nenhum numero impar foi adicionado na lista.
if x%2 == 0 and y%2 == 0 and z%2 == 0:
    print("Nenhum numero impar foi inserido. ")


#Quando apenas um numero impar foi adicionado na lista
elif x%2 != 0 and y%2 == 0 and z%2 ==0:
    print("O maior numero impar digitado foi= ", x,)
elif x%2 == 0 and y%2 != 0 and z%2 ==0:
    print("O maior numero impar digitado foi= ", y,)
elif x%2 == 0 and y%2 == 0 and z%2 !=0:
    print("O maior numero impar digitado foi= ", z,)

#Quando dois numeros impares foram adicionados na lista
elif x%2 != 0 and y%2 !=0 and z%2 ==0:
    if x > y:
        print("O valor de x=", x, "foi o maior impar inserido")
    else:
         print ("O valor de y=",x, "foi o maior impar inserido")
elif x%2 != 0 and y%2 ==0 and z%2 !=0:
    if x > z:
        print("O valor de x=", x, "foi o maior impar inserido")
    else:
        print("O valor de z=", z, "foi o maior impar inserido")

#Quando todos numeros sao impares.
elif x%2 == 0 and y%2 !=0 and z%2 !=0:
    if y > z:
        print("O valor de y=", y,"foi o maior impar inserido")
    else:
        print("O valor de z=", z, "foi o maior impar inserido")
elif x%2 != 0 and y%2 !=0 and z%2 !=0:
    if x>y and x>z:
        print("O valor de x=", x,"foi o maior impar inserido")
    elif y>z:
        print("O valor de y=", y, "foi o maior impar inserido")
    else:
        print("O valor de z=", z, "foi o maior impar inserido")
