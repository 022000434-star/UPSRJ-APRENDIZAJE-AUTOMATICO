# ============================================================
# Politécnica de Santa Rosa
#
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: [nombre_del_archivo.py]
# Descripción: Archivo de pruebas unitarias para validar el comportamiento de funciones del proyecto
# ============================================================

from main import suma

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0