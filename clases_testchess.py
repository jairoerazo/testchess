# Clase para crear las preguntas del tests
# Por ahora sin soporte para imagenes en el enunciado
class Test:
    def __init__(self):
        self.__list_preguntas = []

    def impPreguntas(self):
        # list_preguntas es un una lista de objetos tipo Pregunta
        for p in self.__list_preguntas:
            print(p.getEnunciado())
            for v in p.getRespuestas().values():
                print("- ", v)

    def crearListaPreg(self, content):
        # Crear listado de objetos de preguntas
        p_list = []
        for p in content:
            # Eliminar el salto de linea
            p = p.rstrip("\n")
            p_list.append(p.split(","))
        # Lista para almacenar los objetos pregunta
        p_obj_list = []
        for pl in p_list:
            p_obj_list.append(Pregunta(pl[0]))
            p_obj_list[-1].setRespuestas(pl[1:-1])
            p_obj_list[-1].setRespCorrecta(int(pl[-1]))
        self.__list_preguntas = p_obj_list
        return p_obj_list

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

class Bidirectional_iterator(object):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        try:
            result = self.collection[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration
        return result

    def prev(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]

    def __iter__(self):
        return self
