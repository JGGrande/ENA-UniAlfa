from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


def temTrabalhoHoje(dataTrabalho):
    dataFromatada = datetime.strptime(dataTrabalho, '%d/%m/%Y')
    dataAtual = datetime.now()

    if dataAtual == dataFromatada:
        return True

    return False


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://alfa.matheusacademico.com.br/index_aluno.asp')

# Passa a tela de login
driver.find_element(By.CSS_SELECTOR, '#txtusuario').send_keys(
    os.environ.get("RA"))
driver.find_element(By.CSS_SELECTOR, '#txtsenha').send_keys(
    os.environ.get("PASSWORD"))
driver.find_element(By.CSS_SELECTOR, '#enviar').submit()

# Chega nos Trabalhos

driver.find_element(
    By.CSS_SELECTOR, '#wrapper > ul > li.IconSala_virtual').click()
driver.find_element(
    By.CSS_SELECTOR, '#wrapper > ul > li.IconSala_virtual > ul > li:nth-child(1)').click()
sleep(3)
driver.find_element(
    By.CSS_SELECTOR, '#divmain2 > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > a:nth-child(1)').click()
sleep(1)

elementoPai = driver.find_element(
    By.CSS_SELECTOR, '#divmain > div > table > tbody > tr:nth-child(2)')
filhosElemento = elementoPai.find_elements(By.CSS_SELECTOR, 'td')

dataUltimoTrabalho = filhosElemento[3].text
nomeDisciplina = filhosElemento[2].text
descricao = filhosElemento[5].text

if temTrabalhoHoje(dataUltimoTrabalho):
    print(
        f'Tem trabalho Hoje! da materia {nomeDisciplina} descrição: {descricao}')
else:
    print(
        f'Não tem trabalho hoje! ultimo trabalho adicionado foi da materia {nomeDisciplina} descrição: {descricao} em {dataUltimoTrabalho}')

sleep(1000)
