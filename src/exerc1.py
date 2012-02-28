
import unittest
from batalha import MainGame

class BatalhaTest(unittest.TestCase):
    
    '''

    Alguns testes do modulo batalha

    '''

    def setUp(self):
        self.game = MainGame()

    def test_1(self):

        try:
            self.assertRaises(Exception, self.game.criarJogo(2, 3))
        except Exception as e:
            self.assertEquals("Largura e Altura devem ser maiores que 2", e.message)

        try:
            self.assertRaises(Exception, self.game.criarJogo(3, 2))
        except Exception as e:
            self.assertEquals("Largura e Altura devem ser maiores que 2", e.message)

        try:
            self.assertRaises(Exception, self.game.criarJogo(-1, 15))
        except Exception as e:
            self.assertEquals("Largura invalida: -1", e.message)

        try:
            self.assertRaises(Exception, self.game.criarJogo(0, 15))
        except Exception as e:
            self.assertEquals("Largura invalida: 0", e.message)

        try:
            self.assertRaises(Exception, self.game.criarJogo(15, -1))
        except Exception as e:
            self.assertEquals("Altura invalida: -1", e.message)
        
        try:
            self.assertRaises(Exception, self.game.criarJogo(15, 0))
        except Exception as e:
            self.assertEquals("Altura invalida: 0", e.message)
        
        try:
            self.assertRaises(Exception, self.game.criarJogo(-1, -1))
        except Exception as e:
            self.assertEquals("Largura invalida: -1", e.message)

        self.game.criarJogo(20, 10)

        self.assertEquals(20, self.game.getLarguraTabuleiro())
        self.assertEquals(10, self.game.getAlturaTabuleiro())
        self.assertFalse(self.game.getQuantidadeBarcos())

        try:
            self.assertRaises(Exception, self.game.addBarcoNoJogo("%#", 3))
        except Exception as e:
            self.assertEquals("Nome deve conter apenas os seguintes caracteres (A..Z), (0..9) e (_-.)",e.message)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoJogo("&&6", 3))
        except Exception as e:
            self.assertEquals("Nome deve conter apenas os seguintes caracteres (A..Z), (0..9) e (_-.)",e.message)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoJogo("", 3))
        except Exception as e:
            self.assertEquals("Nome invalido ''",e.message)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoJogo("BARCO_GRANDE", 21))
        except Exception as e:
            self.assertEquals("Barco nao cabe no tabuleiro",e.message)

        self.game.addBarcoNoJogo("BARCO_GRANDE", 15)
        self.assertTrue(self.game.getQuantidadeBarcos())

        try:
            self.assertRaises(Exception, self.game.addBarcoNoJogo("BARCO_GRANDE", 15))
        except Exception as e:
            self.assertEquals("Ja existe um barco com nome 'BARCO_GRANDE' no jogo", e.message)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1, "LANCHA", 1, 1, 4, 1))
        except Exception as e: 
            self.assertEquals("Barco invalido 'LANCHA'", e.message)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1, "BARCO_GRANDE", 1, 1, 15, 1))
        except Exception as e: 
            self.assertEquals("Posicao invalida: fora do tabuleiro linha=15 coluna=1", e.message)
        
        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1, "BARCO_GRANDE", 1, 1, 1, 16))
        except Exception as e: 
            self.assertEquals("Posicao invalida: maior que barco (16 > 15)", e.message)
        
        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1, "BARCO_GRANDE", 1, 1, 1, 14))
        except Exception as e: 
            self.assertEquals("Posicao invalida: menor que barco (14 < 15)", e.message)
        
        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1, "BARCO_GRANDE", 1, 1, 2, 15))
        except Exception as e: 
            self.assertEquals("Posicao invalida: barco deve estar na vertical ou horizontal", e.message)
        self.game.addBarcoNoTabuleiro(1,"BARCO_GRANDE",1, 1, 1, 15)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1,"BARCO_GRANDE",2, 1, 2, 15))
        except Exception as e: 
            self.assertEquals("A barco 'BARCO_GRANDE' ja existe no tabuleiro 1", e.message)

        self.game.addBarcoNoJogo("LANCHA", 3)
        self.assertEquals(2, self.game.getQuantidadeBarcos())

        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1,"LANCHA", 1, 3, 3, 3))
        except Exception as e: 
            self.assertEquals("Posicao invalida: conflito de coordenada com barco 'BARCO_GRANDE'", e.message)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1,"LANCHA", 1, 1, 3, 1))
        except Exception as e: 
            self.assertEquals("Posicao invalida: conflito de coordenada com barco 'BARCO_GRANDE'", e.message)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1,"LANCHA", 1, 15, 3, 15))
        except Exception as e: 
            self.assertEquals("Posicao invalida: conflito de coordenada com barco 'BARCO_GRANDE'", e.message)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1,"LANCHA", 1, 16, 4, 16))
        except Exception as e: 
            self.assertEquals("Posicao invalida: maior que barco (4 > 3)", e.message)

        
        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1,"LANCHA", 1, 16, 2, 16))
        except Exception as e: 
            self.assertEquals("Posicao invalida: maior que barco (2 < 3)", e.message)

        try:
            self.assertRaises(Exception, self.game.addBarcoNoTabuleiro(1,"LANCHA", 2, 1, 4, 4))
        except Exception as e: 
            self.assertEquals("Posicao invalida: barco deve estar na vertical ou horizontal", e.message)
        
    def test_new_game(self):
        jogo = MainGame()
        jogo.criarJogo(15, 15)
        self.assertEquals(15, jogo.getLarguraTabuleiro())
        self.assertEquals(15, jogo.getAlturaTabuleiro())
        self.assertEquals(0, jogo.getQuantidadeBarcos())

        try:
            self.assertRaises(Exception, jogo.addBarcoNoJogo("LANCHA", 0))
        except Exception as e:
            self.assertEquals("Tamanho de embarcacao invalido: 0", e.message)

        try:
            self.assertRaises(Exception, jogo.addBarcoNoJogo("LANCHA", -1))
        except Exception as e:
            self.assertEquals("Tamanho de embarcacao invalido: -1", e.message)
        
        try:
            self.assertRaises(Exception, jogo.addBarcoNoJogo("LANCHA", 16))
        except Exception as e:
            self.assertEquals("Barco nao cabe no tabuleiro", e.message)

        jogo.addBarcoNoJogo("PORTA_AVIOES", 5)
        jogo.addBarcoNoJogo("DESTROYER", 4)
        jogo.addBarcoNoJogo("CRUZADOR", 4)
        jogo.addBarcoNoJogo("SUBMARINO", 3)
        jogo.addBarcoNoJogo("PATRULHA", 2)
        
        jogo.addBarcoNoTabuleiro(1, "PORTA_AVIOES", 7, 4, 11, 4)
        jogo.addBarcoNoTabuleiro(1, "DESTROYER", 5, 7, 5, 10)
        jogo.addBarcoNoTabuleiro(1, "CRUZADOR", 11, 9, 11, 12)
        jogo.addBarcoNoTabuleiro(1, "SUBMARINO", 2, 2, 4, 2)
        jogo.addBarcoNoTabuleiro(1, "PATRULHA", 14, 6, 14, 7)

        jogo.addBarcoNoTabuleiro(1, "PORTA_AVIOES", 6, 6, 6, 10)
        jogo.addBarcoNoTabuleiro(1, "DESTROYER", 12, 5, 12, 8)
        jogo.addBarcoNoTabuleiro(1, "CRUZADOR", 2, 3, 2, 6)
        jogo.addBarcoNoTabuleiro(1, "SUBMARINO", 7, 3, 9, 3)
        jogo.addBarcoNoTabuleiro(1, "PATRULHA", 10, 13, 11, 13)


if __name__ == '__main__':
    unittest.main()
