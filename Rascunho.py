# http://www.cresesb.cepel.br/index.php?section=sundata&


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import matplotlib.pyplot as plt

   



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
        long_in.send_keys('50.8734516')

        send_button = self.driver.find_element_by_xpath('//*[@id="submit_btn"]')
        send_button.click()

    
    def get_sun_data(self):
        print('Adquirindo os dados...')
        loc_prox = self.driver.find_element_by_xpath('//*[@id="tb_sundata"]/tbody')
        list_of_lists=[]
   
        for row in range(1,4):
            list=[]
            loc_element = '//*[@id="tb_sundata"]/tbody/tr[{}]/td[{}]'.format(row, 3)
            loc_string = self.driver.find_element_by_xpath(loc_element).text
            # print('->',loc_string)
            list.append(loc_string)

            for element in range(8,23):
                data_string = '//*[@id="tb_sundata"]/tbody/tr[{}]/td[{}]'.format(row, element)
                loc_prox = self.driver.find_element_by_xpath(data_string).text
                if loc_prox != '':
                    # print(loc_prox)
                    list.append(loc_prox)
                else:
                    # print('-x-')
                    list.append('-')
            list_of_lists.append(list)
            # print (list)
    
        # head = ['Estação', 'Distância', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Média', 'Delta']

        # df = pd.DataFrame(list_of_lists, columns =head, dtype = float)

        # print(list_of_lists)
        return(list_of_lists)

    def sun_data_database(self):
        base = self.get_sun_data()
        # print('cd', base)
        head_line = ['Estação', 'Distância', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Média', 'Delta']
        df = pd.DataFrame(base, columns =head_line, dtype = float)
        # print(df)
        return(df)




    def get_angle_data(self):
        print('Adquirindo os dados...')
        loc_prox = self.driver.find_element_by_xpath('//*[@id="data_output"]/table[2]/tbody') 
        list_of_lists=[]
        
        for tables in range(2,5):
            list_of_lists = []

            for row in range(1,5):
                list = []
        
                for element in range(2,18):
                    data_string = '//*[@id="data_output"]/table[{}]/tbody/tr[{}]/td[{}]'.format(tables, row, element)
                    loc_prox = self.driver.find_element_by_xpath(data_string).text
                    if loc_prox != '':
                        # print(loc_prox)
                        list.append(loc_prox)
                    else:
                        # print('-x-')
                        list.append('-')
                list_of_lists.append(list)
            # print (list_of_lists)
        
            head = ['Ângulo', 'Inclinação', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Média', 'Delta']

            tables = pd.DataFrame(list_of_lists, columns =head, dtype = float)
                
            print(tables)

         