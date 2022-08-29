from cmath import sqrt
from decimal import Rounded
from math import floor


def run():


    #Primer ejercicio

    my_dictionary1 = {}
    for i in range(1,101):
        my_dictionary1[i] = i**3
    print(my_dictionary1)    


    #Segundo ejercicio

    my_dictionary2 = {}
    for i in range(1,101):
        if i % 3 != 0:
            my_dictionary2[i] = i**3
    print(my_dictionary2)


    #Tercer ejercicio 
    
    my_dictionary3 = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dictionary3)


    #Reto

    my_dictionary4 = {i : round(i**0.5,4) for i in range(1,1001)}
    for key, value in my_dictionary4.items():
        print(key,":",value)

if __name__ == "__main__":
    run()






