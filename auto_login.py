# ==================================
# Test a 'Log in' page if a error message is displayed for wrong email or password.
# Version: prototype 
# Developer: Cornel Cristea
# ==================================


from selenium import webdriver                                                     
from time import sleep

browser = webdriver.Edge('Drivers/msedgedriver.exe')        
browser.implicitly_wait(1)                        
browser.maximize_window()

browser.get('https://jules.app')
sleep(2)                    

browser.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys('test@email.com')
browser.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys('pass123!')
sleep(1)                                                       
         
browser.find_element_by_xpath('//span[text()="Log in"]').click()   
sleep(0.2)                                                     
       
browser.find_element_by_xpath('//span[text()="Invalid email/password combination"]')
sleep(2)                                                     
      
browser.close()
browser.quit()


