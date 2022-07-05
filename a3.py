# from selenium import webdriv
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
filepath = input('Enter your filepath (images/video): ')

input('Enter anything after scanning QR code')

# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()
user1 =driver.find_element(by='xpath', value='//span[@title= "{}"]'.format(name))
# user1 = driver.find_element_by_xpath('//span[@title= "{}"]'.format(name))
user1.click()
attachment_box = driver.find_element(by='xpath',value='//div[@title = "Attach"]')
# attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

image_box = driver.find_element(by='xpath',value= '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
# image_box = driver.find_element_by_xpath(
    # '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

send_button = driver.find_element(by='xpath',value='//span[@data-icon="send"]')
# send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()


# C:/Users/misinternee/Downloads/images.jpg