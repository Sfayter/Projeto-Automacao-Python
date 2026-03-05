import pyautogui
import time
import random

#Configuração de humanização para randomizar tempo de espera
#Nota: Randomização fixa, posteriormente, deve-se realizar essa randomização diretamente no código
tempo_colheita= random.uniform(1.3, 1.6)
tempo_caminhada = random.uniform(2.5, 3)


#Configuração global de segurança
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

# Os 9 slots de colheita
SPOT_COLETA = [
    (968, 379), (954, 533), (827, 454),
    (1083, 472), (1197, 425), 
    (986, 345),
    (862, 296), (773, 472), 
    (650, 577)
]

#Otimizar esse bloco posteriormente para poupar linhas e melhorar a eficiência
#Bloco apenas para teste
POSICAO_MONTARIA = [
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

# Os 9 slots de plantação
SPOT_PLANTACAO = [
    (817, 522), (941, 645), (1007, 437),
    (1091, 506), (1086, 329), (1191, 409),
    (1340, 514), (1216, 605), (1082, 701)
]

# MAPA DE NAVEGAÇÃO
# Cada sub-lista [ ] contém os cliques necessários para chegar e CENTRALIZAR no terreno
CAMINHOS_DOS_16_TERRENOS = [
    [(967, 249), (974, 227)],# Coordenadas para chegar da posição inicial até o terreno 1
    [(1362, 196), (979, 211)],#, 1 > 2
    [(1568, 310), (1000, 210)],# 2 > 3
    [(262,  369), (517, 377), (978, 208)], # 3 > 4
    [(852, 1079), (790, 1079), (978, 189)], # 4 > 5
    [(1582, 323), (1713, 1079), (1409, 1079), (921, 1079), (1324, 827), (987, 211)], # 5 > 6
    [(1313, 266), (1002, 221)], # 6 > 7
    [(1391, 1079), (1158, 757), (986, 197)], # 7 > 8

    #manutenção realizada nessa coordenada 8 > 9
    #verificar a colheita daqui em diante para validar se está padrão
    [(1461, 456), (979, 192)], # 8 > 9

    [(1322, 1079), (1215, 695), (985, 215)], # 9 > 10
    [(502, 1075), (1503, 850), (50,856),(989,786),(981, 213)], # 10 > 11 (necessita manutenção)

    [(377, 939), (716, 933), (989, 231)], # 11 > 12
    [(68, 679), (962, 232)], # 12 > 13
    [(1919, 530), (1422, 350), (1685, 1079), (1423, 1079), (131, 893), (980, 193)], # 13 > 14
    [(1841, 498), (1003, 183)], # 14 > 15
    [(761, 1079), (693, 938), (1139, 872), (980, 218)], # 15 > 16
]


#Funções de ações
#Futuramente ajustar essa parte para deixar o código mais organizado e limpo

#Função de colher as plantações
def realizar_colheita():
    print(f"Iniciando Colheita e Montaria no Terreno...")
    
    # 1. Primeiro ele colhe os 9 slots
    with pyautogui.hold('shift'): 
        for x, y in SPOT_COLETA:
            pyautogui.click(x, y, duration=1)
            time.sleep(tempo_colheita)
    
#Função de pegar semente
def preparar_semente():
    time.sleep(3)
    print(f"Pegando semente no inventário...")
    pyautogui.press("i")
    pyautogui.click(1676, 540, duration=0.5)
    pyautogui.click(822, 427, duration=0.5)

#Função de plantar as sementes nos 9 slots de cada terreno
def realizar_plantacao(indice_terreno):
    print(f"Plantando no terreno {indice_terreno + 1}...")
    
    #------Comentado para manutenção------
    for x, y in SPOT_PLANTACAO:
        pyautogui.click(x, y, duration=0.5)
        time.sleep(random.uniform(1.1, 1.4))

    #Ajusta o boneco para pegar a montaria e navegar nos terrenos
    time.sleep(3)
    passos_montaria = POSICAO_MONTARIA[indice_terreno]
    
    print(f"Executando {len(passos_montaria)} para subir na montaria...")
    
    for x, y in passos_montaria:
        pyautogui.rightClick(x, y, duration=0.8)
        time.sleep(random.uniform(2.5, 2.8)) 

    #Sobe na montaria
    pyautogui.press("a")
    print("Montagem estabilizada!")
    time.sleep(random.uniform(0.7, 1.2))
    pyautogui.press("esc")

#Função de caminhar entre os terrenos de acordo com as coordenadas passadas nas listas e sublistas
def navegar_para_terreno(lista_de_cliques):
    for x, y in lista_de_cliques:
        pyautogui.click(x, y, duration=1)
        time.sleep(3)
        #if para manutenção dos terrenos
        # resposta = input("Deseja continuar?")
        # if resposta == "s":
        #     print("prosseguindo")
        #     time.sleep(2)
    pyautogui.press("a")
    #if para manutenção dos terrenos
    # resposta = input("Deseja continuar?")
    # if resposta == "s":
    #     print("prosseguindo")
    #     time.sleep(1)
    

#Função Principal Inicialização
def iniciar_bot():
    print("O bot começará em 3 segundos. Mude para a janela do jogo!")
    time.sleep(3)

    # O loop percorre cada terreno da lista de 16
    for indice, cliques_trajeto in enumerate(CAMINHOS_DOS_16_TERRENOS):
        num_terreno = indice + 1
        print(f"INICIANDO TERRENO {num_terreno}")

        #Chama função de navegar nos terrenos
        navegar_para_terreno(cliques_trajeto)
        
        #Chama as funções de ações no terreno

        #comentado para manutenção
        realizar_colheita()
        preparar_semente()
        realizar_plantacao(indice)

        print(f"TERRENO {num_terreno} FINALIZADO\n")

    print("Ciclo de 16 terrenos completo!")

#Executa o bot
if __name__ == "__main__":
    iniciar_bot()
