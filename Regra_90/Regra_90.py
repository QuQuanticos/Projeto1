#%% Imports

import numpy as np
import matplotlib.pyplot as plt

#%% Generating First Step

def Initiate_Cellular_Automaton(Width):
    First_Step = np.full((1, Width), 0, dtype = int)
    First_Step[0][int(Width/2)] = 1

#    First_Step = np.full((1, Width), 255, dtype = np.uint8)
#    First_Step[0][int(Width/2)] = 0

    return First_Step

#%% Rule 90

def Rule_90(Cellular_Automaton):
    New_Step = (np.roll(Cellular_Automaton[-1:],1) + np.roll(Cellular_Automaton[-1:],-1)) % 2
    return np.concatenate((Cellular_Automaton, New_Step))

#%% Bora rodar

Number_of_Steps = 5
Width = 2*Number_of_Steps + 1 #Garante que Width é um número ímpar e, portanto,
#temos uma única célula no centro

Cellular_Automaton = Initiate_Cellular_Automaton(Width)

for i in range(Number_of_Steps):
    print("Step " + str(i))
    Cellular_Automaton = Rule_90(Cellular_Automaton)

#%% Plotting

plt.pcolor(Cellular_Automaton, edgecolors = 'k', linewidths = 1)
plt.show()