from unicodedata import name
import pywhatkit
import pyautogui
import keyboard as k
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
import time
from sre_constants import IN
import phonenumbers
from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

win = Tk() # Some Tkinter stuff
screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor


#Spreadsheet files 
getdatafromsheet = True
scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("WhatsAppBot").sheet1

data = sheet.get_all_records() 
cell = sheet.cell(2,7).value 
#pp(cell)
new = '0'
def randomFunctionYouWantToKeepRunning(cell):
       print("WhatsApp BOT is running in Background Every 10 secs.")
       file1 = open("latest.txt","r")
       old = file1.read()
       cell = sheet.cell(2,7).value 
       if old == cell:
        pp("No new Updates")
        exit
       else :
        new = cell
        with open('latest.txt', 'w') as f:
         f.write(new)
        pp("New number found")
        #getdatafromsheet == False
        # database number 
        new = phonenumbers.parse(new, "IN")
        x = phonenumbers.format_number(new, phonenumbers.PhoneNumberFormat.E164)
        number = x
        print(number)
        #WhatsApp Bot
        
        currentPath = __file__.split("Automate.py")[0]
        driverPath = currentPath + r"chromedriver.exe"
        
        chromeOptions = Options()
       
        #chromeOptions.headless = True
        chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
        chromeOptions.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
        chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
        #driver = webdriver.Chrome(driverPath, options=chromeOptions)
       

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)

        #Arguments
        name = sheet.cell(2,8).value 
        message = "Hello " + name + " !!" 
        #driver.get("https://web.whatsapp.com/send?phone={number}&text={quote(message)}")
        #driver.get("https://web.whatsapp.com/send?phone=+919766400530&text=Hi")
        


        site = f"https://web.whatsapp.com/send?phone={number}&text={message}"
        driver.get(site)
        driver.implicitly_wait(10)
        time.sleep(5)
        #WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "app")))
        text = ''' 
        
        Welcome to Dewa Direction.

        We got your message, but we’re a little busy making sure everyone is taken care of. 
        A representative will reply when they’re free - the estimated wait time is 10 -15 minutes.'''   
        
        #element = driver.find_element_by_xpath("//div//button/span[@data-icon='send']")
        inp_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
        input_box = driver.find_element(By.XPATH,inp_xpath)
        time.sleep(2)
        input_box.send_keys(text + Keys.ENTER)
        time.sleep(2)
        #element = driver.find_element(By.XPATH,"//div//button/span[@data-icon='send']")
        # Loads a send button
        #driver.implicitly_wait(10)
        
        # Clicks the send button
        
        #element.click()
        ##To send attachments
        ##click to add
        
        # Sleeps for 5 secs to allow time for text to send before closing window
        time.sleep(3) 

        # Closes window
        driver.close()
        print("Welcome message Sent!")
        randomFunctionYouWantToKeepRunning(cell)



while getdatafromsheet == True:
    randomFunctionYouWantToKeepRunning(cell)
    time.sleep(5)





# database number 

new = phonenumbers.parse(new, "IN")
x = phonenumbers.format_number(new, phonenumbers.PhoneNumberFormat.E164)

number = x
print(number)


#WhatApp BOT 


t = time.localtime()
hour = time.strftime("%H", t)
h=int(hour)
minute =time.strftime("%M", t) 
m=int(minute)
m=m+1
pywhatkit.sendwhatmsg(number, 'Hi Bro', h, m)
time.sleep(3)
pyautogui.click(1330, 695)
time.sleep(3)
k.press_and_release('ctrl+w')
#k.press_and_release('enter')
getdatafromsheet = True
