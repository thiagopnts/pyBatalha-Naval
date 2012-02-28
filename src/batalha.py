from string import ascii_uppercase
from string import digits

class Barco:
    nome = ''
    tam = 0

    def __init__(self, nome, tam):
        self.nome = nome
        self.tam = tam

    def __eq__(self, barco):
        return self.nome == barco.nome

class MainGame:

    def criarJogo(self, larg, alt):
        if larg <= 0:
            raise Exception('Largura invalida: %d' %larg)
        elif alt <= 0:
            raise Exception('Altura invalida: %d' %alt)
        elif alt < 2 or larg < 2 :
            raise Exception('Largura e Altura devem ser maiores que 2')
        self.tabuleiros = [Tabuleiro(larg, alt), Tabuleiro(larg, alt)]
        self.larg = larg
        self.alt = alt
        self.barcos_do_jogo = {}
        self.barcos1 = []
        self.barcos2 = []

    def getLarguraTabuleiro(self):
        return self.larg

    def getAlturaTabuleiro(self):
        return self.alt

    def addBarcoNoJogo(self, nome, tam):
        if tam <= 0:
            raise Exception("Tamanho de embarcacao invalido: %d" %tam)
        if nome == '':
            raise Exception("Nome invalido ''")
        elif tam > self.larg and tam > self.alt:
            raise Exception("Barco nao cabe no tabuleiro")
        for letter in nome:
            if letter not in ascii_uppercase and letter not in digits \
                    and letter not in ['_','-','.']:
                raise Exception("Nome deve conter apenas os seguintes caracteres (A..Z), (0..9) e (_-.)")
        b = Barco(nome, tam)
        if b.nome not in self.barcos_do_jogo.keys():
            self.barcos_do_jogo[b.nome] = b
        else:
            raise Exception("Ja existe um barco com nome '%s' no jogo" % b.nome)

    def addBarcoNoTabuleiro(self, tab, nome, x1, y1, x2, y2):
        if nome not in self.barcos_do_jogo.keys():
            raise Exception("Barco invalido '%s'" % nome)
        coord = (
                self.tabuleiros[tab-1].getAlturaTabuleiro(),
                self.tabuleiros[tab-1].getLarguraTabuleiro() 
                )
        b = self.barcos_do_jogo[nome]
        if coord < (x1-1, y1-1):
            raise Exception("Posicao invalida: fora do tabuleiro linha=%d coluna=%d" %(x1,y1))
        elif coord < (x2-1, y2-1):
            raise Exception("Posicao invalida: fora do tabuleiro linha=%d coluna=%d" %(x2,y2))
        if (x1 == x2 and ((y1 - y2)*-1)+1 > b.tam): 
            raise Exception("Posicao invalida: maior que barco (%d > %d)" % (y2,b.tam))
        if (y1 == y2 and ((x1-x2)*-1)+1 > b.tam):
            raise Exception("Posicao invalida: maior que barco (%d > %d)" % (x2,b.tam))
        elif (x1 == x2 and ((y1-y2)*-1)+1 < b.tam):
            raise Exception("Posicao invalida: menor que barco (%d < %d)" % (y2,b.tam))
        elif (y1 == y2 and ((x1-x2)*-1)+1 < b.tam):
            raise Exception("Posicao invalida: maior que barco (%d < %d)" % (x2,b.tam))
        elif x1 != x2 and y1 != y2:
            raise Exception("Posicao invalida: barco deve estar na vertical ou horizontal")
        if tab == 1 and b in self.barcos1 or tab == 2 and b in self.barcos2:
            raise Exception("O barco '%s' ja existe no tabuleiro %d" % (nome,tab))
        self.__add_to_tab(tab, nome, x1, y1, x2, y2)

    def __add_to_tab(self, tab, nome, x1, y1, x2, y2):
        barco = self.barcos_do_jogo[nome]
        tabuleiro = self.tabuleiros[tab-1]
        for i in range(tabuleiro.getAlturaTabuleiro()):
            for j in range(tabuleiro.getLarguraTabuleiro()):
                if i == (x1-1) and j == (y1-1):
                    if x2 > x1:
                        for k in range(x1-1, x2):
                            if type(tabuleiro.tab[k][j]) != 'int':
                                tabuleiro.tab[k][j] = barco
                            else:
                                raise Exception("conflito de coordenada com barco '%s'" %(tabuleiro.tab[k][j].nome))
                    elif x1 == x2 and i == x2-1:
                        for k in range(y1-1, y2):
                            tabuleiro.tab[i][k] = barco
        
    def getQuantidadeBarcos(self):
        return len(self.barcos_do_jogo)


class Tabuleiro:
    def __init__(self, larg, alt):
        self.__larg = larg
        self.__alt = alt
        self.tab = self.__alt*[self.__larg*[0]]

    def setLarguraTabuleiro(self, larg):
        self.__larg = larg

    def getLarguraTabuleiro(self):
        return self.__larg

    def setAlturaTabuleiro(self, alt):
        self.__alt = alt

    def getAlturaTabuleiro(self):
        return self.__alt

    def getTabuleiro(self):
        return self.tab



