#separar lista de numeros en lista de pares e impares
numeros = [1,2,3,4,5,6,7,8,9,10]
par = []
impar = []
while len(numeros) > 0:
    number = numeros.pop() #Toma el ultimo elemento de las lista
    if number % 2 == 0:
        par.append(number)

    else:
        impar.append(number)

print(par)
print(impar)