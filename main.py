import time
from src.utils.config import caminhosTerrenos
from src.core.farmActions import realizarColheita, prepararSemente, realizarPlantacao, sementeHorta
from src.navigation.movement import navegarTerreno

#Função Principal de Inicialização
#Responsável por chamar as funções na ordem correta
def iniciarAcoes():
    opcao = int(input(" 1- Colher Abóbora\n 2- Colher Leite de Vaca\n 3- Colher Hortaliças\n"))
    print("Iniciando em 3 segundos...")
    time.sleep(3)

    #Loop para percorrer nos terrenos
    for indice, cliques_trajeto in enumerate(caminhosTerrenos):
        numTerreno = indice + 1
        print(f"Iniciando Terreno {numTerreno}")

        #Chama função de navegar nos terrenos
        navegarTerreno(cliques_trajeto)

        #Funções de ação
        realizarColheita()

        #Estrutura de decisão necessária para fazer a troca de semente de acordo com o número do terreno na fazenda 3
        if 12 <= numTerreno <= 16 and opcao == 3:
            sementeHorta(numTerreno)
        else:
            prepararSemente()

        realizarPlantacao(indice)
        print(f"Terreno {numTerreno} finalizado.\n")
        
    print("Ciclo de 16 terrenos completo!")

#Executa o bot
if __name__ == "__main__":
    iniciarAcoes()