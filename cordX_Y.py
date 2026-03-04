import pyautogui
import time

try:
    while True:
        # Captura a posição atual
        x, y = pyautogui.position()
        
        # Formata a saída para apagar a linha anterior e mostrar a nova
        posicao = f"X: {str(x).rjust(4)} Y: {str(y).rjust(4)}"
        print(posicao, end="\r", flush=True)
        
        time.sleep(0.1) # Pequeno intervalo para não sobrecarregar o processador
except KeyboardInterrupt:
    print("\nLocalização finalizada.")