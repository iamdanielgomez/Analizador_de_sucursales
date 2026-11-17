# 📊 Analizador de Sucursales

## 📌 Descripción

Analizador de Sucursales es un proyecto desarrollado en Python que permite cargar, integrar y analizar información de ventas y sucursales de una empresa.

Mediante el uso de la biblioteca Pandas, el programa procesa archivos CSV y JSON para generar diferentes reportes que permiten conocer el comportamiento de las ventas, comparar el rendimiento de las sucursales e identificar cuáles generan mayores ingresos.

Los resultados pueden consultarse directamente desde la terminal o exportarse a un archivo Excel.

## 🚀 Funcionalidades

El programa cuenta con un menú interactivo que permite realizar las siguientes operaciones:

- **Cargar datos:** Leer información de ventas y sucursales desde archivos CSV y JSON.
- **Mostrar ventas:** Consultar los registros de ventas.
- **Mostrar sucursales:** Visualizar la información de las sucursales.
- **Integrar información:** Unir ambos conjuntos de datos mediante el identificador `sucursal_id`.
- **Ventas por sucursal:** Calcular el importe total de ventas de cada sucursal.
- **Promedio de ventas:** Obtener el promedio de ventas por sucursal.
- **Ranking de sucursales:** Ordenar las sucursales según el importe total de sus ventas.
- **Ventas por ciudad:** Calcular el importe total de ventas agrupado por ciudad.
- **Estadísticas:** Obtener estadísticas descriptivas de las cantidades e importes.
- **Exportar reporte:** Generar un archivo Excel con los resultados obtenidos.

## 🛠️ Tecnologías utilizadas

- Python
- Pandas
- CSV
- JSON
- Excel

## 📂 Estructura del repositorio

```text
Analizador_de_sucursales/
│
├── Analizador_de_Sucursales.py  # Código principal
├── sucursales.json              # Datos de las sucursales
├── ventas.csv                   # Datos de las ventas
└── README.md                    # Documentación del proyecto
```

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/iamdanielgomez/Analizador_de_sucursales.git
```

### 2. Entrar al directorio

```bash
cd Analizador_de_sucursales
```

### 3. Instalar las dependencias

```bash
pip install pandas openpyxl
```

### 4. Ejecutar el programa

```bash
python Analizador_de_Sucursales.py
```

## 📊 Reporte de resultados

El programa permite exportar los análisis realizados a un archivo Excel llamado:

**`reporte_sucursales.xlsx`**

El archivo contiene seis hojas:

| Hoja | Descripción |
|---|---|
| Ventas | Información integrada de ventas y sucursales. |
| Ventas por sucursal | Total de ventas de cada sucursal. |
| Promedio | Promedio de ventas por sucursal. |
| Ranking | Clasificación de sucursales según sus ventas totales. |
| Ventas por ciudad | Total de ventas agrupado por ciudad. |
| Estadísticas | Resumen estadístico de cantidad e importe. |

## 🎯 Objetivo del proyecto

Aplicar herramientas de Python y análisis de datos para transformar información de diferentes fuentes en resultados organizados que permitan interpretar el rendimiento de las sucursales de una empresa.

Este proyecto permite poner en práctica:

- Creación y utilización de funciones.
- Lectura de archivos CSV y JSON.
- Manipulación de datos con Pandas.
- Integración de información con `merge()`.
- Agrupación de datos con `groupby()`.
- Cálculos estadísticos.
- Generación y exportación de reportes en Excel.
- Desarrollo de menús interactivos en consola.

## 👨‍💻 Autor

**Daniel Gómez**

GitHub: [@iamdanielgomez](https://github.com/iamdanielgomez)

---

⭐ Si te gusta este proyecto, puedes dejar una estrella en el repositorio.
