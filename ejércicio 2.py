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

#Creo una función llamada lee_numero() que pida y lea un número
def lee_numero():   
    return inputfloat("Dame un número: ")

#Creo una función llamada mayor() con 3 parametros que devuelva el mayor de los 3 
def mayor(numero1, numero2, numero3):
             return max(numero1, numero2, numero3)       

numero1 = lee_numero() 
numero2 = lee_numero()
numero3 = lee_numero()

print(mayor(numero1, numero2, numero3))