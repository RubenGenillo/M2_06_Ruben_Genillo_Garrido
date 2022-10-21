import math

#Creo una función que solo admita números
def inputfloat(texto):
  while True:
    num = input(texto)
    try:
        num = float(num)
    except:
        print("no es un numero") 
    else:    
       return num

#Creo una función llamada area_circulo que devuelva el área de un círculo a partir de un radio que se pedirá al usuario
def area_circulo():
    radio = inputfloat("Dame el radio de una circunferencia: ")
    return math.pi * radio**2