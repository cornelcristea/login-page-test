# ==================================
# Test a 'Log in' page if a error message is displayed for wrong email or password.
# Version: 3.1
# Developer: Cornel Cristea
# ==================================

# ----------------------------------
# import libraries
# ----------------------------------
from selenium import webdriver              # to have control on browser
import os                                   # to create folders
import unittest                             # to run unit tests                 
from time import sleep                      # to delay program
import HtmlTestRunner                       # to generate HTML report

# ----------------------------------
# create directories (Screenshots, Reports)
# ----------------------------------
ssFolder = 'Screenshots'
reportsFolder = 'Reports'
ssPath = os.path.join(os.getcwd(), ssFolder)                # get full path for Screenshots folder
reportsPath = os.path.join(os.getcwd(), reportsFolder)      # get full path for Reports folder

if not os.path.exists(ssFolder):                            # if folders not exist
    os.mkdir(ssFolder)                                      # create Screenshots folder in currecnt directory
    os.mkdir(reportsFolder)                                 # create Reports folder in currecnt directory

# ----------------------------------
# start tests
# ----------------------------------
class FailedLogIn(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Edge('Drivers/msedgedriver.exe')        # comment this line to change browser
        # cls.browser = webdriver.Chrome('Drivers/chromedriver.exe')    # uncomment to use Chrome browser
        # cls.browser = webdriver.FireFox('Drivers/geckodriver.exe')    # uncomment to use FireFox browser
        cls.browser.implicitly_wait(1)                        
        # cls.browser.maximize_window()                                 # uncomment to maxime the window                 
                   
    # test 1 open page
    def test_1_open_page(self):
        self.browser.get('https://jules.app')                                 
        sleep(1)
        self.browser.save_screenshot(ssFolder + '/' + 'test_1.png') 
    
    # test 2 complete email and password fields
    def test_2_complete_user_pass(self):                         
        self.browser.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys('test@email.com')
        self.browser.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys('pass123!')
        sleep(1)                                                            # delay program to make screenshot
        self.browser.save_screenshot(ssFolder + '/' + 'test_2.png')         # make screenshot for this step

    # test 3 click on Log in button
    def test_3_log_in(self):
        self.browser.find_element_by_xpath('//span[text()="Log in"]').click()   
        sleep(0.2)                                                          # delay program to make screenshot
        self.browser.save_screenshot(ssFolder + '/' + 'test_3.png')         # make screenshot for this step

    # test 4 error message
    def test_4_display_error_message(self):
        self.browser.find_element_by_xpath('//span[text()="Invalid email/password combination"]')
        sleep(0.2)                                                          # delay program to make screenshot
        self.browser.save_screenshot(ssFolder + '/' + 'test_4.png')         # make screenshot for this step

    # test 5 this test will be failed in report
    def test_5_forgot_password(self):
        self.browser.find_element_by_link_text('Forgot my password').click()
        sleep(0.2)                                                          

    # test 6 this test will be skipped
    @unittest.SkipTest
    def test_6_sign_up(self):
        self.browser.find_element_by_link_text('Sign up').click()                                                          

# ----------------------------------
# finish tests
# ----------------------------------
    @classmethod
    def tearDownClass(cls):
        cls.browser.close()                                     # close browser after ran tests
        cls.browser.quit()                                      # quit web driver 
        print('\n\nTest Completed. \n ')                        # info messages in Terminal
        print('Screenshot saved in ' + ssPath + '\n')           

# ----------------------------------
# generate HTML report 
# ----------------------------------
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reportsPath))     

