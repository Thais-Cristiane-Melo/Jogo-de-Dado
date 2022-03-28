from ast import Or
from logging import exception
import random

class SimuladorDaDo:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar novo valor para o dado?'

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
             if resposta == 'sim' or resposta == 's':
                 self.GerarValorDodado()
             elif resposta == 'não' or resposta == 'n':
                 print('Agradecemos a sua participação')
             else:
                 print('Favor digitar sim ou não')
        except:
              print('Ocrreu um erro ao receber sua resposta')
        
    def GerarValorDodado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDaDo()
simulador.Iniciar()



    