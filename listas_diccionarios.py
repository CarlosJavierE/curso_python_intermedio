def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Miguel", "lastname": "Torrez"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "Jose", "lastname": "Garcia"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "flotating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f"{key}    :    {value}")

    print()         # separador o espaciado
    
    for dicc in super_list:         # recorro la lista, que se convierte en diccionario
        for keys, values in dicc.items():       # recorro el diccionario creado por el anterior for
            print(f"{keys}  :   {values}")


if __name__ == '__main__':
    run()