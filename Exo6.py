print("Saisissez la température que vous souhaitez convertir ? (par exemple, 45F, 102C etc.)")
temp = input()
if temp[-1] in ['F', 'f']:
    celsius = (float(temp[:-1]) - 32) * 5.0 / 9.0
    print(f"La température en Celsius est : {celsius:.2f}C")
elif temp[-1] in ['C', 'c']:
    fahrenheit = (float(temp[:-1]) * 9.0 / 5.0) + 32
    print(f"La température en Fahrenheit est : {fahrenheit:.2f}F")
else:
    print("Format de température invalide.")