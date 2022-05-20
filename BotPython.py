from email import message
from typing import Text
from selenium import webdriver
from re import TEMPLATE, search
import json
import smtplib
import os
import time

i = 0
while i < 50:
    print("Stay on the chrome page !!!")
    i += 1

substring = ":"
settingsJson = 'settings.json'

link = "https://ge.ch/cari-online/examensPublic?pageContext=selectDate&action=select&item="
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://ge.ch/cari-online/examensPublic")


with open(settingsJson, 'r') as userSettings:
    settings = json.load(userSettings)

time.sleep(1)
idInput = driver.find_element_by_name("noReg")
idInput.send_keys(settings['idJson'])

time.sleep(1)
ddInput = driver.find_element_by_name("dateJJ")
ddInput.send_keys(settings["ddJson"])

time.sleep(1)
mmInput = driver.find_element_by_name("dateMM")
mmInput.send_keys(settings["mmJson"])

time.sleep(1)
aaaaInput = driver.find_element_by_name("dateAAAA")
aaaaInput.send_keys(settings["aaaaJson"])

time.sleep(1)
validate = driver.find_element_by_name("valider")
validate.click()

time.sleep(1)
move = driver.find_element_by_xpath(settings['moveButton'])
move.click()

time.sleep(2)
clear = lambda: os.system('cls')
clear()


def SendMail():
    senderEmail = settings['senderEmailJson']
    targetEmail = settings['targetEmailJson']
    password = settings['passwordJson']
    message = "Rendez vous disponnible"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, password)
    server.sendmail(senderEmail, targetEmail, message)

RdvAvailable = False

while True:

    week = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[1]/td[1]/font')
    currentDate = week.text

    if currentDate != settings['maxWeek']:
            time.sleep(1)

            newWeek = driver.find_element_by_name("nextWeek")
            newWeek.click()

            day1_1 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[1]')
            if search(":", day1_1.text):
                print("lundi matin")
                RdvAvailable = True

            day1_2 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[2]')
            if search(":", day1_2.text):
                print("Lundi apres-midi")
                RdvAvailable = True

            day2_1 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[3]')
            if search(":", day2_1.text):
                print("Mardi matin")
                RdvAvailable = True
    
            day2_2 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[4]')
            if search(":", day2_2.text):
                print("Mardi apres-midi")
                RdvAvailable = True

            day3_1 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[5]')
            if search(":", day3_1.text):
                print("Mercredi matin")
                RdvAvailable = True
    
            day3_2 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[6]')
            if search(":", day3_2.text):
                print("Mercredi apres-midi")
                RdvAvailable = True

            day4_1 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[7]')
            if search(":", day4_1.text):
                print("Jeudi matin")
                RdvAvailable = True
    
            day4_2 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[8]')
            if search(":", day4_2.text):
                print("Jeudi apres-midi")
                RdvAvailable = True

            day5_1 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[9]')
            if search(":", day5_1.text):
                print("Vendredi matin")
                RdvAvailable = True
    
            day5_2 = driver.find_element_by_xpath('//*[@id="idDivTablePlaceLibre"]/table/tbody/tr[2]/td[10]')
            if search(":", day5_2.text):
                print("Vendredi apres-midi")
                RdvAvailable = True
        
            if RdvAvailable == True:
                SendMail()
                RdvAvailable = False
            else :
                print("aucun rdv")
    else:
        time.sleep(1)
        retour = driver.find_element_by_name('return')
        retour.click()
        time.sleep(1)
        move = driver.find_element_by_xpath(settings['moveButton'])
        move.click()
        time.sleep(2)