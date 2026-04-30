import time
from src.utils.config import caminhosTerrenos, caminhosIlhas, ilhas
from src.core.farmActions import pegar_itens, realizarColheita, prepararSemente, realizarPlantacao, sementeHorta, guardar_itens, viajar_ilha, posicionarIlha
from src.navigation.movement import navegarTerreno, navegarIlha

#Função Principal de Inicialização
#Responsável por chamar as funções na ordem correta
def iniciarAcoes():
    print("Iniciando em 3 segundos...")
    time.sleep(3)

    #Loop para percorrer nos terrenos
    for ilha in range(3):
        if ilha < 2:
            for indice, cliques_trajeto in enumerate(caminhosTerrenos):
                numTerreno = indice + 1
                print(f"Iniciando processo/terreno {numTerreno}")

                #Chama função de navegar nos terrenos
                navegarTerreno(cliques_trajeto)

                #Funções de ação
                realizarColheita()

                #Estrutura de decisão necessária para fazer a troca de semente de acordo com o número do terreno na fazenda 2
                if 12 <= numTerreno <= 16 and ilha == 1:
                    sementeHorta(numTerreno)
                else:
                    prepararSemente()

                realizarPlantacao(indice)
                print(f"Terreno {numTerreno} finalizado.\n")
                
            print("Ciclo de 16 terrenos completo!")

            #Loop para guardar itens coletados e viajar entre as ilhas
            if ilha <= 1:
                for indice, cliques_trajeto in enumerate(caminhosIlhas):
                    quantidade = indice + 1
                    navegarIlha(cliques_trajeto, descerMontaria=5 if indice == 0 else None)
                    if quantidade == 1:
                        guardar_itens()
                    elif quantidade == 2:
                        print("Viajando entre ilhas...")
                        time.sleep(3)
                        viajar_ilha(ilhas[ilha])
                        time.sleep(12)
                #Funções para pegar itens e posicionar o personagem na ilha 2 para realizar o processo de colheita e plantação.
                time.sleep(1.5)
                pegar_itens()
                posicionarIlha()
        else:
            print("Iniciando processo na ilha 3...")
            
    
#Executa o bot
if __name__ == "__main__":
    iniciarAcoes()