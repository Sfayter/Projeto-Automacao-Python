import pyautogui
import time

#Função de caminhar entre os terrenos de acordo com as coordenadas passadas na lista e sublistas da lista caminhosTerrenos
def navegarTerreno(listaCliques):

    for x, y in listaCliques:
        pyautogui.click(x, y, duration=1)
        time.sleep(3.3)
        #if para manutenção dos terrenos
        # resposta = input("Deseja continuar?")
        # if resposta == "s":
        #      print("prosseguindo")
        #      time.sleep(1)

    pyautogui.press("a")

def navegarIlha(listaCliques, descerMontaria=None):
    indice = 0
    for x, y in listaCliques:
        indice += 1
        pyautogui.click(x, y, duration=1)
        time.sleep(3.9)
        # resposta = input("Deseja continuar?")
        # if resposta == "s":
        #      print("prosseguindo")
        #      time.sleep(1)
        if descerMontaria and indice == descerMontaria:
            pyautogui.press("a")
    
    #if para manutenção dos terrenos
    # resposta = input("Deseja continuar?")
    # if resposta == "s":
    #     print("prosseguindo")
    #     time.sleep(1)