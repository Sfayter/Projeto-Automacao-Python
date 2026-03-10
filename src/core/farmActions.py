import pyautogui
import time
import random
from src.utils.config import spotColeta, spotPlantacao, posicaoMontaria

#Funções de ação
#Função de colher as plantações
def realizarColheita():
    print("Iniciando Colheita...")

    #Loop para fazer a colheita utilizando o shift pressionado para uma colheita mais eficiente e rápida.
    with pyautogui.hold('shift'): 
        for x, y in spotColeta:
            pyautogui.click(x, y, duration=0.8)
            time.sleep(random.uniform(0.8, 1))
    
#Função de pegar semente no inventário
def prepararSemente():
    print(f"Pegando semente no inventário...")
    pyautogui.press("i")
    pyautogui.click(1676, 540, duration=0.6)
    pyautogui.click(822, 427, duration=0.6)

#Função de plantar as sementes nos 9 slots de cada terreno
def realizarPlantacao(indiceTerreno):
    print(f"Plantando no terreno {indiceTerreno + 1}...")
    
    for x, y in spotPlantacao:
        pyautogui.click(x, y, duration=0.5)
        time.sleep(random.uniform(1.0, 1.3))

    #Ajusta o boneco para pegar a montaria na posição correta e navegar nos terrenos
    time.sleep(random.uniform(0.7, 1))
    passosMontaria = posicaoMontaria[indiceTerreno]
    
    print("Executando passos para subir na montaria...")
    
    #Loop para percorrer a lista e sublistas de posicaoMontaria e conseguir subir na montaria na posição correta.
    for x, y in passosMontaria:
        pyautogui.rightClick(x, y, duration=0.7)
        time.sleep(random.uniform(1, 1.4)) 

    #Sobe na montaria
    pyautogui.press("a")
    time.sleep(random.uniform(0.5, 0.8))
    #Fecha o inventário aberto pela função prepararSemente
    #O motivo dele fechar nessa função é devido a dinâmica do jogo, pois se ele fechasse assim que pegasse a semente, ela voltaria para o inventário.
    pyautogui.press("esc")

def sementeHorta(terrenoAtual):
    print("Pegando Sementes de Dedaleira...")
    if terrenoAtual >= 12 <= 16:
        pyautogui.click(1676, 540, duration=0.6)
        pyautogui.click(822, 427, duration=0.6)