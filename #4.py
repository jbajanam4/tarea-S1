#Ejercicio 11:
#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.
valor = input("Ingrese la cantidad del numero entero: ")
while int(valor) <= 0:
    print("El el numero debe ser positivo")
    valor = input("Ingrese la cantidad del numero entero: ")
suma = 0
for i in range (1, int(valor) + 1):
    cuadrado = i * i
    suma = suma + cuadrado
print("La suma de cuadrado es:", suma)


#Ejercicio 12:
# se desean escribir los números del 1 al 100
x = 0
while x <= 100:
    x = x + 1
    print(x)


#Ejercicio 13:
#calcular la suma y producto de N números enteros
#utilizando un bucle controlado por el usuario.
suma = 0
acum = 0
while True:
    usuario = input("Escriba 's' continuar, 'n'para cancelar: ")
    if(usuario == "s"):
        num = input("Ingrese un numero: ")   
        suma = suma + int(num)
        acum = acum + 1 
    elif (usuario == "n"):
        break
if (suma > 0):
    print("La suma es: ",suma)
    print("Las veces ingresados son: ", acum)
else:
    print("Usted a salido")


#Ejercicio 14:
# calcular la suma y producto de N números enteros, 
#utilizando un bucle controlado por centinela.
suma = 0
acum = 0
centinela = input("Ingrese un valor centiela: ")
print(centinela)
while True:
    num = input("Ingrese un numero: ")
    if (int(num) == int(centinela)):
        break
    elif int(num) != int(centinela):
        suma = suma + int(num)
        acum = acum + 1 
if (suma > 0):
    print("La suma es: ",suma)
    print("Las veces ingresados son: ", acum)
else:
    print("Usted a salido")


#Ejercicio 15:
# Determinar si un número entero proporcionado por el usuario es primo. 
# Un número primo es un entero que no tiene más divisores que él mismo y la unidad.
num = input("Ingrese un numero: ")
def evaluar_numero(num):
    contador = 0
    resultado = True
    for i in range(1, int(num) + 1):
        if (int(num) % i == 0):
            contador += 1
        if (contador > 2):
            resultado = False
            break
    return resultado
if (evaluar_numero(int(num)) == True):
    print("El numero ingresado es primo")
else:
    print("El numero no es primo")