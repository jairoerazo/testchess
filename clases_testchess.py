# Clase para crear las preguntas del tests
# Por ahora sin soporte para imagenes en el enunciado
class Test:
    def __init__(self, content):
        self.__list_preguntas = []
        self.__index = 0
        self.__score = 0
        # Crear listado de objetos de preguntas
        p_list = []
        for p in content:
            # Eliminar el salto de linea
            p = p.rstrip("\n")
            p_list.append(p.split(","))
        # Lista para almacenar los objetos pregunta
        for pl in p_list:
            self.__list_preguntas.append(Pregunta(pl[0]))
            self.__list_preguntas[-1].setRespuestas(pl[1:-1])
            self.__list_preguntas[-1].setRespCorrecta(int(pl[-1]))

    def impPreguntas(self):
        # list_preguntas es un una lista de objetos tipo Pregunta
        for p in self.__list_preguntas:
            print(p.getEnunciado())
            for v in p.getRespuestas().values():
                print("- ", v)

    def ListQuestions(self):
        return self.__list_preguntas

    def nextQuestion(self):
        if self.__index <= (len(self.__list_preguntas) - 1):
            next_question = self.__list_preguntas[self.__index]
            self.__index += 1
            print("index: ",self.__index)
            return next_question
        else:
            return False

    def currentQuestion(self):
        return self.__list_preguntas[self.__index - 1]

    def getIndex(self):
        return self.__index

    def getResult(self):
        correct = 0
        for q in self.__list_preguntas:
            if q.getRespCorrecta() == q.getRespUsuario():
                correct += 1
        total = len(self.__list_preguntas)
        return (correct, total)

class Pregunta:
    def __init__(self, enunciado = "Enunciado"):
        self.__enunciado = enunciado
        self.__respuestas = {}
        self.__resp_usuario = None
        self.__resp_correcta = None

    def setEnunciado(self, enunciado):
        self.__enunciado = enunciado

    # __respuestas es un diccionario con valores de clave a partir de cero
    def setRespuestas(self, respuestas):
        dict_respuestas = {}
        i = 0
        for r in respuestas:
            dict_respuestas[i] = r
            i += 1
        self.__respuestas = dict_respuestas

    # La respuesta sera un numero de mayor o igual a cero
    # debe corresponer con la clave del diccionario que tenga el valor True
    def setRespUsuario(self, respuesta):
        self.__resp_usuario = respuesta

    def setRespCorrecta(self, num_resp):
        self.__resp_correcta = num_resp

    def getEnunciado(self):
        return self.__enunciado

    def getRespuestas(self):
        return self.__respuestas

    def getRespCorrecta(self):
        return self.__resp_correcta

    def getRespUsuario(self):
        return self.__resp_usuario
