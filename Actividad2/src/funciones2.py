def convertir_a_segundos(duracion_str):
    """Esta funcion convierte la duración de formato "m:ss" a cantidad de segundos totales (número entero)"""
    minutos, segundos = duracion_str.split(':')
    return int(minutos) * 60 + int(segundos)