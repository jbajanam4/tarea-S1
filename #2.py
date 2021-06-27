#Ejercicio 4:
# Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación 
# es mayor o igual que 7 y “Reprobado” en caso contrario.
alumno = input("Escriba el nombre del estudante: ")
nota = int(float(input("Ingree su promedio: ")))
if int(float(nota)) >= 7:
    print("Usted Sr.(@):",alumno)
    print("Aprobo, su nota es de:",nota)
elif int(float(nota)) <= 6.9:
    print("Usted Sr.(@):", alumno) 
    print("No aprobo, su nota es de:",nota)


#Ejercicio 5:
#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% 
#si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
#sueldo = input("Ingrese el valor de su sueldo: ")
if int(float(sueldo)) >= 600:
    pago = (600 * 10) / 100
    aumento = int(float(sueldo)) + pago
    print("Su sueldo actual es de $:",sueldo)
    print("Su aumento del 10% $:",pago)
    print("El pago total es de $:",aumento)
elif int(float(sueldo)) < 600:
    print("Usted no tiene aumento, el sueldo es el mismo $:",sueldo)
 

#Ejercicio 6:
#Determinar la cantidad de dinero que recibirá un trabajador 
#por concepto de las horas extras trabajadas en una empresa, 
#sabiendo que cuando las horas de trabajo exceden de 40, el 
#resto  se consideran horas extras y que éstas se pagan al doble de una hora normal 
#cuando no exceden de 8;  si las horas extras 
#exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una 
#hora normal y el resto al triple.
Hora = input("Ingrese sus horas de trabajo: ")
pago = input("Cuanto le pagan por hora: ")
if int(Hora) >= 48:
    triple = float(pago) * 3
    sueldo = int(Hora) * triple  
    print("Usted es un exelecte trabajador")
    print("El sueldo con horas extras es de $:",sueldo)
elif int(Hora) >= 40:
    doble = float(pago) * 2
    sueldo = int(Hora) * doble 
    print("Usted es un buen trabajador")
    print("Su sueldo por horas extras es $:",sueldo)
else:
    sueldo = int(Hora) * float(pago)
    print("Su sueldo de trabajo es $:",sueldo)    


#ejercicio 7:
#Leer tres números enteros diferentes entre sí y determinar 
#el número mayor de los tres.
a = input("Ingrese un numero entero: ")
b = input("Ingrese otro numero entero: ")
c = input("Ingrese un ultimo numero entero: ")
if b < a > c:
    print("El numero mayor es:", a)
elif a < b > c:
    print("El numero mayor es:",b)
elif a < c > b:
   print("El numero mayor es:",c)
else:
    print("Todos los numeros son iguales")