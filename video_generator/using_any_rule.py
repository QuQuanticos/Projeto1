import cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc
import matplotlib.pyplot as plt
import os

class Automato:

    def __init__(self, Number_of_Steps=5, Rule=30, Random = False):#Main
        self.Number_of_Steps = Number_of_Steps
        self.Rule = Rule
        self.Random = Random

        self.Width = 2*self.Number_of_Steps + 1 #Garante que Width é ímpar e, portanto,
        #temos uma única célula no centro

#         print('Passo 1')
        self.Cellular_Automaton = self.FirstStep()

        for i in range(Number_of_Steps-1):
#             print('Passo ' + str(i+2))
            self.Cellular_Automaton = self.Step(self.Cellular_Automaton)

    def FirstStep(self):#Initiate_Cellular_Automaton
        '''
        Cria condição inicial (chamado de "step 1" pelo Wolfram) de uma única
        célula preta no centro do autômato.
    -------------------------------------------------------------------------------
        Inputs:
            Width: Número de células do autômato, i.e., largura da malha.
    -------------------------------------------------------------------------------
        Outputs:
            First_Step: Autômato na condiação inicial.
        '''

        if self.Random:
            First_Step = np.random.randint(0,2, (1,self.Width))

        else:
            First_Step = np.full((1, self.Width), 0)
            First_Step[0][int(self.Width/2)] = 1

        return First_Step

    def Step(self,Cellular_Automaton):
        '''
        Aplica a Regra n ∈ [0, 255]
    -------------------------------------------------------------------------------
        Inputs:
            self.Cellular_Automaton: evolução do autômato até o atual n-ésimo passo como
            array (n, Width).
    -------------------------------------------------------------------------------
        Outputs:
            Autômato concatenado com novo passo, resultando em array (n+1, Width).
        '''

        Rule_Bin = np.binary_repr(self.Rule, 8) #Representação binária de 8 bits da regra em string
        #Ex: '01101110' pra Regra 110

        Rule_Bin = np.array([int(_) for _ in Rule_Bin], dtype=np.int8) #Iterando sobre a string para separar os 0's e 1's
        #Ex: [0,1,1,0,1,1,1,0] pra Regra 110

        New_Step = np.vstack((np.roll(Cellular_Automaton[-1:],-1), Cellular_Automaton[-1:], np.roll(Cellular_Automaton[-1:],1))).astype(np.int8)
        #[[0,0,0,1,0,0,0,0,0],
        # [0,0,0,0,1,0,0,0,0],
        # [0,0,0,0,0,1,0,0,0]]

        u = np.array([[4],[2], [1]])
        #[[4],
        # [2],
        # [1]]

        New_Step = u*New_Step #Multiplica column-wise
        #[[0,0,0,4,0,0,0,0,0],
        # [0,0,0,0,2,0,0,0,0],
        # [0,0,0,0,0,1,0,0,0]]

        New_Step = np.sum(New_Step, axis= 0).astype(np.int8) #Soma row-wise
        #[0,0,0,4,2,1,0,0,0]

        New_Step = np.array([Rule_Bin[7 - New_Step]]) #Aplica a regra
        #[0,0,0,0,1,1,0,0,0]
        return np.concatenate((Cellular_Automaton, New_Step))

    def Plot(self, Save=False):
        '''
        Gera imagem da evolução do autômato em todos os passos.
    -------------------------------------------------------------------------------
            evolução do autômato celular ao longo de todos os
            passos na forma de um array (número de passo, 2*número de passo + 1)
            de zeros (casas brancas) e uns (casas pretas).
        '''

        Number_of_Steps = self.Cellular_Automaton.shape[0]

        Plot_Width = 20
        fig, axs = plt.subplots(1, 1, figsize=(Plot_Width+1, (Plot_Width-1)/2))
        plt.title("Regra "+str(self.Rule), fontsize = 50)
        axs.pcolormesh(np.flip(self.Cellular_Automaton), edgecolors = 'white', cmap = 'binary', label = 'Passos Totais: '+str(Number_of_Steps),linewidths =5/self.Number_of_Steps)

        plt.axis('off')

        axs.grid(color='white', ls='solid')
        axs.grid(True)
        axs.set_xlabel('X [pixels]')
        axs.set_ylabel('Y [pixels]')
        plt.tight_layout()
        if Save:
            # Não sobrescrever imagem
            outfilename = 'Regra'+str(self.Rule)+'_'+str(Number_of_Steps)+'passos_'
            i = 0
            while os.path.exists(outfilename + str(i) + '.png'):
                i += 1

            plt.savefig(outfilename + str(i) + '.pdf', bbox_inches='tight', dpi=300)

        plt.show()



'''
Producao do video
'''

'''
Parametros utilizados na producao do video
'''
ite = int (input("Digite o numero de iteracoes desejadas (>0): "))
width, height = input("Digite a largura e altura do video (ex: 1920 1080): ").split(" ")
width = int(width)
height = int(height)
FPS = 120


# width = 1920
# height = 1080
# ite = 300
# FPS = 120

'''
Iniciando o operador que grava o video e denominando o video a partir dos parametros inseridos.
'''
fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./Regra_30_' + str(ite) +'_iteracoes_'+ str(width) +'x'+str(height)+ "_@" + str(FPS)+"_fps" + '.avi', fourcc, float(FPS), (width, height), 0)


'''
Criacao de um objeto (aut) da classe Automato, uma imagem branca (whiteFrame),
uma imagem auxiliar (Frame), uma matriz linha (line) e calculo dos limites
referentes ao posicionamento do padrao da regra 30 no centro da imagem do video.

'''
aut = Automato(Number_of_Steps = ite)

whiteFrame = np.full((height, width), 255, dtype = np.uint8)

Frame = np.full((height, width), 255, dtype = np.uint8)

line = np.full((1, width), 255, dtype = np.uint8)

lim_i = int((2*ite+1)/2) - int(width/2)

lim_s = (int((2*ite+1)/2) + int(width/2))


'''
Manipulacao do padrao gerado pela regra 30 para facilitacao dos passos subsequentes
de producao do video
'''
matrix = aut.Cellular_Automaton


for i in range(len(matrix)):
    for j in range(len(matrix[0])):

        if (matrix[i][j] == 1):

            matrix[i][j] = 0

        else:

            matrix[i][j] = 255

'''
Tratamento dos casos de numero de iteracoes menor do que a resolucao do video e
seu complementar. Gravacao dos frames obtidos a partir do padrao da regra 30

'''
if (2*ite+1 < width):

    ini = np.full((1, int(((width - 2*ite+1)/2))), 255, dtype = np.uint8)

    for i in range(len(matrix)):

        a = np.concatenate((ini[0], matrix[i], ini[0]), axis = 0)

        a = np.delete(a, -1, axis = 0)

        Frame[i] = a

        whiteFrame[i] = Frame[i]

        video.write(whiteFrame)

else:

    for i in range(ite):

        if (i < height):
            whiteFrame[i] = aut.Cellular_Automaton[i][lim_i:lim_s]

        else:

            line = aut.Cellular_Automaton[i][lim_i:lim_s]

            newLine = []
            newLine.append(line)
            whiteFrame = np.concatenate((whiteFrame, np.uint8(newLine)), axis=0)

            whiteFrame = np.delete(whiteFrame, (0), axis=0)

        video.write(whiteFrame)

video.release()
