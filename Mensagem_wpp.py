from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.chrome()
navegador.get('https://web.whatsapp.com/')
navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/div/span')
navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/span/div/ul/li[1]/div')
navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/div[2]/input')