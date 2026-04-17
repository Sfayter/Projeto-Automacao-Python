import pyautogui

#Configuração global de segurança
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

#Slots de colheita
spotColeta = [
    (968, 379), (954, 533), (827, 454),
    (1083, 472), (1205, 392), (986, 345),
    (862, 296), (773, 472), (650, 577)
]

#Slot dos baús para guardar itens e pegar itens
slotItens = [
    (1676, 540), (63, 404),       #Guardar semente do slot 1
    (1735, 539), (124, 404),      #Guardar abóbora do slot 2
    (1795, 540), (182, 404),      #3
    (1854, 541), (243, 404),      #4
    (1771, 454), (299, 404),      #5 Guardar montaria
]

#Posições da montaria
#Foi necessário definir as coordenadas nesse formato no lugar de um loop com uma coordenada fixa, pois a montaria 
#varia o posicionamento de acordo com o terreno de colheita
posicaoMontaria = [
    [(942,829), (966, 400)],    #1
    [(942, 825), (986, 409)],  #2
    [(942, 830), (976, 391)],  #3
    [(942, 829), (989, 408)],  #4
    [(942, 829), (989,404)],   #5 
    [(943, 828), (997, 402)],  #6 
    [(942, 828), (980, 404)],  #7
    [(942, 829), (988, 403)],  #8
    [(942, 829), (988,403)],   #9
    [(942, 829), (1001, 403)], #10
    [(944, 829), (994,409)],   #11
    [(942, 829), (974, 403)],  #12
    [(944, 829), (1000,408)],  #13
    [(942, 829), (995,406)],   #14
    [(942, 829), (982,399)],   #15
    [(942, 829), (983,404)],   #16  
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
    [(967, 249), (974, 227)],                                                       #Coordenadas para chegar na posição inicial do terreno 1
    [(1362, 196), (979, 211)],                                                      # 1 > 2
    [(1568, 310), (1000, 210)],                                                     # 2 > 3
    [(262,  369), (517, 377), (978, 208)],                                          # 3 > 4
    [(852, 1079), (790, 1079), (978, 189)],                                         # 4 > 5
    [(1582, 323), (1713, 1079), (1409, 1079), (921, 1079), (1324, 827), (987, 211)],# 5 > 6
    [(1313, 266), (1002, 221)],                                                     # 6 > 7
    [(744, 1001), (1095, 1020), (1515, 691), (943, 141), (963, 224)],               # 7 > 8 Atualizar o terreno
    [(1461, 456), (979, 192)],                                                      # 8 > 9
    [(1322, 1079), (1215, 695), (985, 215)],                                        # 9 > 10
    [(502, 1075), (1503, 850), (50,856),(989,786),(981, 213)],                      # 10 > 11
    [(377, 939), (716, 933), (989, 231)],                                           # 11 > 12
    [(68, 679), (962, 232)],                                                        # 12 > 13
    [(1919, 530), (1422, 350), (1685, 1079), (1423, 1079), (131, 893), (980, 193)], # 13 > 14
    [(1841, 498), (1003, 183)],                                                     # 14 > 15
    [(761, 1079), (290, 874), (1272, 834), (1145, 693), (999, 150)],                # 15 > 16
]

caminhosIlhas = [
    [(1016, 0), (303, 0), (0, 176), (697, 214), (1111, 338)],                       #Caminha até o baú
    [(809, 1045), (344, 937), (748, 477)],                                          #Caminha até o viajante
    [(1555, 79), (1022, 207)],                                                      #Pegar montaria e semente na ilha 2
]

posicionamentoIlha = [
    (0, 897), (743, 756), (966, 895)                                                #Caminha para o ponto inicial de colheita e plantação da ilha 2
]