#debo realizar un programa que tome minutos y los transforme en horas

#creo definición de una hora
una_hora = 60

while True:
    #ingreso minutos a transformar y genero su cantidad en horas
    try:
        in_minutos = int(input("ingrese los minutos a convertir - "))
    except ValueError:
        print("Ingrese un Valor Válido")
    try:
        new_hora = int(in_minutos / una_hora)
    except NameError:
        break
    #si hay mas de 60 min, genero la transformación
    if new_hora > 0:
        new_minutos = in_minutos % (new_hora*60)
        result_horas = f"Horas: {new_hora} , Minutos {new_minutos}"
        print(result_horas)
        #si el input es 0, termino el programa
    elif in_minutos == 0:
        print("programa finalizado")
        break
    #si el input esta entre 1 y 59, devuelvo resultado en minutos. 
    else:
        print(f"Horas: 0, minutos {in_minutos} ")
