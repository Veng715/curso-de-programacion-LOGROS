# Login simple
nombre = input("nombre de usuario: ")
contra = int(input("contraseña: "))

if nombre != "admin" and contra != "1234":
    print("error al iniciar sesión")
else:
    print("iniciando sesión")