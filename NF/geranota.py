import pyautogui
import time

pyautogui.PAUSE = 0.7
CNPJ_ATLANTICA = "19.333.416/0001-50"
CNPJ_NUSEED = "05.734.807/0002-52"

def geraNota(data, cnpj, mes, valor):
    # abrir site
    pyautogui.press("win")
    pyautogui.write("firefox")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.press("F6")
    pyautogui.write("https://www.nfse.gov.br/EmissorNacional/Dashboard")
    pyautogui.press("enter")

    # logar no site
    pyautogui.click(x=1356, y=498)
    pyautogui.click(x=1315, y=421)
    pyautogui.write("025.048.301-73")
    pyautogui.click(x=1543, y=482)

    time.sleep(1)
    pyautogui.click(x=1169, y=380)
    pyautogui.write("I86b=1t21l")
    pyautogui.click(x=1432, y=508)
    # pyautogui.moveTo(x=1873, y=150)
    # pyautogui.click()
    time.sleep(1)

    #move para o menu de PESSOAS
    pyautogui.click(x=1322, y=171)
    pyautogui.click(x=1258, y=281)

    #preencher as informações PESSOAS
    pyautogui.click(x=151, y=438)
    pyautogui.write(data)
    pyautogui.press("tab")
    pyautogui.scroll(-500)
    # pyautogui.moveTo(x=132, y=799) # coordenadas para o chrome
    pyautogui.moveTo(x=144, y=785) # coordenadas para o firefox
    time.sleep(1)
    pyautogui.click()
    pyautogui.scroll(-600)
    # pyautogui.click(x=150, y=418) # coordenadas para o chrome
    pyautogui.click(x=155, y=400) # coordenadas para o firefox
    if cnpj == 0:
        pyautogui.write(CNPJ_ATLANTICA)
    else:
        pyautogui.write(CNPJ_NUSEED)
    pyautogui.press("tab")
    pyautogui.scroll(-600)
    time.sleep(1)
    # pyautogui.click(x=1728, y=738) # coordenadas para o chrome
    pyautogui.click(x=1718, y=728) # coordenadas para o firefox

    # #avança para SERVIÇOS
    time.sleep(1)
    #pyautogui.click(x=879, y=472) # coordenadas para o chrome
    pyautogui.click(x=869, y=462) # coordenadas para o firefox
    pyautogui.write("Acreuna")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.write("suporte")
    pyautogui.press("enter")
    time.sleep(1)
    #pyautogui.click(x=127, y=733)
    pyautogui.click(x=139, y=726)
    time.sleep(1)
    #pyautogui.click(x=170, y=1017)
    pyautogui.click(x=160, y=1007)
    time.sleep(1)
    pyautogui.write(f"ASSISTENCIA TECNICA DE INFORMATICA REFERENTE AO MES DE {mes}")
    pyautogui.scroll(-1200)
    # pyautogui.click(x=141, y=652)
    pyautogui.click(x=161, y=778)
    pyautogui.write("PIX: 64 99625-6186")
    pyautogui.scroll(-200)
    # #pyautogui.click(x=1713, y=957)
    pyautogui.click(x=1736, y=894)

    #preencher TRIBUTAÇÃO
    time.sleep(1)
    pyautogui.click(x=341, y=481)
    pyautogui.write(valor)
    pyautogui.press("tab")
    pyautogui.scroll(-1050)
    # pyautogui.click(x=1751, y=1015)
    pyautogui.click(x=1724, y=1001)
    # pyautogui.moveTo(x=368, y=307)

    # # finalizar GERAR NOTA
    pyautogui.click(x=341, y=481)
    pyautogui.scroll(-3000)
    pyautogui.scroll(-3000)
    pyautogui.scroll(-3000)

    pyautogui.click(x=1717, y=749)
    # pyautogui.moveTo(x=1749, y=809)# coordenadas para o chrome

    # baixar nota
    #pyautogui.moveTo(x=720, y=980) # coordenadas para o chrome
    pyautogui.click(x=742, y=969)