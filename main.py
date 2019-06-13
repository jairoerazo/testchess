#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:38:35 2019

@author: jairoerazo
Archivo principal para trabajar con kivy
"""
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from clases_testchess import Pregunta, Test

Window.clearcolor = get_color_from_hex("#01A9DB")
#Window.size = (300,580)
class MyScreenManager(ScreenManager):
    def __init__(self):
        super(MyScreenManager, self).__init__()

class WindowQuestion(Screen):
    r1 = ObjectProperty(None)
    r2 = ObjectProperty(None)
    r3 = ObjectProperty(None)
    r4 = ObjectProperty(None)

    def set_answer(self):
        rta = None
        if self.r1.active:
            rta = 0
            self.r1.active = False
        if self.r2.active:
            rta = 1
            self.r2.active = False
        if self.r3.active:
            rta = 2
            self.r3.active = False
        if self.r4.active:
            rta = 3
            self.r4.active = False
        return rta

    def load_question(self):
        rtas = []
        next_question = test.nextQuestion()
        if next_question:
            self.ids.enunciado.text = next_question.getEnunciado()
            for v in next_question.getRespuestas().values():
                rtas.append(v)
            self.ids.text_r1.text = rtas[0]
            self.ids.text_r2.text = rtas[1]
            self.ids.text_r3.text = rtas[2]
            self.ids.text_r4.text = rtas[3]

class WindowFeedback(Screen):
    def evaluar_pregunta(self, rta):
        if preguntas[test.getIndex()-1].getRespCorrecta() == rta:
            self.ids.eval.text = "Respuesta correcta"
        else:
            self.ids.eval.text = "Respuesta incorrecta"

class WindowMain(Screen):
    pass

class TestChess(App):
    def build(self):
        return MyScreenManager()

    def on_start(self):
        pass

    def on_pause(self):
        return True

    def on_resume(self):
        pass

# Conexion al archivo de las preguntas
try:
    # Acceder a la fuente de las preguntas
    stream = open("./tests/test-1.1.csv", "rt")
    content = stream.readlines()
    stream.close()
except IOError as e:
    print(e)
else:
    # Imprimir preguntas
    test = Test()
    preguntas = test.crearListaPreg(content)

    #test.impPreguntas()
if __name__ == '__main__':
    display = TestChess()
    display.run()
