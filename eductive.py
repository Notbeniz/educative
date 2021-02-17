from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pdfkit
password = ""

browser = webdriver.Firefox()
browser.get('https://www.educative.io/login')
username = ""


time.sleep(5)

emailInput = browser.find_element_by_name('email')
emailInput.send_keys(username)

passwordInput = browser.find_element_by_name('password')
passwordInput.send_keys(password)

loginBTN = browser.find_element_by_xpath('//button[text()="Login"]')
loginBTN.click()
time.sleep(7)
browser.get('https://www.educative.io/module/lesson/microservices-implementation/7D62VMrLjzj')

time.sleep(10)


mainBox = browser.page_source


soup = BeautifulSoup(mainBox, 'html.parser')

for link in soup.find_all('a'):
    # print(link.get('href'))
    page = str(link.get('href'))
    
    if 'module' in page :
        # pdfkit.from_url('https://www.educative.io'+page, page+'.pdf')
        # browser.get('https://www.educative.io'+page)

        print(f'https://www.educative.io'+page)
