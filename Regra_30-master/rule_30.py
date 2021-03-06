import cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc

'''
Definicao da funcao que verifica a regra 30
'''

def rule_30(frame, line):


    for i in range(len(frame[line]) - 3):

        if (frame[line][i] == 0 and frame[line][i+1] == 0 and frame[line][i+2] == 0):

            frame[line+1][i + 1] = 255

        elif (frame[line][i] == 0 and frame[line][i+1] == 0 and frame[line][i+2] == 255):

            frame[line+1][i + 1] = 255

        elif (frame[line][i] == 0 and frame[line][i+1] == 255 and frame[line][i+2] == 0):

            frame[line+1][i + 1] = 255

        elif (frame[line][i] == 0 and frame[line][i+1] == 255 and frame[line][i+2] == 255):

            frame[line+1][i + 1] = 0

        elif (frame[line][i] == 255 and frame[line][i+1] == 0 and frame[line][i+2] == 0):

            frame[line+1][i + 1] = 0

        elif (frame[line][i] == 255 and frame[line][i+1] == 0 and frame[line][i+2] == 255):

            frame[line+1][i + 1] = 0

        elif (frame[line][i] == 255 and frame[line][i+1] == 255 and frame[line][i+2] == 0):

            frame[line+1][i + 1] = 0

        elif (frame[line][i] == 255 and frame[line][i+1] == 255 and frame[line][i+2] == 255):

            frame[line+1][i + 1] = 255

    return frame

'''
Definicao da funcao que inicia um vetor 1 linha por "width" colunas com valores 0 ou 255
'''
def start_rand_line():
    #frame = np.random.randint(0, 255,(height, width, 3), dtype=np.uint8) #RGB video
    frame = np.random.randint(0, 255,(1, width), dtype=np.uint8)

    for i in range(len(frame[0])):

        if (frame[0][i] > 100):
            #print(frame[0])
            frame[0][i] = 255
            #print(frame[0])
        else:
            frame[0][i] = 0
    return frame

'''
Definicao da funcao que inicia um vetor 1 linha por "width" colunas com valores 255 e um unico
(no centro da imagem) com valor 0
'''


def start_line():
    frame = np.full((1, width), 255, dtype = np.uint8)

    frame[0][int(width/2)] = 0

    return frame


'''
Definicao de parametros da imagem assim como do video que sera gravado
'''

width = 1280
height = 720
FPS = 60
seconds = height

fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./noise.avi', fourcc, float(FPS), (width, height), 0)
#video = VideoWriter('./noise.avi', fourcc, float(FPS), (width, height)) #----RGB video

counter = 0


'''
Criacao do vetor condicao inicial e da matriz correspondente a imagem (inicialmente toda branca)
'''


frame = start_line() ## Mude o vetor inicial alterando a funcao chamada (start_line ou start_rand_line)


whiteFrame = np.full((height-1, width), 255, dtype = np.uint8)

'''
Juntando o vetor com a matriz para que a imagem final tenha a altura "height"
'''

frameFinal = np.concatenate((frame, whiteFrame))

'''
Construindo os frames com base na regra 30 e a condicao inicial
'''

for _ in range(seconds - 1):

    frameFinal = rule_30(frameFinal, counter)

    video.write(frameFinal)
    counter += 1

video.release()
