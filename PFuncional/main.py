BD = {"ADMIN": "1234", "JUAN": "juan123"}
# Este diccionario se considera constante y no debe ser modificado después de su definición

def access(username, password):
    return confirm(password == BD.get(username, None))

def login():
    user = getUser().upper()  # Convertir a mayúsculas para que coincida con las claves
    password = getPass()
    return access(user, password)

def confirm(result):
    if result:
      return "Inicio de sesión exitoso"
    else:
     return "Inicio de sesión fallido"

def getUser():
    return input("Ingrese su nombre de usuario: ")

def getPass():
    return input("Ingrese clave: ")


if __name__ == "__main__":
    print(login())


