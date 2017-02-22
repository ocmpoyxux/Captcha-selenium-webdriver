from selenium import webdriver
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
from datetime import datetime, timedelta
import time
import sys
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
#import skimage.morphology as morphology
#import cv2
#import tesseract
import string
import pytesseract

driver = webdriver.Firefox()
driver.get("https://bit-changer.net/ru/contacts/")

name_field = driver.find_element_by_name('name')
name_field.send_keys("Test+Valerii")

email_field = driver.find_element_by_name('email')
email_field.send_keys("ocmpoyxux@gmail.com")

text_field = driver.find_element_by_name('text')
text_field.send_keys("UI Test")

alphabet = list(string.ascii_lowercase)
i=1
num=0

driver.get_screenshot_as_file('/home/v.ostrouhih/screenshots/screenshot'+ alphabet[num] +'i'+'.png')
iframe= driver.find_element_by_xpath('.//*[@id="form-contacts"]/table/tbody/tr[4]/td[2]/img')
location = iframe.location
size = iframe.size

im = Image.open('/home/v.ostrouhih/screenshots/screenshot'+ alphabet[num] +'i'+'.png') # uses PIL library to open image in memory
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
im = im.crop((left, top, right, bottom)) # defines crop points
im.save('/home/v.ostrouhih/captchas/captcha'+ alphabet[num] +'i'+'.png') # saves new cropped image

scrin = Image.open ('/home/v.ostrouhih/captchas/captcha'+ alphabet[num] +'i'+'.png')

text = pytesseract.image_to_string(scrin)
print (text)











#content = driver.find_element_by_class_name('button-big-form-1.butt-send-form-w-check')
#content.click()

driver.close()
