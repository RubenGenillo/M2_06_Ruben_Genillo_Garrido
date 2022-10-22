import math

#Creo una función que me va servir para la mayoría de preguntas del ejercicio
def inputfloat(texto):
  while True:
    num = input(texto)
    try:
        num = float(num)
    except:
        print("no es un numero") 
    else:    
       return num

#1.
#Creo una función llamada area_circulo que devuelva el área de un círculo a partir de un radio que se pedirá al usuario
def area_circulo():
    radio = inputfloat("Dame el radio de una circunferencia: ")
    return math.pi * radio**2


#2.
#Creo una función llamada lee_numero() que pida y lea un número
def lee_numero():   
    return inputfloat("Dame un número: ")

#Creo una función llamada mayor() con 3 parametros que devuelva el mayor de los 3 
def mayor(numero1, numero2, numero3):
        return max(numero1, numero2, numero3)

numero1 = lee_numero() 
numero2 = lee_numero()
numero3 = lee_numero()

#Le paso estos 3 números a mayor para que devuelva el número mayor de los 3
print(mayor(numero1, numero2, numero3))

#3.
#Creo una función llamada imc, que reciba el peso (en kilos) y talla (en metros) de una persona, y calcule y proporcione el estado nutricional de una persona
def imc(peso, talla):
    Imc = peso/(talla**2)
    tabla = {
    Imc<18.50: "Bajo peso",
    18.50 <= Imc <25 : "Normal",
    25 <= Imc < 30 : "Sobrepeso",
    30 <= Imc: "Obesidad"
    }
    return tabla[True]
