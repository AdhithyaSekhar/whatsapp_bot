from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(executable_path= r"C:\Users\ADHI\Downloads\chromedriver_win32 (1)\chromedriver.exe",options=chrome_options)
driver.get("https://web.whatsapp.com/")

name = input("Enter Recipient Name : ")
msg = input("Enter the message to be sent : ")
count = int(input("Enter number of times the message to be displayed : "))

last_ht, ht = 0, 2
not_found = True

while True:
    try:
        scroll_box = driver.find_element_by_xpath('//*[@id="pane-side"]')
        break
    except:
        sleep(2)
while not_found:
    try:
        recipient = driver.find_element_by_xpath('//span[contains(@title,"'+ name +'")]')
        recipient.click()
        sleep(1)
        message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        not_found = False
    except:
        print("Searching for " + name)
        # Scroll down by 5 names
        driver.execute_script("""
        arguments[0].scrollTo(0,arguments[1])
        """, scroll_box, ht)
        last_ht = ht
        ht += 5


for i in range(count):
    message_box.send_keys(msg)
    sleep(0.5)
    send_button=driver.find_element_by_class_name('_1U1xa')
    send_button.click()


sleep(10)
