import json
import random



idVehiculo = 301
lista_tipos = ["BUS ESCOLAR","AUTO PARTICULAR","MOTOCICLETAS","CAMION","BUS PUBLICO","TAXI"]
lista_sectores = ["SAMBORONDON", "DAULE", "LA ALBORADA", "BELLAVISTA"]
lista_horas = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]

for i in range(0, 100):

    minutos = random.randint(0,59)
    if minutos <= 9:
        minutos = "0" + str(minutos)

    dic = {
        "IdCarro" : idVehiculo,
        "tipo" : lista_tipos[random.randint(0,len(lista_tipos)-1)],
        "hora" : str(lista_horas[random.randint(0,len(lista_horas)-1)] +  str(minutos)),
        "sector" : lista_sectores[random.randint(0,len(lista_sectores)-1)],
        "velocidad" : random.randint(60,121)
    }

    json_object = json.dumps(dic, indent = 4)

    with open("Vehiculos.json", "a") as outfile:
        outfile.write(json_object + "," + "\n")

    idVehiculo += 1