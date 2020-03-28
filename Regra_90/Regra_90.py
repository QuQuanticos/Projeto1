#%% Imports

import numpy as np
import matplotlib.pyplot as plt
import os

#%% Generating First Step

def Initiate_Cellular_Automaton(Width, Random):
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
    
    if Random:
        First_Step = np.random.randint(0,2, (1,Width))
    
    else:
        First_Step = np.full((1, Width), 0)
        First_Step[0][int(Width/2)] = 1
    
    return First_Step

#%% Rule 90

def Rule_90(Cellular_Automaton):
    '''
    Aplica a Regra 90: a célula será preta no próximo passo caso uma, e apenas
    uma, de suas vizinhas for preta; do contrário, será branca.
    
-------------------------------------------------------------------------------
    Inputs:
        Cellular_Automaton: evolução do autômato até o atual n-ésimo passo como
        array (n, Width).
        
-------------------------------------------------------------------------------
    Outputs:
        Autômato concatenado com novo passo, resultando em array (n+1, Width).
    '''
    
    New_Step = (np.roll(Cellular_Automaton[-1:],1) + np.roll(Cellular_Automaton[-1:],-1)) % 2
    
    return np.concatenate((Cellular_Automaton, New_Step))

#%% Running

def Main(Number_of_Steps = 5, Random = False):
    '''
    Executa os vários passos para o autômato definido pela regra 90.
    
-------------------------------------------------------------------------------
    Inputs:
        Number_of_Steps: Número de passos da evolução do autômato.
        
-------------------------------------------------------------------------------
    Outputs:
        Autômato concatenado com novo passo, resultando em array (n+1, Width).
    '''
    
    Width = 2*Number_of_Steps + 1 #Garante que Width é ímpar e, portanto,
    #temos uma única célula no centro
    
    print('Passo 1')
    Cellular_Automaton = Initiate_Cellular_Automaton(Width, Random)
    
    for i in range(Number_of_Steps-1):
        print('Passo ' + str(i+2))
        Cellular_Automaton = Rule_90(Cellular_Automaton)
    
    return Cellular_Automaton

#%% Plotting

def Plot(Cellular_Automaton):
    '''
    Gera imagem da evolução do autômato em todos os passos.
    
-------------------------------------------------------------------------------
    Inputs:
        Cellular_Automaton: evolução do autômato celular ao longo de todos os
        passos na forma de um array (número de passo, 2*número de passo + 1) 
        de zeros (casas brancas) e uns (casas pretas).
    '''
    
    Number_of_Steps = Cellular_Automaton.shape[0]
    
    Plot_Width = 20
    plt.figure(figsize=(Plot_Width+1, (Plot_Width-1)/2))
    plt.pcolor(np.flip(Cellular_Automaton), edgecolors = 'k', cmap = 'binary',
               linewidths = 5/Number_of_Steps)
    
    plt.axis('off')
    
    # Várias gambiarras para fazer com que o padding da caixa batesse com a moldura da grid
    plt.text(1.99*Number_of_Steps+1,0.99*Number_of_Steps, 'Passos Totais: '+str(Number_of_Steps),
             size = 20, verticalalignment='top', horizontalalignment='right',
             color='w', bbox={'facecolor': 'red', 'alpha': 1, 'pad': 5})
    
    # Plota rótulo de cada passo caso isso seja bem visível
    if Number_of_Steps<=15:
        for i in range(Number_of_Steps):
            plt.text(0+Number_of_Steps/100,Number_of_Steps-i-0.5, 'Passo '+str(i+1),
                     fontsize = 100/Number_of_Steps,
                     verticalalignment='center', horizontalalignment='left',
                     color='w', bbox={'facecolor': 'red', 'alpha': 1, 'pad': 5})
    
    # Não sobrescrever imagem
    outfilename = 'Regra90_'+str(Number_of_Steps)+'passos_'
    i = 0
    while os.path.exists(outfilename + str(i) + '.png'):
        i += 1
        
    plt.savefig(outfilename + str(i) + '.png', bbox_inches='tight', dpi=200)

#%%

Cellular_Automaton = Main(50)
Plot(Cellular_Automaton)