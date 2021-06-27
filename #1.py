
# Transcribir los sguientes Pseudocodigos al lenguaje Python

# Ejercicio 1:
# En una tienda se ofrece un descuento del 15% sobre el total de la 
# compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
tienda = input("Ingrese el valor de la compra: ")
Dc = int(float(tienda)) * 15 / 100
cant_Pago = int(float(tienda)) - Dc
print("Su descueto por la compra es de: $", Dc)
print("El valor a pagar es: $", cant_Pago)


#Ejercicio 2:
# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las 
# tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.
sueldo = int(float(input("Ingrese el valor del sueldo: ")))
venta_1 = int((float(input("Ingrese su primera venta del mes: "))))
venta_2 = int((float(input("Ingrese su segunda venta del mes: "))))
venta_3 = int((float(input("Ingrese su tercera venta del mes: "))))
comision = (venta_1 + venta_2 + venta_3) * 10 / 100
print("El sueldo del empleado es: $", sueldo)
print("La comsion del mes por las 3 ventas son: $", comision)
print("El sueldo total incluido su comision es de: $", sueldo + comision)


#Ejercicio 3:
# Dado como dato la calificación de un alumno en un examen
acum = 0
long = 0
Estudiante = int("Escriba el nombre del estudante: ")
notas = input[float(int("Ingrese su calficaciones: "))]
for lista_Notas in notas:
    parcial = 0 
    print(notas, end = " ")
    for nota in notas:
        print(notas)
        long = long + 1
        acum = acum + notas
        parcial += notas
    Promedio = parcial / len(notas)
    print("Notas Parciales = {} Promedio parcial = {}". format(parcal, Promedio))
prom = acum/long
print("Total nostas ={} -#Notas ={}: Promedio ={} ".format(acum, long, prom))
nota_1 = For()
nota_1.usoFor()