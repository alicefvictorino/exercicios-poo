
class DataHora:
    def __init__(self,dia, mes, ano, hora, min):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.hora = hora
        self.min = min

    def __str__(self):
        return '{}/{}/{}, {}:{}'.format(self.dia, self.mes, self.ano, self.hora, self.min)

class Evento:
    def __init__(self, nome, dia, mes, ano, hora, min):
        self.nome = nome
        self.data = DataHora(dia, mes, ano, hora, min)
          
    def Getnome(self):
        return self.nome

    def Setnome(self,nome_novo):
            self.nome = nome_novo

    def chave(self):
        return '{}/{}/{}, {}:{}'.format(self.dia, self.mes, self.ano, self.hora, self.min)

    def __str__(self):
        return ('{} - {}/{}/{}, {}:{}').format(self.nome, self.data.dia, self.data.mes, self.data.ano, self.data.hora, self.data.min)

class Agenda:
    def __init__(self):
        self.eventos = []

    def adiciona(self, ev):
        self.eventos.append(ev)
        print('Evento "{}" adicionado à agenda'.format(ev))

    def remove(self, nomeRemovido):
        for i in self.eventos:
            if i.nome == nomeRemovido:
                self.eventos.remove(i)
                print('Evento "{} removido da agenda'.format(nomeRemovido))

    def atualiza(self, nomeFornecido, novoNome):
        existe = False
        for i in self.eventos:
            if i.nome == nomeFornecido:
                i.Setnome(novoNome)
                print('"{}" atualizado para "{}"'.format(nomeFornecido, novoNome))
                existe = True
        if existe == False:
            print('Evento "{}" não encontrado: atualização não realizada'.format(nomeFornecido))        

    def imprime(self):
        print('Agenda:')
        for i in self.eventos:
            print(i)
        

def main():
    ev1 = Evento('Aula de Inglês', 18, 4, 2023, 14, 55)
    ev2 = Evento('Aula de POO', 25, 4, 2023, 14, 55)
    ev3 = Evento('Evento Importante', 27, 4, 2023, 14, 55)
    ev4 = Evento('Academia', 25, 4, 2023, 14, 55)

    ag = Agenda()
    ag.adiciona(ev1)
    ag.adiciona(ev2)
    ag.adiciona(ev3)
    ag.adiciona(ev4)

    ag.imprime()

    ag.remove('Dentista')
    ag.remove('Aula de Inglês')

    ag.atualiza('Dentista', 'Prova de POO')
    ag.atualiza('Evento Importante', 'Prova de POO')
    ag.imprime()

if __name__ == '__main__':
    main()