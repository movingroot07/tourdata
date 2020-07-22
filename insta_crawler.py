import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from secret import insta_id, insta_pw

from sqlalchemy import create_engine

keyword = "한달살기"

url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

browser = webdriver.Chrome('chromedriver.exe')
browser.get(url)
time.sleep(5)


if browser.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1)'):
    browser.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1)').click()
    login = browser.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.fPMEg._8PWHW > div > div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.lDRO1 > div > div > div.gr27e.o7laV > div > form > div:nth-child(2) > div > label > input')
    login.send_keys(insta_id)
    login = browser.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.fPMEg._8PWHW > div > div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.lDRO1 > div > div > div.gr27e.o7laV > div > form > div:nth-child(3) > div > label > input')
    login.send_keys(insta_pw)
    login.send_keys(Keys.RETURN)
    
    time.sleep(3)
    browser.find_element_by_css_selector('#react-root > section > main > div > div > div > section > div > button').click()
    print('로그인안함')

elif browser.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.fPMEg._8PWHW'):
    login = browser.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.fPMEg._8PWHW > div > div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.lDRO1 > div > div > div.gr27e.o7laV > div > form > div:nth-child(2) > div > label > input')
    login.send_keys(insta_id)
    login = browser.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.fPMEg._8PWHW > div > div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.lDRO1 > div > div > div.gr27e.o7laV > div > form > div:nth-child(3) > div > label > input')
    login.send_keys(insta_pw)
    login.send_keys(Keys.RETURN)
    
    time.sleep(3)
    browser.find_element_by_css_selector('#react-root > section > main > div > div > div > section > div > button').click()
    print('로그인함')


time.sleep(5)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]').click()

insta_bodies = []
insta_dates = []

time.sleep(3)
# while True:

for i in range(10):
    body = browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > span').text
    date = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/div[2]/a/time').get_attribute('datetime')
    insta_bodies.append(body)
    insta_dates.append(date)

    time.sleep(1)

    if i == 0:
        browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
    elif i != 0:
        browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()

    time.sleep(2)

print(insta_bodies, insta_dates)