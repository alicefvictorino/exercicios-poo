import random

class Musica:
    def __init__(self,artista,titulo):
        self.artista = artista
        self.titulo = titulo
    
    def __str__(self):
        return f'{self.artista} - {self.titulo}'
    
class Playlist:
    def __init__(self, musicas):
        self.__musicas = musicas
    
    def imprime(self):
            print(f'----------')
            for i in self.__musicas:
                 print(i)
            print(f'----------')
    
    def adiciona(self,musicaNova):
        self.__musicas.append(musicaNova)
    
    def toca_proxima(self):
            print(f'Tocando agora: {self.__musicas[0]}')
            self.__musicas.remove(self.__musicas[0])
    
    def embaralha(self):
        random.shuffle(self.__musicas)

def main():
    
    m1 = Musica('Nirvana', 'Smells Like Teen Spirit')
    m2 = Musica('Green Day', 'Basket Case')
    m3 = Musica('The Offspring', 'Original Prankster')
    m4 = Musica('Foo Fighters', 'Everlong')
    m5 = Musica('Avril Lavigne', 'Skater Boy')
    m6 = Musica('Papa Roach', 'Last Resort')
    musicas = [m1, m2, m3]

    pl = Playlist(musicas)
    pl.imprime()

    pl.adiciona(m4)
    pl.imprime()

    pl.toca_proxima()
    pl.toca_proxima()
    pl.imprime()

    pl.adiciona(m5)
    pl.adiciona(m6)
    pl.embaralha()
    pl.imprime()

if __name__ == '__main__':

    main()