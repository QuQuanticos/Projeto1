# Regra_30
Programa utilizado na construção do vídeo que simula a regra 30

Instalação do opencv para funcionamento do programa:

    Para Linux (debian like... p outras distros que usam algo alem do apt, tente com o respectivo gerenciador)

    1° - sudo apt update && sudo apt upgrade

    2° - para ver se o pip3 esta instalado eh soh dar o comando "pip3" no terminal

    3° - caso pip3 nao esteja instalado:

        sudo apt install python3-pip

    4° - apos instalado, instalar o opencv:

        sudo pip3 install opencv-python

    5° - apos instalado o opencv, entre no python3 pelo terminal e importe esse pacote:

        python3
        import cv2

    caso nenhum erro ocorra, está tudo certo e o programa "rule_30.py" deve funcionar sem problemas.
   
Ainda falta:
    - Implementação do zero padding para tratamento das colunas inicial e final da imagem.
    - Implementação da rolagem da imagem à medida que as iterações ocorram.
