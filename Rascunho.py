# http://www.cresesb.cepel.br/index.php?section=sundata&


Latitude = '8.0113981'
Longitude = '34.8734516'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

   



class solar_gather_bot():
    
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        print('Inicializado...')


    def acess_site():
        self.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")

        assert "Python running..." in self.driver.title


    def put_coords(self):
        lat_in = self.driver.find_element_by_xpath('//*[@id="latitude_dec"]')
        lat_in.send_keys('8.666')

        long_in = self.driver.find_element_by_xpath('//*[@id="longitude_dec"]')
        long_in.send_keys('50.666')

        send_button = self.driver.find_element_by_xpath('//*[@id="submit_btn"]')
        send_button.click()

    
    def get_gata():
        self.put_coords()
