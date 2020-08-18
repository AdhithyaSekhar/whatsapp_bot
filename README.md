# whatsapp_bot
A simple Whatsapp bot that can be used to send messages.
This bot uses the Selenium Webdriver along with the chromedriver to access your Whatsapp account via the website using Google Chrome.

Points to note before executing the code -

Please scan the QR code with your phone to LogIn to Whatsapp the first time .It will automatically LogIn from the next time onwards.

For the chromedriver to work correctly, you can either add its path to the Path variable under system variables or you can directly add a parameter to the webdriver.Chrome() function on the 8th line in the instabot_selenium.py file stating executable_path="PATH_POINTING_TO_YOUR_CHROMEDRIVER".

Issues may arise due to incompatibility with the chromedriver. In this case, please click this link and then download the required version. https://www.selenium.dev/downloads/

This program can also be run on other browsers, although chrome is recommended. 
