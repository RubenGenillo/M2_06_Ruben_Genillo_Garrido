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