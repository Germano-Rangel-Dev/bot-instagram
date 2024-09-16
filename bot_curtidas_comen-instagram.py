import pyautogui
from time import sleep
from pyscreeze import ImageNotFoundException
import webbrowser

def logout():
    pyautogui.click(1314,724, duration=3)
    sleep(2)
    pyautogui.click(1451,717, duration=2)

# 1 - navegar até o site https://www.instagram.com
while True:
    webbrowser.open('https://www.instagram.com')
    sleep(1)
# 2 - entrar com o usuario
    pyautogui.click(1947,315, duration=1)
    sleep(1)
    pyautogui.typewrite('seu nomeDeUsuario, email ou telefone')
    sleep(1)
# 3 - entrar com senha
    pyautogui.click(1955,358, duration=1)
    sleep(1)
    pyautogui.typewrite('suaSenhaDoInstragram')
    sleep(1)
# 4 - clicar no botão de entrar
    pyautogui.click(1957, 408, duration=3)
    sleep(1)
# 5 - clicar em não salvar para o navegador não salvar usuario e senha
    pyautogui.click(1785, 479, duration=4)
    sleep(1)
# 6 - fechar a janela de salvar senha (somente se aparecer)
    #pyautogui.click(x,y, duration= float)
    #sleep(int)
# 7 - pesquisar pela página que pretende dar comentário e like
    pyautogui.click(1317,296, duration=2)
    sleep(1)
    pyautogui.click(1400,226, duration=1)
    sleep(1)
    pyautogui.typewrite('nomeDeQuemSeraPesquisado')
    sleep(1)
# 8 - Entrar na página
    pyautogui.click(1447, 287, duration=2)
    sleep(1)
# 9 - Clicar na postagem mais recente
    pyautogui.click(1512,500, duration=2)
    sleep(1)
# 10- verificar se já houve ou não curtida minha na página
    coracao = pyautogui.useImageNotFoundException('coracao.png')
    sleep(1)
    
# 11- se curtida, fazer nada e pausar o bot por 24h
    if coracao is not None:
        logout()
        sleep(86400)
        
# 12- se não tiver curtido, curtir
    elif coracao == None:
        pyautogui.click(1798,536, duration=1)
# 13- se não tiver comentado, comentar na foto
        pyautogui.click(1836,537, duration=1)
        sleep(3)
        pyautogui.click(1924,642, duration=1)
        sleep(2)
        pyautogui.typewrite('Amei a foto!')
        sleep(2)
        pyautogui.click(2122,640, duration=1)
        sleep(1)
# 13.5- saindo da conta:
    logout()        
# 14- pausar por 24h
    sleep(86400)
# 15- Apos 24h, rodar tudo de novo
# no 15, colocamos o codigo na função WHILE:


