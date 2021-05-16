import json
import random



idVehiculo = 1
lista_tipos = ["BUS ESCOLAR","AUTO PARTICULAR","MOTOCICLETAS","CAMION","BUS PUBLICO","TAXI"]
lista_sectores = ["SAMBORONDON", "DAULE", "LA ALBORADA", "BELLAVISTA"]

dic_list = []

for i in range(0, 100):

    horas = random.randint(0, 23)
    minutos = random.randint(0,59)

    dic = {
        "IdCarro" : idVehiculo,
        "tipo" : random.choice(lista_tipos),
        "hora" : str(horas).zfill(2) + ":" +str(minutos).zfill(2),
        "sector" : random.choice(lista_sectores),
        "velocidad" : random.randint(60,121)
    }

    dic_list.append(dic)
    idVehiculo += 1

json_object = json.dumps(dic_list, indent = 0)

with open("Vehiculos.json", "a") as outfile:
    outfile.write(json_object)
