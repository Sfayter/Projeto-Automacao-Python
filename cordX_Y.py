import pyautogui
import time

try:
    while True:
        #Captura a posição do mouse
        x, y = pyautogui.position()
        
        #Formata a saída para apagar a entrada anterior
        posicao = f"X: {str(x).rjust(4)} Y: {str(y).rjust(4)}"
        print(posicao, end="\r", flush=True)
        
        time.sleep(0.1) #Intervalo de atualização entre uma coordenada e outra
except KeyboardInterrupt:
    print("\nLocalização finalizada.")