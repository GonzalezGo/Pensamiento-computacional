print("Primer programa pasar meses de español a ingles")

month_mes = {
    "enero": "January",
    "febrero": "February",
    "marzo": "March",
    "abril": "April",
    "mayo": "May",
    "junio": "June",
    "julio": "July",
    "agosto": "August",
    "septiembre": "September",
    "octubre": "October",
    "noviembre": "November",
    "diciembre": "December"
}

def traduce_mes(month):
    month = month.lower()
    return month_mes.get(month, "mes no válido")


mes_español = input("Ingresa un mes en español: ")
mes_ingles = traduce_mes(mes_español)
print("El mes en ingles es: ", mes_ingles)