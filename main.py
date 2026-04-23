import time
from src.utils.config import caminhosTerrenos, caminhosIlhas, ilhas
from src.core.farmActions import pegarItens, realizarColheita, prepararSemente, realizarPlantacao, sementeHorta, guardarItens, viajar_ilha, posicionarIlha
from src.navigation.movement import navegarTerreno, navegarIlha

#Função Principal de Inicialização
#Responsável por chamar as funções na ordem correta
def iniciarAcoes():
    print("Iniciando em 3 segundos...")
    time.sleep(3)

    #Loop para percorrer nos terrenos
    for i in range(2):
        #for indice, cliques_trajeto in enumerate(caminhosTerrenos):
            #numTerreno = indice + 1
            #print(f"Iniciando processo/terreno {numTerreno}")

            #Chama função de navegar nos terrenos
            #navegarTerreno(cliques_trajeto)

            #Funções de ação
            #realizarColheita()

            #Estrutura de decisão necessária para fazer a troca de semente de acordo com o número do terreno na fazenda 2
            #if 12 <= numTerreno <= 16 and i == 1:
                #sementeHorta(numTerreno)
            #else:
                #prepararSemente()

            #realizarPlantacao(indice)
            #print(f"Terreno {numTerreno} finalizado.\n")
            
        print("Ciclo de 16 terrenos completo!")

        #Loop para guardar itens coletados e viajar entre as ilhas
        if i <= 1:
            for indice, cliques_trajeto in enumerate(caminhosIlhas):
                quantidade = indice + 1
                navegarIlha(cliques_trajeto, descerMontaria=5 if indice == 0 else None)
                if quantidade == 5:
                    guardarItens()
                elif quantidade == 1:
                    print("Viajando para a ilha 2...")
                    time.sleep(3)
                    viajar_ilha(ilhas[i])
                    time.sleep(12)
            #Funções para pegar itens e posicionar o personagem na ilha 2 para realizar o processo de colheita e plantação.
            time.sleep(1.5)
            pegarItens()
            posicionarIlha()
    
#Executa o bot
if __name__ == "__main__":
    iniciarAcoes()