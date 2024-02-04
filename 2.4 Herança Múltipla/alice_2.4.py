class PreProcessador:
    def __init__(self, texto):
        self._texto = texto
        self._lista_palavras = []
    
    def processa(self):
        
        self._lista_palavras = self._texto.split(" ")

        for i in self._lista_palavras:
            if i[-1].isalpha() == False:
                i.strip(i[-1])

    def __repr__(self):
        return f'{self._lista_palavras}'

class ContadorPalavras(PreProcessador):
    def __init__(self, texto):
        PreProcessador.__init__(self,texto)
        self._ocorrencias = {}

    def processa(self):
        PreProcessador.processa(self)
        for i in self._lista_palavras:
            if i in self._ocorrencias:
                self._ocorrencias[i] += 1
            else:
                self._ocorrencias[i] = 1

    def __repr__(self):
        s = "Frequência das palavras: "
        return s + f'{self._ocorrencias}'
            
        
class Tradutor(PreProcessador):
    def __init__(self, texto):
        PreProcessador.__init__(self,texto)
        self._traducoes = {"olá": "hello", "este": "this", "é": "is", "um": "an", 
        "exemplo": "exemple", "de": "of", "texto": "text", "com": "with", "termos": "terms",
         "repetidos": "repeated", "possui": "has", "vários": "many"}
        self._lista_palavras_trad = []

    def processa(self):
        PreProcessador.processa(self)
        for i in self._lista_palavras:
            if i in self._traducoes:
                self._lista_palavras_trad.append(self._traducoes[i])
    
class ProcessadorTexto(ContadorPalavras, Tradutor):
    def __init__(self, texto):
        ContadorPalavras.__init__(self, texto)
        Tradutor.__init__(self,texto)
    
    def processa(self):
        ContadorPalavras.processa(self)
        Tradutor.processa(self)

    def __repr__(self):
        return f'Tradução robótica: {self._lista_palavras_trad}'


if __name__ == '__main__':
    #
    # Descomente a seguir para testar apenas a classe PreProcessador
    preprocessador = PreProcessador('OLá! Este é um exemplo de texto com termos repetidos.'
                                     ' Este texto possui vários termos repetidos:'
                                     ' este, Este, ESte, esTE!')
    preprocessador.processa()
    print(preprocessador)
    
    # Descomente a seguir para testar apenas a classe ContadorPalavras
    contador = ContadorPalavras('OLá! Este é um exemplo de texto com termos repetidos.'
                                 ' Este texto possui vários termos repetidos:'
                                 ' este, Este, ESte, esTE!')
    contador.processa()
    print(contador)

    # Descomente a seguir para testar apenas a classe Tradutor
    tradutor = Tradutor('OLá! Este é um exemplo de texto com termos repetidos.'
                          'Este texto possui vários termos repetidos:'
                          'este, Este, ESte, esTE!')
    tradutor.processa()
    print(tradutor)

    processadortexto = ProcessadorTexto('OLá! Este é um exemplo de texto com termos repetidos.'
                                        ' Este texto possui vários termos repetidos:'
                                        ' este, Este, ESte, esTE!')
    processadortexto.processa()