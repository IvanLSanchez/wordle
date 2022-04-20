## importa base de datos y propiedadews de tiempo ♥
import dataBase
import time

## seleccion de dificultad y declaracion de cantidad de letras ♥
palabraSeleccionada = ""
cantidadLetras = 1
print("")
dificultad = input("Ingrese dificultad facil (F), normal (M) o dificil (D): ")

if dificultad == "F" or dificultad == "f":
    palabraSeleccionada=dataBase.pF
    cantidadLetras = 4

elif dificultad == "M" or dificultad == "m":
    palabraSeleccionada = dataBase.pM
    cantidadLetras = 5

elif dificultad == "D" or dificultad == "d":
    palabraSeleccionada = dataBase.pD
    cantidadLetras = 6

## texto de transicion e inicio de tiempo ♥
print("")
print("seleccionando palabra")
for i in range (3):
    print("...")
print ("¡listo!")
comienzo=time.time()

## intentos ♥
respuesta = ""
intentos=0
while (respuesta != palabraSeleccionada) and intentos<=5:
    ## recibe respuesta  ♥
    print("")
    respuesta = input(f"Ingrese una palabra de {cantidadLetras} letras: ")
    print("")
    if len(respuesta) != cantidadLetras:
        while len(respuesta) != cantidadLetras:
            respuesta = input(f"Ingrese una palabra de {cantidadLetras} letras: ")
            print("")
    
    ## compara ♥
    comparativa = []
    i = 0
    for i in range (cantidadLetras):
        if respuesta[i] == palabraSeleccionada[i]:
            comparativa.append("=")
        elif respuesta[i] in palabraSeleccionada:
            comparativa.append("-")
        else:
            comparativa.append("x")
        i += 1
    
    # imprime comparacion ♥
    letras=""
    strcomparado=""
    i = 0
    for i in range (cantidadLetras):
        letras = letras + respuesta[i]
        strcomparado = strcomparado + comparativa[i]
        if i != cantidadLetras:
            letras = letras + " "
            strcomparado = strcomparado + " "
    
    print(letras)
    print(strcomparado)
    
    ## suma intento ♥
    intentos = intentos + 1

##finaliza tiempo ♥
final=time.time()

## respuestas finales ♥
if respuesta == palabraSeleccionada:
    print("")
    print("")
    print ("Ganaste :D")
    print("")
    print (f"adivinaste la palabra en: {final-comienzo} segundos")
    print("")
    print (f"te tomo adivinar la palabra {intentos} intentos")
else:
    print("")
    print("")
    print ("Perdiste D:")
    print("")
    print (f"Estuviste: {final-comienzo} segundos")