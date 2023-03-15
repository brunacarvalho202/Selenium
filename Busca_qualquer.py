from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.get('https://www.w3schools.com/')
time.sleep(1)
#elemento = navegador.find_element(By.XPATH, '//*[@id="search2"]').click()
elemento = navegador.find_element(By.ID, "search2")
elemento.send_keys("python")
print(elemento)
time.sleep(2)
busca = navegador.find_element(By.XPATH, '//*[@id="learntocode_searchbtn"]').click()
time.sleep(3)
navegador.close()


