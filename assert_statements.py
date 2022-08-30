def divisors(num):
    divisorss = []
    for i in range(1,num+1):
        if num % i == 0:
            divisorss.append(i)
    return divisorss

def run():
    #Flujo assert statements
    num = input("Ingresa un numero: ")
    assert num.isnumeric() and int(num) >= 0,"Debes ingresar un número y que sea positivo"
    print(divisors(int(num)))
    print("Termino mi programa")

if __name__ == "__main__":
    run()
