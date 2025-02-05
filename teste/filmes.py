from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

nome = list()
driver = webdriver.Chrome()
username = 'diogovaladao'
senha = 'n2o2v1a2'
driver.get("https://letterboxd.com/")
sleep(100)