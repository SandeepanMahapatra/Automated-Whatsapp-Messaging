import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pickle
import pprint
import time
from time import sleep

#To save the cookies that has credentials
def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))

def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://web.whatsapp.com/" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):#Checks if the instance expiry a float
            cookie['expiry'] = int(cookie['expiry'])# it converts expiry cookie to a int
        driver.add_cookie(cookie)
        driver.refresh()

def delete_cookies(driver, domains=None):
    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()

#send message function
def Sendmsg():
    #enter name of receiver
    # name = input("Enter the name of user or group : ")
    name="Gudli"
    #enter the message
    # msg = input("Enter the message : ")
    msg="You are a fool!"
    #enter the count

    # count = int(input("Enter Number of count : "))
    count=5000

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
        button.click()


#get the driver for individual browser
driver = webdriver.Chrome('C:/Users/KIIT/Desktop/Files/chromedriver')

#scan the QR code
print("Scan the QR code")
driver.get("https://web.whatsapp.com/")

#send image or video file function
# def sendimgvid():
#     #enter name of receiver
#     # name = input("Enter the name of user or group : ")
#     #enter file path
#     # filepath = input("Enter the file path (Image,Video) : ")
#
#     user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
#     user.click()
#
#     attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
#     attachment_box.click()
#
#     imgvid_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
#     imgvid_box.send_keys(filepath)
#
#     sleep(3)
#
#     send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
#     send_button.click()

#user input
# print("Press 1 for sending multiple messages \nPress 2 to send an image or video \n Press 3  to exit")
# n = int(input())
# if (n == 1):
#     Sendmsg()
#
# elif(n == 2):
#     sendimgvid()
#
# elif(n==3):

cookies_location = "C:/Users/KIIT/Desktop/Files/cookies.txt"

# success = "false"
# while not success:
#     try:
#         Sendmsg()
#         success = "true"
#     except:
#         pass
#
# if(success=="false"):
#     time.sleep(2)
#     load_cookies(driver, cookies_location)
#     time.sleep(10)
#     input()
#     Sendmsg()
#     success="True"
# print(success)
# Sendmsg()
#
# cookies = driver.get_cookies() # returns list of dicts
#
# login_status = False
# for cookie in cookies:
#     if cookie['name'] == 'login_token':
#         login_status = True
#         break
#
# if login_status:
#     print('login ok')
# else:
#     print('login incorrect')

input("PRESS ANY KEY TO CONTINUE")
#Loading the cookies
# load_cookies(driver, cookies_location)

Sendmsg()
# save_cookies(driver, cookies_location)
input("DONE KEY")

quit()