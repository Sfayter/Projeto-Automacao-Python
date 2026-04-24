import pyautogui, time, random
from src.utils.config import spots_colheita, spots_plantacao, posicaoMontaria, slot_itens, posicionamentoIlha

pyautogui.FAILSAFE = True

def realizarColheita():
    print("Iniciando Colheita...")
    with pyautogui.hold('shift'): 
        for coletarTerreno, (x, y) in enumerate(spots_colheita):
            pyautogui.click(x, y, duration=0.4)
            if coletarTerreno in [0, 1, 2, 3, 5, 7]:
                time.sleep(0.1)
            else:
                time.sleep(0.35)
            
    
#Função de pegar semente no inventário
def prepararSemente():
    print(f"Pegando semente no inventário...")
    pyautogui.press("i")
    pyautogui.click(1676, 540, duration=0.6)
    pyautogui.click(822, 427, duration=0.6)


def realizarPlantacao(indiceTerreno):
    print(f"Plantando no terreno {indiceTerreno + 1}...")
    
    for x, y in spots_plantacao:
        pyautogui.click(x, y, duration=0.3)
        time.sleep(0.6)

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
    #O motivo dele fechar nessa função é devido a dinâmica do jogo, pois se ele fechasse assim que pegasse a semente
    #ela voltaria para o inventário.
    pyautogui.press("esc")

def sementeHorta(terrenoAtual):
    print("Pegando Sementes de Dedaleira...")
    if terrenoAtual >= 12 <= 16:
        pyautogui.press("i")
        pyautogui.click(1737, 540, duration=0.6)
        pyautogui.click(822, 427, duration=0.6)

def guardar_itens():
    print("Guardando itens...")
    for i in range(0, len(slot_itens), 2):
        x1, y1 = slot_itens[i]
        x2, y2 = slot_itens[i+1]
        pyautogui.moveTo(x1, y1, duration=0.8)
        pyautogui.dragTo(x2, y2, duration=0.8)
        time.sleep(random.uniform(0.5, 0.8))

def pegar_itens():
    print("Pegando itens...")
    for i in range(1, len(slot_itens), 2):
        x1, y1 = slot_itens[i]
        x2, y2 = slot_itens[i-1]
        pyautogui.moveTo(x1, y1, duration=0.9)
        pyautogui.dragTo(x2, y2, duration=0.9)
        time.sleep(random.uniform(0.5, 0.8))
        

def viajar_ilha(coordenadas_ilha):
    pyautogui.click(170, 357, duration=0.7)
    pyautogui.moveTo(166,396, duration=0.7)
    pyautogui.moveTo(360, 396, duration=1)
    if coordenadas_ilha:
        x, y = coordenadas_ilha
        pyautogui.click(x, y, duration=0.8)
    pyautogui.click(231, 785, duration=0.8)

def posicionarIlha():
    print("Posicionando personagem na ilha...")
    pyautogui.press("a")
    time.sleep(random.uniform(5, 5.7))
    pyautogui.press("esc")
    time.sleep(0.6)
    for x, y in posicionamentoIlha:
        pyautogui.click(x, y, duration=0.8)
        time.sleep(random.uniform(3, 3.5))

    