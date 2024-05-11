import os
import time
from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Ejercicio navegacion web
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://bienes-raices-topaz.vercel.app/")
time.sleep(3)
nosotros = driver.find_element(By.CSS_SELECTOR,'a[href="nosotros.html"]')
nosotros.click()
time.sleep(3)
anuncios = driver.find_element(By.CSS_SELECTOR,'a[href="anuncios.html"]')
anuncios.click()
time.sleep(3)


# Ejercicio rellenado de formularios
driver.get("https://bienes-raices-topaz.vercel.app/contacto.html")
mensaje = driver.find_elements(By.ID,"mensaje")[0]
nombre = driver.find_element(By.ID,"nombre")
email = driver.find_element(By.ID,"email")
telefono = driver.find_element(By.ID,"telefono")

nombre.send_keys("Manuel")
email.send_keys("manuel.portero.leiva@gmail.com")
telefono.send_keys("+34629956368")
mensaje.send_keys("hello World")

time.sleep(3)
driver.get("https://bienes-raices-topaz.vercel.app/anuncios.html")
title_elements = driver.find_elements(By.CLASS_NAME,"precio")

templist = []

#Ejercicio Scrapping
for title_element in title_elements:
    print(title_element.get_attribute('innerText'))


time.sleep(5)
driver.close()