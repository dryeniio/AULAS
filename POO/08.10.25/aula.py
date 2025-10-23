temp = float(input("Digite a Temp."))

if (temp > 40):
    print("Está quente!")
elif (temp == 0):
    print("Muito frio!")
elif ( temp > 0 and temp < 20):
    print("Ainda está frio")
elif (temp > 30):
    print("Estamos derretendo!")
elif ( -273.15 <= temp < 0):
    print("Estamos Congelando.")
elif (temp < -273.15):
    print("Temperatura não existe.")
else:
    print("Temperatura agradável.")