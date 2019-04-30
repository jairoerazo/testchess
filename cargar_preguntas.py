#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:38:35 2019

@author: jairoerazo
Archivo de conexion a la fuente de datos de las preguntas
Devuelve las preguntas en forma de un listado de objetos
"""
from clases_testchess import Pregunta, Test

# Conexion al archivo de las preguntas
try:
    # Acceder a la fuente de las preguntas
    stream = open("./tests/tests.csv", "rt")
    content = stream.readlines()
    stream.close()
except IOError as e:
    print(e)
else:
    # Imprimir preguntas
    test = Test()
    test.crearListaPreg(content)
    test.impPreguntas()
