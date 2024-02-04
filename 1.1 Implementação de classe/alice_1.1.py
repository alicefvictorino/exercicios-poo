class ContaBancaria:

    def __init__(self,conta,agencia,saldo):
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo
        
    def deposito(self,quantia):
        if(quantia <= 0):
            print('Valor para depósito inválido.')
        else:
            self.saldo = self.saldo + quantia
    
    def saque(self,quantia):
        if(quantia > 0):
            if(self.saldo < quantia):
                print("Saldo insuficiente na conta.")
            else:
                self.saldo = self.saldo - quantia
        else:
            print('Valor inválido para saque.')
            
    def mesma_agencia(self,cb):
        if(self.conta == cb.conta):
            print('Mesma agência')
        
    def __str__(self):
        return 'Ag: {}, conta: {}, saldo: R${}'.format(self.agencia,self.conta,self.saldo)

def main():
    c1 = ContaBancaria(100, 2, 1000.0)
    c2 = ContaBancaria(200, 8, 500.0)
    c3 = ContaBancaria(300, 2, 2000.0)

    c1.deposito(-5) # valor inválido para depósito
    c1.saque(-5) # valor inválido para saque
    print(c1)

    c1.deposito(100)
    c1.saque(1200) # saldo insuficiente
    c1.saque(600)
    print(c1)

    c1.mesma_agencia(c2) # não têm mesma agência
    c1.mesma_agencia(c3) # têm mesma agência

if __name__ == '__main__':
    main()