def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname": "Felipe", "lastname": "Bravo"}

    super_list = [
        {"firstname": "Felipe", "lastname": "Bravo"},
        {"firstname": "Juan", "lastname": "Guzman"},
        {"firstname": "Alejandro", "lastname": "Azabache"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-2,-1,0,1,2,3],
        "floating_nums": [1.1,2.2,3.4,6.2]
    }

    for key, value in super_dict.items():
        print(key, " - ",value)

    #Esta es la actividad que solicita el profe al final del video
    #1st way
    for value in super_list:
        print(value.items())  
    #2nd way
    for item in super_list:
        print(item["firstname"], " - ",item["lastname"])      
    #3rd way
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

if __name__ == "__main__":
    run()


