from filtering_data_db import DATA

def run():
    #Usamos list comprehensions
    print("Made with comprehensions\n")
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == "python"]
    for worker in all_python_devs:
        print(worker)

    print("\n")

    #Usamos high order functions (Filter y map)
    print("Made with high order functions and lambdas\n")
    #Con filter es para validar las condiciones de la busqueda
    all_python_devs2 = list(filter(lambda worker: worker['language'] == "python",DATA))
    #Con map es para extraer solo la informacion que queremos utilizar
    all_python_devs2 = list(map(lambda worker: worker['name'],all_python_devs2))
    for worker in all_python_devs2:
        print(worker)

    print("\n")

    #Usamos list comprehensions
    print("Made with comprehensions\n")
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == "Platzi"]     
    for worker in all_platzi_workers:
        print(worker)

    print("\n")

    #Usamos high order functions (Filter y map)
    print("Made with high order functions and lambdas\n")
    all_platzi_workers2 = list(filter(lambda worker: worker['organization'] == "Platzi",DATA))
    all_platzi_workers2 = list(map(lambda worker: worker['name'],all_platzi_workers2))
    for worker in all_platzi_workers2:
        print(worker)

    print("\n")

    #Usamos high order functions (Filter y map)
    print("Made with high order functions and lambdas\n")
    adults = list(filter(lambda worker: worker['age'] > 18,DATA))
    adults = list(map(lambda worker: worker["name"] + " : " + str(worker["age"]),adults))
    for worker in adults:
        print(worker)    

    print("\n")

    #Usamos list comprehensions
    print("Made with comprehensions\n")
    adults = [worker['name'] + " : " +str(worker['age']) for worker in DATA if worker['age'] > 18]
    for worker in adults:
        print(worker)

    print("\n")

    #Usamos high order functions (Filter y map)
    print("Made with high order functions and lambdas\n")
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70},DATA))
    for worker in old_people:
        print(worker)   

    print("\n")

    #Usamos list comprehensions
    print("Made with comprehensions\n")
    old_people2 = [worker | {'old': worker["age"] > 70} for worker in DATA]
    for worker in old_people2:
        print(worker)

if __name__ == "__main__":
    run()
