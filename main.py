#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:38:35 2019

@author: jairoerazo
Archivo principal para trabajar con kivy
"""
import  kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from clases_testchess import Pregunta, Test

Window.clearcolor = get_color_from_hex("#01A9DB")
Window.size = (300,580)
class Canvas(BoxLayout):
    def on_press_bt(self):
        rtas = []
        self.ids.enunciado.text = preguntas[0].getEnunciado()
        for v in preguntas[0].getRespuestas().values():
            rtas.append(v)
        self.ids.text_r1.text = rtas[0]
        self.ids.text_r2.text = rtas[1]
        self.ids.text_r3.text = rtas[2]
        self.ids.text_r4.text = rtas[3]

class TestChess(App):
    def build(self):
        return Canvas()

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
    preguntas = test.crearListaPreg(content)

    #test.impPreguntas()

display = TestChess()
display.run()
