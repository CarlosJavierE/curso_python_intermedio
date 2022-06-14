def read():
    numeros = []
    # aqui en la ubicacion del archivo si funciona "./archivos/numeros.txt" aunque no autocomplete
    with open("./archivos/numeros.txt", "r", encoding="utf-8") as f:
        for line in f:
            numeros.append(int(line))       # en el archivo de texto vien con cadena de texto
    print(numeros)

def write():
    # "r" read, "w" write, "a" append
    nombres = ["Fatima", "Carlos", "Javier", "Samuel", "Nuñez"]
    with open("./archivos/names.txt", "a",  encoding="utf-8") as f:
        for name in nombres:
            f.write(name)
            f.write("\n")

def run():
    read()     # no olvidarse llamar a la funcion


if __name__ == '__main__':
    run()