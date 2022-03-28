# Simulador de dados
# O uso de um dador, gerando um valor de 1 a 6
import random
import PySimpleGUI as sg

class SimuladorDaDo:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar novo valor para o dado?'
        # Layout
        self.layout = [sg.text('jogar o dado?')]
                  [sg.button('sim'),sg.button('não')]


    def Iniciar(self):
        # Criar janela
        self.janela = sg.window('Simulador de Dado', layout=layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Depois fazer alguma coisa com valores
        while True:
        try:
                 if self.eventos == 'sim' or self.eventos == 's'
                     self.GerarValorDodado()
                 elif resposta == 'não' or self.eventos == 'n':
                     print('Agradecemos a sua participação!')
                 else:
                     print('Favor digitar sim ou não')
            except:
                  print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDodado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDaDo()
simulador.Iniciar()



    