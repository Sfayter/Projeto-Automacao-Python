import pyautogui
import time

#Função de caminhar entre os terrenos de acordo com as coordenadas passadas na lista e sublistas da lista caminhosTerrenos
def navegarTerreno(lista_de_cliques):
    
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