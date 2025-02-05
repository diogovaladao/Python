from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

nome = list()
# SENHA =   Deutschland88

# NUMCLIENTE = 12716007
driver = webdriver.Firefox()
driver.get("https://meiobit.com/")
#driver.get("https://portal.xpi.com.br/default.aspx")
sleep(1)
#cabecalho = driver.find_elements(By.XPATH, "//div[@class='head']")
titulos = driver.find_elements(By.XPATH, "//h2")

#titulos = driver.find_elements(By.XPATH, "//div[@class='caption box65 double-padding-left f-right']")
for titulo in titulos:
    #print(titulo.text)
    nome.append(titulo.text)
    print(titulo.text)
#sleep(5)
