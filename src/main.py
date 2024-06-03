def start():
    print("Bienvenido a calculadora")
    cycle_calculator()
    
def sumar():
    num1 = int(input("Escriba el primer numero: "))
    num2 = int(input("Escriba el segundo numero: "))
    res = suma(num1, num2)
    print(f"El resultado de {num1} + {num2} es {res}")

def suma(num1, num2):
    return num1 + num2

def restar():
    num1 = int(input("Escriba el primer numero: "))
    num2 = int(input("Escriba el segundo numero: "))
    res = resta(num1, num2)
    print(f"El resultado de {num1} - {num2} es {res}")

def resta(num1, num2):
    return num1 - num2

def multiplcar():
    num1 = int(input("Escriba el primer numero: "))
    num2 = int(input("Escriba el segundo numero: "))
    res = multiplcacion(num1, num2)
    print(f"El resultado de {num1} * {num2} es {res}")

def multiplcacion(num1, num2):
    return num1 * num2
    
def dividir():
    num1 = int(input("Escriba el dividendo: "))
    num2 = int(input("Escriba el divisor: "))
    if num2 <= 0:
        print("Error, division por cero")
    else:
        res = division(num1, num2)
        print(f"El resultado de {num1} / {num2} es {res}")

def division(num1, num2):
    if num2 == 0:
        return "error"
    return num1 / num2
    
def cycle_calculator():
    stop = True
    while stop:
        print("Menu")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        option = int(input("Escoja una opción: "))
        
        if option == 1:
            sumar()
        elif option == 2:
            restar()
        elif option == 3:
            multiplcacion()
        elif option == 4:
            division()
        else:
            print("Opción no válida. Intente nuevamente.")