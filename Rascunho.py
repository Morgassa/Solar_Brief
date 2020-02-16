# http://www.cresesb.cepel.br/index.php?section=sundata&


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

   



class solar_gather_bot():
    
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        #self.latitude = latitude
        #self.longitude = longitude
        print('Inicializado...')


    def acess_site():
        print('Acessando...')
        self.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")

        assert "Python running..." in self.driver.title


    def put_coords(self):
        print('Logando...')

        lat_in = self.driver.find_element_by_xpath('//*[@id="latitude_dec"]')
        lat_in.send_keys('8.0113981')

        long_in = self.driver.find_element_by_xpath('//*[@id="longitude_dec"]')
        long_in.send_keys('34.8734516')

        send_button = self.driver.find_element_by_xpath('//*[@id="submit_btn"]')
        send_button.click()

    
    def get_gata(self):
        print('Adquirindo os dados...')
        loc_prox = self.driver.find_element_by_xpath('//*[@id="tb_sundata"]/tbody')

   
        for row in range(1,4):
            loc_element = '//*[@id="tb_sundata"]/tbody/tr[{}]/td[{}]'.format(row, 3)
            loc_string = self.driver.find_element_by_xpath(loc_element).text
            print('->',loc_string)

        #for row in range(1,4):
            for element in range(8,23):
                data_string = '//*[@id="tb_sundata"]/tbody/tr[{}]/td[{}]'.format(row, element)
                loc_prox = self.driver.find_element_by_xpath(data_string).text
                if loc_prox != '':
                    print(loc_prox)
                else:
                    print('-x-')
        

    head = ['Estação', 'Distância', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Média', 'Delta']

