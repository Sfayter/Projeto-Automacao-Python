import pyautogui
import time
import random

# Configurações de randomização do tempo de espera
tempo_colheita= random.uniform(1.3, 1.6)
tempo_caminhada = random.uniform(2.5, 3)


# --- CONFIGURAÇÕES E SEGURANÇA ---
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

# --- COORDENADAS FIXAS (Ajuste conforme sua tela) ---

# Os 9 slots de colheita (relativos à posição central do boneco)
SPOT_COLETA = [
    (925, 512), (908, 725), (812, 500),
    (1078, 507), (1197, 425), (986, 345),
    (862, 296), (773, 472), (650, 577)
]

POSICAO_MONTARIA = [
    [(1225, 620), (866,416)], #posição terreno 1
    [(1225, 620), (866,416) ], #posição terreno 2
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

# MAPA DE NAVEGAÇÃO (Aqui está a mágica dos 16 terrenos)
# Cada sub-lista [ ] contém os cliques necessários para chegar e CENTRALIZAR no terreno
CAMINHOS_DOS_16_TERRENOS = [
    [(1135, 158), (798, 317)],                # Cliques para chegar no Terreno 1
    [(1483, 172), (744, 308)],#, (747, 302)],   # Cliques para sair do 1 e chegar no 2
    [(1522, 358), (1142, 377), (793, 323)],#, (747, 302)],   # Cliques para sair do 2 e chegar no 3
    [(75, 427), (798, 271), (764, 297)],
    [(725, 1079), (725, 1079), (964, 580), (1168, 301), (802, 329)], #terreno 5
    [(1584, 478), (1773, 1079), (1082, 1079), (1471, 1079), (1072, 691), (1123, 321), (793, 323)], #terreno 6
    [(1258, 313), (1163, 364), (793, 323)], #terreno 7
    [(1332, 1079), (1072, 912), (1164, 335), (793, 323)], #terreno 8
    [(1384, 531), (1134, 345), (793, 323)], #terreno 9
    [(1280, 1079), (1130, 895), (1153, 336), (793, 323)], #terreno 10
    
    [(637, 1079), (637, 1079), (525, 952), (1181, 341), (793, 323)], #terreno 11 fazer manutenção no terreno 11
    
    [(157, 1079), (639, 1068), (1191, 359), (793, 323)], #terreno 12
    [(2, 782), (811, 565), (1152, 334), (793, 323)], #terreno 13
    [(1919, 416), (1919, 1001), (781, 1079), (899, 1079), (932, 571), (1199, 296), (793, 323)], #terreno 14
    [(1812, 565), (1152, 338), (793, 323)], #terreno 15
    [(851, 1079), (851, 1079), (703, 1050), (1161, 326), (793, 323)], #terreno 16
]

# --- FUNÇÕES DE AÇÃO ---

def realizar_colheita():
    print(f"Iniciando Colheita e Montaria no Terreno...")
    
    # 1. Primeiro ele colhe os 9 slots
    # Se não precisar segurar nada, apague a linha do 'with' e alinhe o 'for' à esquerda
    with pyautogui.hold('shift'): 
        for x, y in SPOT_COLETA:
            pyautogui.click(x, y, duration=1)
            time.sleep(tempo_colheita)
    
    

def preparar_semente():
    time.sleep(3)
    print(f"Pegando semente no inventário...")
    pyautogui.press("i")
    pyautogui.click(1676, 540, duration=0.5) # Slot da semente
    pyautogui.click(822, 427, duration=0.5)  # Seleciona

def realizar_plantacao(indice_terreno):
    print(f"Plantando no terreno {indice_terreno + 1}...")
    # 1. Faz a plantação normal
    #for x, y in SPOT_PLANTACAO:
        #pyautogui.click(x, y, duration=0.5)
        #time.sleep(random.uniform(1.1, 1.4))

    # --- AJUSTE DA MONTARIA ---
    # Busca a sublista de cliques para o terreno atual
    time.sleep(3)
    passos_montaria = POSICAO_MONTARIA[indice_terreno]
    
    print(f"Executando {len(passos_montaria)} cliques para estabilizar montaria...")
    
    for x, y in passos_montaria:
        # Usa botão direito para garantir que o boneco apenas ande
        pyautogui.rightClick(x, y, duration=0.8)
        # Espera o boneco chegar no ponto antes do próximo clique ou de montar
        time.sleep(random.uniform(2.5, 2.8)) 

    # Agora que ele percorreu todos os passos, ele monta
    pyautogui.press("a")
    print("Montagem estabilizada!")
    time.sleep(random.uniform(0.7, 1.2))
    pyautogui.press("esc")

def navegar_para_terreno(lista_de_cliques):
    """Executa a sequência de cliques para o boneco andar até o próximo centro"""
    for x, y in lista_de_cliques:
        pyautogui.rightClick(x, y, duration=0.9)
        time.sleep(tempo_caminhada)
    pyautogui.press("a")
    

# --- LOOP PRINCIPAL (A EXECUÇÃO) ---

def iniciar_bot():
    print("O bot começará em 3 segundos. Mude para a janela do jogo!")
    time.sleep(3)

    # O loop 'for' percorre cada terreno da nossa lista de 16
    for indice, cliques_trajeto in enumerate(CAMINHOS_DOS_16_TERRENOS):
        num_terreno = indice + 1
        print(f"--- INICIANDO TERRENO {num_terreno} ---")

        # 1. Movimentação (O boneco segue os pontos de clique até o centro)
        navegar_para_terreno(cliques_trajeto)
        
        # 2. Ações no local (Agora que ele parou no centro)

        #realizar_colheita()
        #preparar_semente()
        realizar_plantacao(indice)

        print(f"--- TERRENO {num_terreno} FINALIZADO ---\n")

    print("Ciclo de 16 terrenos completo!")

# Executa o bot
if __name__ == "__main__":
    iniciar_bot()
