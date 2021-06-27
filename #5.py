#Ejercicio 16:
#Aplicar los pasos de la metodología para la 
#solución de un problema para leer un número entero N y 
#calcular el resultado de la siguiente serie:
#1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema 
#utilizando bucle Repeat controlado por contador y usando banderas.
class numero:
  def num_entero(self):
    x = 0
    i = 1
    num = input("Ingrese un numero entero: ")
    a = "T"
    while i < int(num):
      if a == "T":
        x = x * (1/i)
        a = "F"
      else:
        x = x -(1/i)
        a = "T"
      i = i + 1
    print("El resultado de la serie es: {}".format(x))
dato = numero()
dato.entero()


#Ejercicio 17:
#Calcular el factorial de N números enteros leídos de teclado.
#El problema consistirá en realizar una estructura de N 
#iteraciones aplicando el factorial de un número.
class factorial:
  def numero(el):
    num = input("Ingrese la cantidad de veces: ")
    a = 1 
    for i en range(int(num)):
      n = input("Ingrese un numero entero: ")
      fac = 1
      for b en el range(1, int(n) + 1):
        fac += b
        print("El factor del numero {}".format(int(n), fac))
dato = factorial()
dato.numero()


#Ejercicio 18:
#Sea un vector “Calificaciones” de 100 componentes:
#En forma de columna se representaría así:
class vector:
  def calificaciones(self):
    calificaciones = []
    j = 0
    c = 1
    for i in range(100):
      calificaciones.append(i)
      j = j + 1
      print(" ")
      for i in range(j):
        print("La calificacion es {}".format(calificaciones[i]+1))
        c = c + 1
dato = vector()
dato.calificaciones()


#Ejercicio 19:
#Aplicar las fases  para  la resolución de un problema para leer un vector de 20 
#números enteros y a continuación escribir en un vector A todos los números negativos y 
#en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores.
class vector:
  def calificaciones(self):
    A = []
    B = []
    a = 0
    b = 0
    num = []
    for i in range(0, 20, 1):
      n = input("Ingrese un numero entero: ")
      num.append(int(n))
      if num[i] < 0:
        A.insert(a, num[i])
        a = a + 1
      else:
        B.insert(b, num[i])
        b = b + 1
    print(" ")
    for i in range(0, a, 1):
      print("El vector A tiene el valor de{}".format(A[i]))
    print(" ")
    for i in range(0, b, 1):
      print("El vector B tiene el valor de{}". format(B[i]))
dato = vector()
dato.calificaciones()


#Ejercicio 20:
#Se tiene información sobre las calificaciones de 6 
#exámenes de un grupo de 30 alumnos. Los datos sobre estos exámenes 
#se proporcionan de la siguiente manera:
#Donde Cali,j es una variable real que expresa la calificación que obtuvo el alumno i en el examen j. 
#Calcular lo siguiente:
#a) el promedio de calificaciones de cada uno de los 6 exámenes
#b) el promedio de cada alumno
#c) el tipo (número) de examen que tuvo el mayor promedio de calificación. Escriba también dicho promedio.
class Arreglo:  
    def dimensiones(self):
        Calif = []
        prom = []
        for f in range(30):
            Calif.append([])
            for c in range(6):
                Calif[f].append(None)
                Calif[f][c] = float(input("Ingresar calificacion que obtuvo el alumno {} en el examen {}: ".format(f + 1, c + 1)))
        print("")
        for f in range(30):
            for c in range(6):
                print(Calif[f][c],end=" ")
            print() 
        
        print(" ")
        #Cálculo del promedio de calificaciones de cada uno de los exámenes
        for c in range(6):
            sum = 0
            for f in range(30):
                sum = sum + Calif[f][c]
            prom.append(sum / len(Calif))
            print("El promedio del examen {} : {:.2f}".format(c + 1, sum / len(Calif)))
        print(" ")
        #cálculo del promedio de cada alumno
        for f in range(30):
            sum = 0
            for c in range(6):
                sum = sum + Calif[f][c]
            print("El promedio del alumno {} : {:.2f}".format(f + 1, sum / len(Calif)))
        print(" ")
        #cálculo del tipo de examen que tuvo el mayor promedio de calificación.
        exam = 0
        prom_mayor = prom[1]
        for c in range(6):    
            if prom_mayor < prom[c]:
                prom_mayor = prom[c]
                exam = c
        print("El examen {} obtuvo el mayor promedio siendo este: {}".format(exam + 1, pro_mayor))
dato = Arreglo()
dato.dimensiones()