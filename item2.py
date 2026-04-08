# 1. Datos fijos
print("Evaluacion: N°1 Programacion y Redes Virtualizadas")
print("Nombre: Matias Mellado")

# 2. Pedir datos al usuario
nombre = input("Nombre: ")
apellido = input("Apellido: ")
seccion = input("Sección: ")
sede = input("Sede: ")

# Mostrar los datos
print("Datos: " + nombre + " " + apellido + ", Sección: " + seccion + ", Sede: " + sede)

# 3. Clasificación de ACL
n = int(input("Ingrese número de ACL: "))

if n >= 1 and n <= 99:
    print("ACL Estandar")
elif n >= 100 and n <= 199:
    print("ACL Extendida")
elif n >= 1300 and n <= 1399:
    print("ACL Estandar")
elif n >= 2000 and n <= 2699:
    print("ACL Extendida")
else:
    print("El número no corresponde a una ACL")
