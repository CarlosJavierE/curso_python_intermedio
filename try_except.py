# try and except
# def palindromo(string):
#     return string == string[::-1]

# try:                            # si el usuario ingresa un numero entonces primero try
#     print(palindromo(1))    
# except TypeError:               # una vez detectado el error en la consola, copiamos el error y lo ponemos en el except
#     print("Solo se pueden ingresar strings")


# raise
def palindromo(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindromo(""))
except TypeError:
    print("Solo se pueden ingresar strings")