import time, random, pydirectinput
from src.utils.config import spots_colheita, spots_plantacao, posicaoMontaria, slot_itens, posicionamentoIlha, spots_ordenha, spots_alimentacao
from src.utils.input import click, clickPlantacao, rightClick, dragTo, moveTo

pydirectinput.FAILSAFE = True

def realizarColheita():
    print("Iniciando Colheita...")
    pydirectinput.keyDown ('shift')
    try: 
        for coletarTerreno, (x, y) in enumerate(spots_colheita):
            click(x, y, duration=0.4)
            if coletarTerreno in [0, 1, 2, 3, 5, 7]:
                time.sleep(0.1)
            else:
                time.sleep(0.35)
    finally:
        pydirectinput.keyUp('shift')
            
    
#Função de pegar semente no inventário
def prepararSemente():
    print(f"Pegando semente no inventário...")
    pydirectinput.press("i")
    click(1676, 540, duration=0.6)
    click(822, 427, duration=0.6)


def realizarPlantacao(indiceTerreno):
    pausePadrao = pydirectinput.PAUSE
    pydirectinput.PAUSE = 0
    print(f"Plantando no terreno {indiceTerreno + 1}...")
    
    for x, y in spots_plantacao:
        click(x, y, duration=0.5)
        time.sleep(0.6)

    pydirectinput.PAUSE = pausePadrao

    #Ajusta o boneco para pegar a montaria na posição correta e navegar nos terrenos
    time.sleep(random.uniform(0.7, 1))
    passosMontaria = posicaoMontaria[indiceTerreno]
    
    print("Executando passos para subir na montaria...")
    
    #Loop para percorrer a lista e sublistas de posicaoMontaria e conseguir subir na montaria na posição correta.
    for x, y in passosMontaria:
        rightClick(x, y, duration=0.7)
        time.sleep(random.uniform(1, 1.4)) 

    #Sobe na montaria
    pydirectinput.press("a")
    time.sleep(random.uniform(0.5, 0.8))
    #Fecha o inventário aberto pela função prepararSemente
    #O motivo dele fechar nessa função é devido a dinâmica do jogo, pois se ele fechasse assim que pegasse a semente
    #ela voltaria para o inventário.
    pydirectinput.press("esc")

def sementeHorta(terrenoAtual):
    print("Pegando Sementes de Dedaleira...")
    if terrenoAtual >= 11 <= 16:
        pydirectinput.press("i")
        click(1737, 540, duration=0.6)
        click(822, 427, duration=0.6)

def guardar_itens():
    print("Guardando itens...")
    for i in range(0, len(slot_itens), 2):
        x1, y1 = slot_itens[i]
        x2, y2 = slot_itens[i+1]
        dragTo(x1, y1, x2, y2, duration=0.9)
        time.sleep(random.uniform(0.5, 0.8))
    pydirectinput.press("esc")

def pegar_itens():
    print("Pegando itens...")
    for i in range(1, len(slot_itens), 2):
        x1, y1 = slot_itens[i]
        x2, y2 = slot_itens[i-1]
        dragTo(x1, y1, x2, y2, duration=0.8)
        time.sleep(random.uniform(0.5, 0.8))
    pydirectinput.press("esc")
        

def viajar_ilha(coordenadas_ilha):
    click(170, 357, duration=0.7)
    pydirectinput.moveTo(166,396, duration=0.7)
    pydirectinput.moveTo(360, 396, duration=1)
    if coordenadas_ilha:
        x, y = coordenadas_ilha
        click(x, y, duration=0.8)
    click(231, 785, duration=0.8)

def posicionarIlha(ilha_atual):
    print("Posicionando personagem na ilha...")
    pyautogui.press("a")
    time.sleep(random.uniform(5, 5.7))
    pyautogui.press("esc")
    time.sleep(0.6)
    if ilha_atual <= 1:
        for x, y in posicionamentoIlha[:3]:
            pyautogui.click(x, y, duration=0.8)
            time.sleep(random.uniform(3, 3.5))
    #Condição para ignorar os 3 primeiros pontos da lista "PosicionamentoIlha" e garantir
    #que seja usado os pontos para posicionar na fazenda 4(Thetford)
    elif ilha_atual == 2:
        for x, y in posicionamentoIlha[3:]:
            pyautogui.click(x, y, duration=0.8)
            time.sleep(random.uniform(3, 3.5))

def ordenhar():
    for ordenhar_animais, (x, y) in enumerate(spots_ordenha):
        with pyautogui.hold('shift'):
            pyautogui.click(x, y, duration=0.4)
            if ordenhar_animais in [0, 4, 6, 8]:
                time.sleep(0.1)

def alimentar():
    for alimentar_animais, (x, y) in enumerate(spots_alimentacao):
        with pyautogui.hold('shift'):
            pyautogui.click(x, y, duration=0.5)
            if alimentar_animais in [0, 4, 6, 8]:
                time.sleep(0.65)
    pyautogui.press("a")
    time.sleep(1.5)