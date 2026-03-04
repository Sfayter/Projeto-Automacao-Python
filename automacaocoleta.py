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
    (925, 512), (908, 725), (812, 500),
    (1078, 507), (1197, 425), (986, 345),
    (862, 296), (773, 472), (650, 577)
]

#Otimizar esse bloco posteriormente para poupar linhas e melhorar a eficiência
#Bloco apenas para teste
POSICAO_MONTARIA = [
    [(1225, 620), (866,416)], #1
    [(1225, 620), (866,416) ], #2
    [(1225, 620), (866,416) ], #3
    [(1225, 620), (866,416) ], #4
    [(1225, 620), (866,416) ], #5 
    [(1225, 620), (866,416) ], #6 
    [(1225, 620), (866,416) ], #7
    [(1225, 620), (866,416) ], #8
    [(1225, 620), (866,416) ], #9
    [(1225, 620), (866,416) ], #10
    [(1225, 620), (866,416) ], #11 
    [(1225, 620), (866,416) ], #12
    [(1225, 620), (866,416) ], #13
    [(1225, 620), (866,416) ], #14
    [(1225, 620), (866,416) ], #15
    [(1225, 620), (866,416) ], #16  
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
    [(1135, 158), (798, 317)],# Coordenadas para chegar da posição inicial até o terreno 1
    [(1483, 172), (744, 308)],#, 1 > 2
    [(1522, 358), (1142, 377), (793, 323)],# 2 > 3
    [(75, 427), (798, 271), (764, 297)], # 3 > 4
    [(725, 1079), (725, 1079), (964, 580), (1168, 301), (802, 329)], # 4 > 5
    [(1584, 478), (1773, 1079), (1082, 1079), (1471, 1079), (1072, 691), (1123, 321), (793, 323)], # 5 > 6
    [(1258, 313), (1163, 364), (793, 323)], # 6 > 7
    [(1332, 1079), (1072, 912), (1164, 335), (793, 323)], # 7 > 8
    [(1384, 531), (1134, 345), (793, 323)], # 8 > 9
    [(1280, 1079), (1130, 895), (1153, 336), (793, 323)], # 9 > 10
    
    [(637, 1079), (637, 1079), (525, 952), (1181, 341), (793, 323)], # 10 > 11 (necessita manutenção)
    
    [(157, 1079), (639, 1068), (1191, 359), (793, 323)], # 11 > 12
    [(2, 782), (811, 565), (1152, 334), (793, 323)], # 12 > 13
    [(1919, 416), (1919, 1001), (781, 1079), (899, 1079), (932, 571), (1199, 296), (793, 323)], # 13 > 14
    [(1812, 565), (1152, 338), (793, 323)], # 14 > 15
    [(851, 1079), (851, 1079), (703, 1050), (1161, 326), (793, 323)], # 15 > 16
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
    #for x, y in SPOT_PLANTACAO:
        #pyautogui.click(x, y, duration=0.5)
        #time.sleep(random.uniform(1.1, 1.4))

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
        pyautogui.rightClick(x, y, duration=0.9)
        time.sleep(tempo_caminhada)
    pyautogui.press("a")
    

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
        #realizar_colheita()
        #preparar_semente()
        realizar_plantacao(indice)

        print(f"TERRENO {num_terreno} FINALIZADO\n")

    print("Ciclo de 16 terrenos completo!")

#Executa o bot
if __name__ == "__main__":
    iniciar_bot()
