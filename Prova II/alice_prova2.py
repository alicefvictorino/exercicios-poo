

from abc import ABC, abstractmethod
import math
import random
from desenho import QuadroDeDesenho
from typing import Dict, List


class Forma:
    """Representa uma forma geométrica"""
    cores = ('blue', 'yellow', 'red', 'green', 'cyan', 'black')
    '''Atributos de classe contidos em uma tupla que representam cores que a forma geométrica pode assumir'''

    def __init__(self, x: float, y: float):
        '''Cria um objeto do tipo Forma'''
        self.cor = random.choice(self.cores)
        self.x = x
        self.y = y
        self.centro = [self.x, self.y]

    @staticmethod
    def distancia(f1: 'Forma', f2: 'Forma') -> float:
        '''Calcula a distância entre duas formas geométricas f1 e f2'''
        a = (f1.x-f2.x)**2 + (f1.y-f2.y)**2
        return math.sqrt(a)

    @abstractmethod
    def desenha(self) -> None:
        '''Desenha uma forma geométrica na tela'''
        pass

class Circulo(Forma):
    '''Representa a forma geométrica círculo'''

    def __init__(self, x, y, raio: float):
        Forma.__init__(self, x, y)
        self.raio = raio

    def desenha(self) -> List:
        '''Desenha um círculo'''
        lista_desenho = [(self.x-self.raio),(self.y-self.raio),(self.x+self.raio),(self.y+self.raio)]
        return lista_desenho

class Poligono(Forma):
    '''Representa a forma geométrica de um polígono qualquer'''

    def __init__(self, x, y):
        '''Cria um objeto Poligono'''
        Forma.__init__(self, x, y)
        self.vertices = [(self.x,self.y)]

    @abstractmethod
    def desenha(self)-> None:
        '''Desenha um polígono'''
        coordenadas = []
        for i in self.vertices:
            i[0] += self.x
            i[1] += self.y
            coordenadas.append(i)

class Retangulo(Poligono):
    '''Representa a forma geométrica retângulo'''

    def __init__(self, x, y, base: float, altura: float):
        '''Cria um objeto Retangulo'''
        Poligono.__init__(self, x, y)
        self.b = base
        self.h = altura
        self.vertices = [(-self.b/2,-self.h/2),(self.b/2,self.h/2),(self.b/2,-self.h/2),(self.b/2,-self.h/2)]

    def desenha(self) -> None:
        '''Chama um método da classe polígono para desenhar um retângulo'''
        Poligono.desenha(self)

class TrianguloIsosceles(Poligono):
    '''Representa a forma geométrica triângulo'''

    def __init__(self, x, y, base: float, altura: float):
        '''Cria objeto TrianguloIsosceles'''
        Poligono.__init__(self, x, y)
        self.b = base
        self.h = altura

    def desenha(self) -> None:
        '''Chama um método da classe polígono para desenhar um triângulo isóceles'''
        Poligono.desenha(self)



def main():

    c = Circulo(50, 50, 10) # circulo na posicao 50,50 com raio 10
    t1 = TrianguloIsosceles(100, 50, 50, 60) # triangulo isosc. na posicao 100,50 com base 50 e altura 60
    r = Retangulo(50, 100, 70, 10) # retangulo na posicao 50,100 com base 70 e altura 10
    t2 = TrianguloIsosceles(200, 200, 40, 40)

    # Coloque aqui a chamada para calcular a distância entre o objeto c e t1
    dist_c_t1 = Circulo.distancia(c, t1)
    print(f'Distância entre o círculo e o triângulo1: {dist_c_t1}')

    # Coloque aqui a chamada para calcular a distância entre o objeto c e r
    dist_c_r = Circulo.distancia(c, r)
    print(f'Distância entre o círculo e o retângulo: {dist_c_r}')

    # Coloque aqui a chamada para calcular a distância entre o objeto c e t2
    dist_c_t2 = Circulo.distancia(c, t2)
    print(f'Distância entre o círculo e o triângulo2: {dist_c_t2}')

    #quadro = QuadroDeDesenho()
    #quadro.adiciona_forma(c)
    #quadro.adiciona_forma(t1)
    #quadro.adiciona_forma(r)
    #quadro.adiciona_forma(t2)
    #quadro.desenha()
    


if __name__ == '__main__':
    main()