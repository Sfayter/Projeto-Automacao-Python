import pyautogui
import time
import random

#Configuração global de segurança
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

#Slots de colheita
spotColeta = [
    (968, 379), (954, 533), (827, 454),
    (1083, 472), (1197, 425), (986, 345),
    (862, 296), (773, 472), (650, 577)
]

#Posições da montaria
#Foi necessário definir as coordenadas nesse formato no lugar de um loop com uma coordenada fixa, pois a montaria 
#varia o posicionamento de acordo com o terreno de colheita
posicaoMontaria = [
    [(942,829), (966, 400)], #1
    [(942, 825), (986, 409) ], #2
    [(942, 830), (976, 391) ], #3
    [(942, 829), (989, 408) ], #4
    [(942, 829), (989,404) ], #5 
    [(943, 828), (997, 402) ], #6 
    [(942, 828), (980, 404) ], #7
    [(942, 829), (988, 403) ], #8
    [(942, 829), (988,403) ], #9
    [(942, 829), (1001, 403) ], #10
    [(944, 829), (994,409) ], #11
    [(942, 829), (974, 403) ], #12
    [(944, 829), (1000,408) ], #13
    [(942, 829), (995,406) ], #14
    [(942, 829), (982,399) ], #15
    [(942, 829), (983,404) ], #16  
]

#Slots de plantação
spotPlantacao = [
    (817, 522), (941, 645), (1007, 437),
    (1091, 506), (1086, 329), (1191, 409),
    (1340, 514), (1216, 605), (1082, 701)
]

# MAPA DE NAVEGAÇÃO
# Cada sub-lista [ ] contém os cliques necessários para chegar nos terrenos
caminhosTerrenos = [
    [(967, 249), (974, 227)],# Coordenadas para chegar da posição inicial até o terreno 1
    [(1362, 196), (979, 211)],#, 1 > 2
    [(1568, 310), (1000, 210)],# 2 > 3
    [(262,  369), (517, 377), (978, 208)], # 3 > 4
    [(852, 1079), (790, 1079), (978, 189)], # 4 > 5
    [(1582, 323), (1713, 1079), (1409, 1079), (921, 1079), (1324, 827), (987, 211)], # 5 > 6
    [(1313, 266), (1002, 221)], # 6 > 7
    [(1391, 1079), (1158, 757), (986, 197)], # 7 > 8
    [(1461, 456), (979, 192)], # 8 > 9
    [(1322, 1079), (1215, 695), (985, 215)], # 9 > 10
    [(502, 1075), (1503, 850), (50,856),(989,786),(981, 213)], # 10 > 11
    [(377, 939), (716, 933), (989, 231)], # 11 > 12
    [(68, 679), (962, 232)], # 12 > 13
    [(1919, 530), (1422, 350), (1685, 1079), (1423, 1079), (131, 893), (980, 193)], # 13 > 14
    [(1841, 498), (1003, 183)], # 14 > 15
    [(761, 1079), (693, 938), (1139, 872), (980, 218)], # 15 > 16
]

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
    
    print(f"Executando {len(passosMontaria)} para subir na montaria...")
    
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

#Função de caminhar entre os terrenos de acordo com as coordenadas passadas na lista e sublistas da lista caminhosTerrenos
def navegar_para_terreno(lista_de_cliques):
    for x, y in lista_de_cliques:
        pyautogui.click(x, y, duration=1)
        time.sleep(3)
        #if para manutenção dos terrenos
        # resposta = input("Deseja continuar?")
        # if resposta == "s":
        #     print("prosseguindo")
        #     time.sleep(1)
    pyautogui.press("a")
    #if para manutenção dos terrenos
    # resposta = input("Deseja continuar?")
    # if resposta == "s":
    #     print("prosseguindo")
    #     time.sleep(1)
    

#Função Principal Inicialização
def iniciarAcoes():
    print("Iniciando em 3 segundos...")
    time.sleep(3)

    #Loop para percorrer nos terrenos
    for indice, cliques_trajeto in enumerate(caminhosTerrenos):
        num_terreno = indice + 1
        print(f"Iniciando Terreno {num_terreno}")

        #Chama função de navegar nos terrenos
        navegar_para_terreno(cliques_trajeto)

        #Funções de ação
        realizarColheita()
        prepararSemente()
        realizarPlantacao(indice)

        print(f"Terreno {num_terreno} finalizado.\n")

    print("Ciclo de 16 terrenos completo!")

#Executa o bot
if __name__ == "__main__":
    iniciarAcoes()
