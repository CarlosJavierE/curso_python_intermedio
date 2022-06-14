# assert ejemplo 1
def palindromo(string):
    # assert len(string) > 0, "No se puede ingresar una cadena vacia"
    return string == string[::-1]

variable = input("Escribe una palabra: ")
assert variable.isalpha() and len(variable) > 0, "no se admite numeros y cadena vacia"
es_palindromo = palindromo(variable)
print(es_palindromo)


# def divisors(num):
#         divisor = []
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 divisor.append(i)
#         return divisor


# def run():     
#     num = input("Ingresa un numero: ")
#     assert num.isnumeric() and int(num) > 0, "Debes ingresar solo numeros y positivos"    #devuelve true si es un numero pero este numero tiene que estar en string
#     # chelenge, ademas que solo sea numero positivos "and int(num) > 0"
#     print(divisors(int(num)))
#     print("termino mi porgrama")
            

# if __name__ == '__main__':
#     run()