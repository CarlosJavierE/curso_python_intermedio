DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # aqui quiero los nombres de los que su languaje es python
    # worker es una nueva variable que estoy usando para este ejericio
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # print(all_python_devs)   # no es parte dl problema, solo para mirar
    # for trabajador in all_python_devs:
    #     print(trabajador)

    # all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    # for trabajador in all_platzi_workers:
    #     print(trabajador)

    # adultos mayores a 18 años
    # adults = list(filter(lambda worker: worker["age"] > 18, DATA))      # aqui flitra los diccionarios que tengan el key "age" > 18, en diccionarios
    # only_name = list(map(lambda worker: worker["name"], adults ))       # aqui filtra solo los nombres de lo que hicimos antes
    # for name in only_name:
    #     print(name)

    # en la lista de diccionario agregar a cada diccionario una nueva key : value que es
    # si es mayor a 70 años la nueva key:value es "old": True
    # aqui estoy creando otro diccionario con {"old": worker["age"] > 70}
    # que se une a cada diccionario-worker con "|" pipe que es la union como "+" para concatenar listas
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) 
    for old in old_people:
        print(old)
    

if __name__ == '__main__':
    run()

