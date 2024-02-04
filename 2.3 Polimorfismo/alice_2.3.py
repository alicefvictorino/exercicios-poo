class Matriz:
    '''Representa uma matriz de tamanho nl x nc.'''

    def __init__(self, nl, nc):
        self._nl = nl
        self._nc = nc
        self._dados = []
        self._inicializa()

    def _inicializa(self):
        '''Inicializa a matriz com 0s.'''
        for i in range(self._nl):
            self._dados.append([])
            for j in range(self._nc):
                self._dados[i].append(0.0)

    def __repr__(self):
        '''Retorna a matriz em formato de str''' 
        s = ''
        for i in range(self._nl):
            for j in range(self._nc):
                s += f'{self._dados[i][j]} '
            s += '\n'
        return s

    def seta_valores(self, valores):
        '''Atribui valores em lista de listas à matriz.'''
        if len(valores) != self._nl or len(valores[0]) != self._nc:
            print('Lista de valores com tamanho incompatível')
        else:
            for i, lin in enumerate(valores):
                for j, v in enumerate(lin):
                    self._dados[i][j] = v
    
    def _checa_dimensoes(self, b, op):

        if op == 'soma':
            if b._nl == self._nl and b._nc == self._nc:
                return True
            else:
                return False

        if op == 'multiplicacao':
            if self._nc == b._nl:
                return True
            else:
                return False

        '''Retorna falso se as dimensões da matriz não são
           compatíveis com as dimensões do parâmetro b, de
           acordo com a op (soma ou multiplicação) desejada.
        '''
    
    def __getitem__(self, pos):
        '''Operador []: permite acessar
           um elemento da matriz através de m[i,j].
        '''
        if type(pos) != tuple:
            print('pos deve ser do tipo tuple')
        else:
            l, c = pos
            if l >= self._nl or c >= self._nc:
                print('indice fora da matriz')
            else:
                return self._dados[l][c]

    def __setitem__(self, pos, v):
        '''Operador []: permite atribuir um valor
           a um elemento da matriz através de m[i,j].
        '''
        if type(pos) != tuple:
            print('pos deve ser do tipo tuple')
        else:
            l, c = pos
            if l >= self._nl or c >= self._nc:
                print('indice fora da matriz')
            else:
                self._dados[l][c] = v

    def __add__(self, b):
        MatrizNova = Matriz(b._nl,b._nc)

        if self._checa_dimensoes(b,'soma') == True:
            for i in range(b._nl):
                for j in range (b._nc):
                    MatrizNova[i,j] = b[i,j] + self[i,j]

            return MatrizNova
        else:
            print('Erro: a matriz não pode ser somada')
        

    def __mul__(self, b):
        if isinstance(b, Matriz):
            MatrizNova = Matriz(b._nl, b._nc)

            if self._checa_dimensoes(b,'multiplicacao') == True:
                for i in range(self._nl):
                    for j in range (self._nc):
                        MatrizNova[i,j] = 0,0

            else:
                print('Erro: a matriz não pode ser multiplicada')
            
            return MatrizNova

        if isinstance(b, int): 
            for i in range(self._nl):
                    for j in range (self._nc):
                        self[i,j] = self[i,j]*b
            return self

    def __eq__(self, b):
        igual = False
        for i in range(self._nl):
            for j in range (self._nc):
                    if self[i,j] != b[i,j]:
                        igual = True
                        
        if igual == False:
            print('A == B: True')
            return True
        else:
            self.__ne__(b)
        
    def __ne__(self, b):
        igual = False
        for i in range(self._nl):
            for j in range (self._nc):
                    if self[i,j] == b[i,j]:
                        igual = True

        if igual == False:
            print('A != B: True')
            return True
        else:
            return False

    @staticmethod
    def identidade(n):
        MatrizIdentidade = Matriz(n,n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    MatrizIdentidade[i,j] = 1.0
                else:
                    MatrizIdentidade[i,j] = 0.0
        return MatrizIdentidade

def main():
    a = Matriz(3, 3)
    a[0,2] = 1
    a[1,1] = 1
    a[2,0] = 1
    print('Matriz a:')
    print(a)

    b = Matriz(3, 3)
    b.seta_valores([[1.0, 2.0, 0.0],
                    [2.0, 4.0, 5.0],
                    [3.0, 3.0, 0.0]])
    
    mat_soma = a + b
    print('A + B:')
    print(mat_soma)

    mat_prod = a * b
    print('A * B:')
    print(mat_prod)

    mat_prod = b * 5
    print('B * escalar:')
    print(mat_prod)

    print(f'A != B: {a!=b}')
    b.seta_valores([[0, 0, 1],
                    [0, 1, 0],
                    [1, 0, 0]])
    print(f'A == B: {a==b}')
    
    ident = Matriz(3,3)
    print(Matriz.identidade(3))

if __name__ == "__main__":
    main()
