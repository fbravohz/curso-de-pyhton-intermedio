def divisors(num):
    divisorss = []
    for i in range(1,num+1):
        if num % i == 0:
            divisorss.append(i)
    return divisorss

def run():
    #Flujo con Try Except Raise Else Finally
    try:
        num = int(input("Ingresa un numero: "))
        if num < 0:
            raise ArithmeticError("Debes ingresar un numero positivo")
    except ValueError:
        print("Debes ingresar un numero")
    except ArithmeticError as a_e:
        print(a_e)
    else:
        print(divisors(num))
        print("Termino mi programa")

if __name__ == "__main__":
    run()
