import pandas as pd

def cargar_datos(): #Funcion para cargar los datos/archivos
    nombre_ventas = input("Nombre del archivo de ventas, no es necesario poner la extencion de archivo: ")
    nombre_sucursales = input("Nombre del archivo de sucursales, no es necesario poner la extencion de archivo: ")
    archivo_ventas = nombre_ventas + ".csv"
    archivo_sucursales = nombre_sucursales + ".json"
    try:
        ventas = pd.read_csv(archivo_ventas)
        sucursales = pd.read_json(archivo_sucursales)
        print("\nDatos cargados correctamente.")
        return ventas, sucursales
    except FileNotFoundError:
        print("\nError: No se encontró el archivo.")
        return None, None

def mostrar_ventas(ventas): #Funcion para mostrar las ventas que queramos
    if ventas is None:
        print("Primero debes cargar los datos")
        return
    cantidad = int(input("Cuantas ventas deseas mostrar: "))
    print(ventas.head(cantidad).to_string(index=False))

def mostrar_sucusales(sucursales): #Funcion para mostrar el numero de sucursales
    if sucursales is None:
        print("Primero debes cargar los datos")
        return
    cantidad = int(input("Cuantas sucursales deseas mostrar: "))
    print(sucursales.head(cantidad).to_string(index=False))

def integrar_informacion(ventas, sucursales):
    if ventas is None or sucursales is None:
        print("Primero debes cargar los datos")
        return None
    integrado = pd.merge(
        ventas,
        sucursales,
        on="sucursal_id",
        how="left"
    )
    return integrado

def ventas_sucursal(integrado):
    resultado = (
        integrado.groupby("sucursal_id")["importe"]
        .sum()
        .reset_index()
    )
    return resultado

def promedio_ventas(integrado):
    resultado = (
        integrado.groupby(["sucursal_id","sucursal"])["importe"]
        .mean()
        .round(2)
        .reset_index()
        .sort_values("importe", ascending=False)
    )
    return resultado

def ranking_sucursales(integrado):
    resultado =(
        integrado.groupby(["sucursal_id","sucursal"])["importe"]
        .sum()
        .round(2)
        .reset_index()
        .sort_values("importe", ascending=False)
    )
    resultado["ranking"] = resultado["importe"].rank(
        ascending=False,
        method="dense"
    ).astype(int)
    return resultado

def ventas_ciudad(integrado):
    resultado = (
        integrado.groupby("ciudad")["importe"]
        .sum()
        .round(2)
        .reset_index()
        .sort_values("importe", ascending=False)
    )
    return resultado

def estadisticas(integrado):
    resultado = integrado[["cantidad", "importe"]].describe().round(2)
    return resultado

def exportar_reporte(integrado):
    if integrado is None:
        print("Primero debes integrar la informacion")
        return
    ventas_sucursal_resultado = ventas_sucursal(integrado)
    promedio_resultado = promedio_ventas(integrado)
    ranking_resultado = ranking_sucursales(integrado)
    ciudad_resultado = ventas_ciudad(integrado)
    estadisticas_resultado = estadisticas(integrado)
    with pd.ExcelWriter("reporte_sucursales.xlsx") as writer:
        integrado.to_excel(writer,sheet_name="Ventas", index=False)
        ventas_sucursal_resultado.to_excel(
            writer, sheet_name="Ventas por sucursal", index=False
        )
        promedio_resultado.to_excel(
            writer, sheet_name="Promedio", index=False
        )
        ranking_resultado.to_excel(
            writer, sheet_name="Ranking", index=False
        )
        ciudad_resultado.to_excel(
            writer, sheet_name="Ventas por ciudad", index=False
        )
        estadisticas_resultado.to_excel(
            writer, sheet_name="Estadisticas"
        )
    print("Reporte exportado correctamente como ´reporte_sucursales.xlsx´")

integrado = None
ventas = None
sucursales = None
opcion = -1
while opcion != 0:
    print("""=================================
            ANALIZADOR DE SUCURSALES
    =================================
    
        1. Cargar datos
        2. Mostrar ventas
        3. Mostrar sucursales
        4. Integrar información
        5. Ventas por sucursal
        6. Promedio de ventas
        7. Ranking de sucursales
        8. Ventas por ciudad
        9. Estadísticas
        10. Exportar reporte
        11. Salir
        """)
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 1:
        print("---Cargar datos---")
        ventas, sucursales = cargar_datos()
    elif opcion == 2:
        print("---Mostrar ventas---")
        mostrar_ventas(ventas)
    elif opcion == 3:
        print("---Mostrar sucursales---")
        mostrar_sucusales(sucursales)
    elif opcion == 4:
        print("---Información integrada---")
        integrado = integrar_informacion(ventas, sucursales)
        if integrado is not None:
            print("Columnas:")
            print(integrado.columns.tolist())
            print("\nDatos:")
            print(integrado.to_string(index=False))
    elif opcion == 5:
        print("---Ventas por sucursal---")
        if integrado is None:
            print("Primero debes integrar la información")
        else:
            resultado = ventas_sucursal(integrado)
            print(resultado.to_string(index=False))
    elif opcion == 6:
        print("---Promedio de ventas por sucursal---")
        if integrado is None:
            print("Primero debes cargar los datos")
        else:
            resultado = promedio_ventas(integrado)
            print(resultado.to_string(index=False))
    elif opcion == 7:
        print("---Ranking de sucursales---")
        if integrado is None:
            print("Primero debes cargar los datos")
        else:
            resultado = ranking_sucursales(integrado)
            print(resultado.to_string(index=False))
    elif opcion == 8:
        print("---Ventas por ciudad---")
        if integrado is None:
            print("Primero debes cargar los datos")
        else:
            resultado = ventas_ciudad(integrado)
            print(resultado.to_string(index=False))
    elif opcion == 9:
        print("---Estadisticas---")
        if integrado is None:
            print("Primero debes cargar los datos")
        else:
            resultado = estadisticas(integrado)
            print(resultado.to_string(index=False))
    elif opcion == 10:
        print("---Exportar reporte---")
        if integrado is None:
            print("Primero debes cargar los datos")
        else:
            resultado = exportar_reporte(integrado)
    elif opcion == 11:
        print("Saliendo del sistema...")
        input("Presione enter para continuar...")
        break;