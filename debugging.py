# hacer un programa que guarde en una lista los numeros divisibles de un numero
# ahora estoy haciendo con try and except
def divisors(num):
    try:
        if num < 0:
            raise ValueError("Solo poner numeros positivos chaval")
        divisor = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisor.append(i)
        return divisor
    except ValueError as ve:
        print(ve)
        return "Intentalo de nuevo"


def run():      # aqui es donde se ejecuta el porgrama por lo tanto se pone el try and except aqui
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("termino mi porgrama")
    except ValueError:
        print("Debes ingresar un numero")



if __name__ == '__main__':
    run()