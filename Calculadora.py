#calculadora

num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))

operacion = input("introduce operacion: (+ - * / ^): ")

match operacion:
    case "+":
        res = num1+num2
    case "-":
        res = num1-num2
    case "*":
        res = num1*num2
    case "/":
        res = num1/num2
    case "^":
        res = num1**num2

print(f"El resultado de {num1}{operacion}{num2} es {res}")
