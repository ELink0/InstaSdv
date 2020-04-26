#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
from selenium.webdriver.support import ui
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.chrome.options import Options
import os
import time
import sys
import requests
from getpass import getpass
def temporizador():
	tempo = 0
	controle = 1800
	while tempo <= 1800:
		time.sleep(1)
		limpaTerminal = os.system('cls' if os.name == 'nt' else 'clear')
		print("Segundos restantes para o próximo comentário: {}".format(controle))
		controle -= 1
		tempo += 1

	pesquisarPublicacoes()

def pesquisarPublicacoes(palavrachave):
	limpaTerminal = os.system('cls' if os.name == 'nt' else 'clear')
	print("Localizando publicação")
	pesquisar = driver.find_element_by_class_name('XTCLo')
	driver.get('https://www.instagram.com/explore/tags/'+ palavrachave+'/')
	post = driver.find_element_by_class_name('v1Nh3').click()
	comentar()

def comentar(comentario):
	print("Publicação localizada!\nPreparando campo de comentário...")
	time.sleep(5)
	limpaTerminal = os.system('cls' if os.name == 'nt' else 'clear')
	comenta = driver.find_element_by_class_name('Ypffh')
	comenta.click()
	comenta = driver.find_element_by_class_name('Ypffh')
	comenta.send_keys(comentario)
	comenta.send_keys(Keys.ENTER)
	print("Comentário adicionado!")
	temporizador()

def login():
	try:
		# Verifica se já está logado
		driver.get('https://www.instagram.com/accounts/login/')
		while(tempoEsperaDois.until(EC.title_contains(('Entrar'))) == True):
			usuario = input(str("Nome de usuário: "))
			senha = getpass(("Senha: "))

			usuarioInput = driver.find_elements_by_css_selector('form input')[0]
			senhaInput = driver.find_elements_by_css_selector('form input')[1]
			usuarioInput.send_keys(usuario)
			senhaInput.send_keys(senha)
			senhaInput.send_keys(Keys.ENTER)
			time.sleep(3)
			autenticado()


		while(tempoEsperaDois.until(EC.title_is(('Instagram'))) == True):
			autenticado()

	except:
		print("Já conectado!\n\n\n Aguarde...")
		autenticado()

def autenticado():
	limpaTerminal = os.system('cls' if os.name == 'nt' else 'clear')
	print("Conectado!")
	menu()

def menu():
	limpaTerminal = os.system('cls' if os.name == 'nt' else 'clear')
	escolha = int(input("""
===== INSTA BOT =====
1 - Iniciar
0 - Sair

Digite a opção desejada: """))

	if escolha == 1:
		print("Carregando...")
		print("Palavra-chave, vai ser a # para ser pesquisada. Ex: chuvadeseguidores\n")
		palavrachave = input("Digite a palavra-chave: ")
		print("Palavra-chave definida: #{}".format(palavrachave))
		time.sleep(1)
		pesquisarPublicacoes(palavrachave)
	if escolha == 0:
		print('\nObrigado por usar!')
		sys.exit()
	else:
		print("Opção inválida!")
		time.sleep(1)
		menu()

def inicio():
	global driver
	global tempoEspera
	global tempoEsperaDois

	try:
		if os.name == 'nt':
			# Configurações para Windows
			chrome_diretorio = "{0}/.chrome/data_dir/whatsapp_web_cli".format(os.environ['HOME'])
			# Caso o diretório não exista, irá ser criado
			if not os.path.exists(chrome_diretorio):
					os.makedirs(chrome_diretorio)

			configs_driver = webdriver.ChromeOptions()

			configs_driver.add_argument("user-data-dir={0}".format(chrome_diretorio))

			driver = webdriver.Chrome(executable_path="./src/chromedriver.exe", chrome_options=configs_driver)

			driver.set_page_load_timeout(60 * 5)
			tempoEspera = WebDriverWait(driver, 10)
			tempoEsperaDois = WebDriverWait(driver, 2)
		else:
			# Configurações para Linux

			chrome_diretorio = "{0}/.chrome/data_dir/instagram_web_cli".format(os.environ['HOME'])
			
			# Caso o diretório não exista, irá ser criado
			if not os.path.exists(chrome_diretorio):
					os.makedirs(chrome_diretorio)

			configs_driver = Options()
			configs_driver.add_argument("user-data-dir={0}".format(chrome_diretorio))
			# configs_driver.add_argument('--headless') # Modo janela invisivel
			configs_driver.add_argument('--no-sandbox')

			driver = webdriver.Chrome(executable_path="./src/chromedriver", chrome_options=configs_driver)

			driver.set_page_load_timeout(60 * 5)
			tempoEspera = WebDriverWait(driver, 10)
			tempoEsperaDois = WebDriverWait(driver, 2)

	except KeyError:
		print("Driver do Chrome não encontrado!\n")
		time.sleep(5)
		sys.exit(1)

	login()

inicio()