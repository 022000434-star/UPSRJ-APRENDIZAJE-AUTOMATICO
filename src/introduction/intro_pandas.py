# ============================================================
# Politécnica de Santa Rosa
#
# Materia: Aprendizaje automático
# Profesor: Jesús Salvador López Ortega
# Grupo: IRC02
# Archivo: pandas.py
# Descripción: Ejercicios básicos de manejo de pandas
# ============================================================
import pandas as pd
#########################################################################
# NOTE: Revisa la API de Pandas en https://pandas.pydata.org/docs/      #
#########################################################################

# Ejercicio 1
#
# TODO: Crea una función "csv_registers" que reciba un CSV y devuelva la cantidad de registros (int).
#       así como el contenido en un DataFrame en un tuple(int, DataFrame).
# NOTE: https://pandas.pydata.org/docs/dev/reference/api/pandas.read_csv.html
def csv_registers(file: str) -> int:
    data = None
    registers = None
    return (registers, data)

# Ejercicio 2
#
# TODO: Crea una función "json_registers" que reciba un JSON y devuelva la cantidad de registros (int).
#       así como el contenido en un DataFrame en un tuple(int, DataFrame).
# NOTE: https://pandas.pydata.org/docs/dev/reference/api/pandas.read_json.html
def json_registers(file: str) -> tuple:
    data = None
    registers = None
    return (registers, data)

# Ejercicio 3
#
# TODO: Crea una función "yaml_registers" que reciba un YAML y devuelva la cantidad de registros (int)
#       así como el contenido en un DataFrame en un tuple(int, DataFrame).
# NOTE: https://pyyaml.org/wiki/PyYAMLDocumentation
def yaml_registers(file: str) -> tuple:
    data = None
    registers = None
    return (registers, data)

# Ejercicio 4
# TODO: Crea una función "get_head" que devuelva un DataFrame solo con los primeros n registros de otro DataFrame.
# NOTE: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html
def get_head(df: pd.DataFrame, n: int) -> pd.DataFrame:
    df_head = None
    return df_head

# Ejercicio 5
# TODO: Crea una función "get_above" que devuelva un Dataframe solo con los elementos que cumplan la cualidad de ser
#       mayores al valor de entrada "n" en la columna "col" del DataFrame "df" a la entrada. 
# NOTE: https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#dataframe
def get_above(df: pd.DataFrame, col: str, n: int) -> pd.DataFrame:
    above = None
    return above

# Ejercicio 6
# TODO: Crea una función "group_and_average" que agrupe un DataFrame de entrada conforme a la columna "group" de entrada
#       y calcule el promedio de la columna "avg" de entrada. Dadas las cualidades de las columnas de 
#       entrada, debe devolver un objeto Series.
# NOTE: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
def group_and_average(df: pd.DataFrame, group: str, avg: str) -> pd.Series:
    grouped = None
    return grouped

# Ejercicio 7
# TODO: Crea una función "count_in_col" que cuente elementos "item" en un DataFrame de entrada 
#       de una columna "col" de entrada. La salida debe ser el conteo de elementos (int).
def count_in_col(df: pd.DataFrame, item: str, col: str) -> int:
    count = None
    return count 

# Ejercicio 8
# TODO: Crea una función "export_data" que exporte un DataFrame de entrada a un archivo CSV "file" de entrada.
# NOTE: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
def export_data(df: pd.DataFrame, file: str):
    pass

# Ejercicio 9
# TODO: Crea una función "compare_dfs" que compare dos DataFrame de entrada y devuelva un True (bool) si son iguales
#       o bien, un False (bool) si no lo son.
def compare_dfs(df1: pd.DataFrame, df2: pd.DataFrame) -> bool:
    equal = None
    return equal

