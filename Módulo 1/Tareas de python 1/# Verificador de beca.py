# Verificador de beca
edad = int(input("ingrese su edad: "))
calificacion = int(input("ingrese su calificación: "))
if edad >= 18 and calificacion >= 9:
    print("el estudiante puede optar a una beca")
else:
    print("el usuario no puede optar a una beca")