import sqlite3

def conexion():
    conexion = sqlite3.connect("IP_FILTROS.db")
    cursor = conexion.cursor("")












def insertar_datos(conexion,tabla,datos):
    datos = ("filtro",12,2.5,"automotriz")

    cursor = conexion.cursor()
    
    columnas = "?,"*len(datos)#es un string que guarda "?,?,?,?,"con la coma al final(su longuitud depende del numero de colummnas)
    columnas_fix = columnas.rstrip(",")#quita la ultima coma que se guardo en el string anterior (",")
    
    cursor.execute(f"INSERT INTO {tabla} VALUES({columnas_fix})",datos)
    conexion.commit()
    return 1
