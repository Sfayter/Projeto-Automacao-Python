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
    pause = pydirectinput.PAUSE
    pydirectinput.PAUSE = 0
    print(f"Plantando no terreno {indiceTerreno + 1}...")
    
    for x, y in spots_plantacao:
        clickPlantacao(x, y, duration=0.3)
        time.sleep(1)

    pydirectinput.PAUSE = pause
    pydirectinput.press("esc")

def subirMontaria(indiceTerreno):
    #Ajusta o boneco para pegar a montaria na posição correta e navegar nos terrenos
        time.sleep(random.uniform(0.4, 0.7))
        passosMontaria = posicaoMontaria[indiceTerreno]
        
        print("Executando passos para subir na montaria...")
        
        #Loop para percorrer a lista e sublistas de posicaoMontaria e conseguir subir na montaria na posição correta.
        for x, y in passosMontaria:
            rightClick(x, y, duration=0.7)
            time.sleep(random.uniform(1.1, 1.5)) 
    
        #Sobe na montaria
        pydirectinput.press("a")
        time.sleep(random.uniform(0.3, 0.6))

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
        dragTo(x1, y1, x2, y2, duration=0.8)
        time.sleep(random.uniform(0.5, 0.8))
    pydirectinput.press("esc")

def pegar_itens():
    print("Pegando itens...")
    for i in range(1, len(slot_itens), 2):
        x1, y1 = slot_itens[i]
        x2, y2 = slot_itens[i-1]
        dragTo(x1, y1, x2, y2, duration=0.9)
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
    pydirectinput.press("a")
    time.sleep(random.uniform(5, 5.7))
    pydirectinput.press("esc")
    time.sleep(0.6)
    if ilha_atual <= 1:
        for x, y in posicionamentoIlha[:3]:
            click(x, y, duration=0.8)
            time.sleep(random.uniform(3, 3.5))
    #Condição abaixo é para fazer um slicing e ignorar os 3 primeiros pontos da lista "PosicionamentoIlha" e garantir
    #que seja usado os pontos para posicionar na fazenda 4(Thetford)
    elif ilha_atual == 2:
        for x, y in posicionamentoIlha[3:]:
            click(x, y, duration=0.8)
            time.sleep(random.uniform(3, 3.5))

def ordenhar():
    pydirectinput.keyDown('shift')
    pause = pydirectinput.PAUSE
    pydirectinput.PAUSE = 0
    try:
        for ordenhar_animais, (x, y) in enumerate(spots_ordenha):
            click(x, y, duration=0.4)
            if ordenhar_animais in [0, 4, 6]:
                time.sleep(0.8)
            elif ordenhar_animais in [8]:
                time.sleep(1.4)
    finally:
        pydirectinput.keyUp('shift')
        pydirectinput.PAUSE = pause
        

def alimentar():
    pydirectinput.keyDown('shift')
    pause = pydirectinput.PAUSE
    pydirectinput.PAUSE = 0
    try:
        for alimentar_animais, (x, y) in enumerate(spots_alimentacao[:9]):
            click(x, y, duration=0.5)
            if alimentar_animais in [0, 4, 6]:
                time.sleep(0.7)
            elif alimentar_animais in [8]:
                time.sleep(1.2)
    finally:
        pydirectinput.keyUp('shift')
        pydirectinput.PAUSE = pause
    pydirectinput.press("a")
    time.sleep(1.5)

def fertilizarTerreno():
    print("Fertilizando terreno...")
    pydirectinput.keyDown('shift')
    pause = pydirectinput.PAUSE
    pydirectinput.PAUSE = 0
    try:
        for fertilizar, (x, y) in enumerate(spots_alimentacao):
            clickPlantacao(x, y, duration=0.5)
            if fertilizar in [0, 1, 2, 3, 5, 7, 9, 10]:
                time.sleep(1.4)
            elif fertilizar in [4, 6]:
                time.sleep(1.7)
            elif fertilizar in [8]:
                time.sleep(2.2)
    finally:
        pydirectinput.keyUp('shift')
        pydirectinput.PAUSE = pause