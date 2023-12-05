#Do imports
import numpy as np
import pandas as pd
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

# Set driver and initial array 
# menginisialisasi instance dari driver Chrome yang dapat digunakan untuk mengotomatisasi  tindakan di dalam browser
driver = webdriver.Chrome(executable_path=r"D:\chromeDriver\chromedriver.exe") #change parameters to your user and folder structure

# navigate to login screen
driver.get('https://www.twitter.com/login') #browser Chrome dikontrol oleh Selenium diarahkan ke halaman login Twitter.
driver.maximize_window() #memperbesar halaman chrome
sleep(5) #memberikan waktu bagi halaman web untuk dimuat sepenuhnya sebelum tindakan selanjutnya

# Input username
username = driver.find_element_by_xpath('//input[@name="text"]') #langkah untuk menemukan elemen HTML pada halaman web dengan menggunakan XPath
#Elemen ini ditemukan dan disimpan dalam variabel username.
username.send_keys('diansukmahani@gmail.com') #Mengirimkan username ke elemen input
username.send_keys(Keys.RETURN) #menekan tombol "Return" atau "Enter" setelah memasukkan username
sleep(3)


# Input Password
password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys('sukmahani16')
password.send_keys(Keys.RETURN)
sleep(3) 


driver.get("https://twitter.com/i/communities/1562271278744354816") # Membuka halaman Komunitas 
time.sleep(10) #change according to your pc and internet connection
    
tweets = [] #embuatan sebuah list kosong yang akan digunakan untuk menyimpan tweet
result = False #
    
# Get scroll height after first time page load
last_height = driver.execute_script("return document.body.scrollHeight") #untuk mendapatkan tinggi (height) halaman web

last_elem=''
current_elem=''

while True:
    
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #menggulir ke bawah halaman web ke akhir (bottom) halaman
    # Wait to load page
    time.sleep(6)
    # Calculate new scroll height and compare with last scroll height
    # Menghitung tinggi halaman web, kl sama tinggi dg halaman sebelumnya berarti udh tidak ada tweet yg bisa diambil 
    new_height = driver.execute_script("return document.body.scrollHeight") 
    if new_height == last_height:
        break
    last_height = new_height
    
    # update all_tweets to keep loop
    # mencari semua elemen yang mengandung tweet pada halaman web menggunakan XPath
    all_tweets = driver.find_elements(By.XPATH, '//div[@data-testid]//article[@data-testid="tweet"]')

    # mengekstrak tanggal dan teks dari setiap tweet dan menyimpannya dalam list tweets. 
    for item in all_tweets[1:]: # skip tweet already scrapped

        print('--- date ---')
        try:
            date = item.find_element(By.XPATH, './/time').text
        except:
            date = '[empty]'
        print(date)

        print('--- text ---')
        try:
            text = item.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
        except:
            text = '[empty]'
        print(text)

        #Append new tweets replies to tweet array
        tweets.append([ date, text])
               
        if (last_elem == current_elem):
            result = True
        else:
            last_elem = current_elem

driver.close()

df = pd.DataFrame(tweets, columns=['Date of Tweet','Tweet'])
df.to_csv('scrape12.csv', index=False, encoding='utf-8') #save a csv file in the downloads folder, change it to your structure and desired folder

print(df)




















