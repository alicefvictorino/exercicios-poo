class CartaoTransporte:
    
    def __init__(self):
        self.__codigo = 0
        self.__viagens = 0
    
    def __str__(self):
        return 'Código: {}, viagens: {}'.format(self.__codigo , self.__viagens)
    
    def carrega(self, num_viagens):
        if num_viagens > 0:
            self.__viagens += num_viagens
            print("Carregamento confirmado. Viagens: {}".format(num_viagens))
            
        else:
            print('Carregamento inválido: nr. de viagens precisa ser maior que 0')
        
    def usa(self):
        if self.__viagens > 0:
            self.__viagens -= 1
            print("Boa viagem. Viagens: {}".format(self.__viagens))
        else:
            print('Cartão sem viagens disponíveis.')
            
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def viagens(self):
        return self.__viagens
    
    @codigo.setter
    def codigo(self, novo_codigo):
        if type(novo_codigo) != int:
            print('O código precisa ser um nr. inteiro')
        else:
            self.__codigo = novo_codigo

def main():

    c1 = CartaoTransporte()
    
    c1.codigo = 23.5
    print(c1)
    c1.codigo = 1553
    print(c1)

    c1.carrega(-5)
    c1.carrega(3)
    print(c1)

    c1.usa()
    c1.usa()
    c1.usa()
    c1.usa()

    c1.carrega(5)
    print(f'Dados do cartão - Código: {c1.codigo}, viagens: {c1.viagens}')

if __name__ == '__main__':
    main()