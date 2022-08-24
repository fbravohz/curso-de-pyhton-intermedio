def run():
    squares = []
    for i in range(1,101):
        squares.append(i**2)
    print(squares)

    #numeros al cuadrado que no son divisibles entre 3
    squares2 = []
    for i in range(1,101):
        if((i**2)%3 != 0): 
            squares2.append(i**2)
    print(squares2)

    #Comprehension = [element #for element #in iterable #if condition]
    
    squares3 = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares3)

    #ejercicios del profe
    squares4 = [i for i in range(1,100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(squares4)

if __name__ == "__main__":
    run()



    