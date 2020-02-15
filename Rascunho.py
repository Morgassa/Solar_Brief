# http://www.cresesb.cepel.br/index.php?section=sundata&

# Acessar, preecher e pegar os dados da localização.

Latitude = '8.0113981'
Longitude = '34.8734516'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

   



class solar_gather_bot():
    
    def __init__(self, lat, long):
        self.driver = webdriver.Chrome('./chromedriver')
        self.latitude = lat
        self.longitude = long


    def acess_site():
        go = self.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")

        assert "Python running..." in self.driver.title


    def put_coords():
        lat_in = self.driver.find_element_by_xpath('//*[@id="latitude_dec"]')
        lat_in.send_keys(self.latitude)

        long_in = self.driver.find_element_by_xpath('//*[@id="longitude_dec"]')
        long_in.send_keys(self.longitude)

        send_button = self.driver.find_element_by_xpath('//*[@id="submit_btn"]')
        send_button.click()

    
    def get_gata():
        stations_data = self.driver.find_element_by_xpath('//*[@id="tb_sundata"]/tbody')
        # angulos_data = 
        # df = pd.read_html(stations_data)
