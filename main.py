#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:38:35 2019

@author: jairoerazo
Archivo principal para trabajar con kivy
"""
import sys
import kivy
from kivy.uix.scatter import Scatter
from kivy.graphics.svg import Svg
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import SlideTransition
from clases_testchess import Pregunta, Test

Window.clearcolor = get_color_from_hex("#2E9AFE")
#Window.size = (300,580)

#Clase para gestionar las pantallas
#    def __init__(self):
#        super(MyScreenManager, self).__init__()
Builder.load_file('testchess.kv')

class WindowQuestion(Screen):
    r1 = ObjectProperty(None)
    r2 = ObjectProperty(None)
    r3 = ObjectProperty(None)
    r4 = ObjectProperty(None)
    level = NumericProperty(None)
    test = ObjectProperty(None)

    def set_answer(self):
        rta = None
        #Verificar el radiobutton que se seleccionó
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

        self.test.currentQuestion().setRespUsuario(rta)
        return rta

    def load_testfile(self, level, sublevel):
        file_name = "./tests/level_" + str(level) + "/test_" + str(level) + "." + str(sublevel) + ".csv"
        # Conexion al archivo de las preguntas
        try:
            # Acceder a la fuente de las preguntas
            stream = open(file_name, "rt")
            content = stream.readlines()
            stream.close()
        except IOError as e:
            print("Este es el error",e)
        else:
            # Imprimir preguntas
            self.test = Test(content)
            self.load_question()
            #test.impPreguntas()

    def load_question(self):
        next_question = self.test.nextQuestion()
        if next_question:
            filename = "boards/board.svg"
            #Imprimir el tablero svg
            svg = SvgWidget(filename, size_hint=(None, None), pos_hint={'center_x': 0.5, 'top': 1})
            self.add_widget(svg)
            svg.scale = 1
            #Obtener pregunta y sus respuestas
            rtas = []
            self.ids.enunciado.text = next_question.getEnunciado()
            for v in next_question.getRespuestas().values():
                rtas.append(v)
            self.ids.text_r1.text = rtas[0]
            self.ids.text_r2.text = rtas[1]
            self.ids.text_r3.text = rtas[2]
            self.ids.text_r4.text = rtas[3]
        else:
            #Llamar ventana de fin del test
            MyScreenManager.current = 'endtest'
            correct, total = self.test.getResult()
            #Asignar el texto de los puntos ganados al label correspondiente
            MyScreenManager.get_screen('endtest').ids.id_result.text = "{} puntos de {}".format(
                correct, total
            )

class WindowFeedback(Screen):
    def evaluar_pregunta(self, rta, test):
        #obtener la pregunta desplegada actualmente
        question = test.currentQuestion()
        #comparar la respuesta del usuario con la respuesta correcta
        if question.getRespCorrecta() == rta:
            self.ids.eval.text = "Respuesta correcta"
        else:
            self.ids.eval.text = "Respuesta incorrecta"

class WindowEndTest(Screen):
    pass

class WindowMain(Screen):
    pass

class WindowLevels(Screen):
    def load_levels(self, level):
        pass

class SvgWidget(Scatter):

    def __init__(self, filename, **kwargs):
        super(SvgWidget, self).__init__(**kwargs)
        with self.canvas:
            svg = Svg(filename)
        self.size = svg.width, svg.height

#Creo el gestor de pantallas y agrego las pantallas existentes
MyScreenManager = ScreenManager(transition=SlideTransition())
MyScreenManager.add_widget(WindowMain(name= 'main'))
MyScreenManager.add_widget(WindowQuestion(name= 'question'))
MyScreenManager.add_widget(WindowFeedback(name= 'feedback'))
MyScreenManager.add_widget(WindowLevels(name= 'levels'))
MyScreenManager.add_widget(WindowEndTest(name= 'endtest'))
MyScreenManager.current = 'main'

class TestChess(App):
    def build(self):
        return MyScreenManager

    def on_start(self):
        pass

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':
    TestChess().run()
