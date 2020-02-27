# http://www.cresesb.cepel.br/index.php?section=sundata&


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import matplotlib.pyplot as plt

def str_to_float(string):
    if string.__contains__(','):
        string = float(string.replace(',', '.'))
        # print('s')
        # print(type(string))
        return(string)
    else:
        return(string)



class solar_gather_bot():
    
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        #self.latitude = latitude
        #self.longitude = longitude
        print('Inicializado...')


    def acess_site():
        
            # Acessa os site da CRESESB.
        
        print('Acessando...')
        self.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")

        assert "Python running..." in self.driver.title


    def put_coords(self):

            # Preenche os dados de latitude e longitude no site e solicita a 
            # atualização da pagina com os dados.
        
        print('Logando no site...')

        lat_in = self.driver.find_element_by_xpath('//*[@id="latitude_dec"]')
        lat_in.send_keys('8.0113981')

        long_in = self.driver.find_element_by_xpath('//*[@id="longitude_dec"]')
        long_in.send_keys('50.8734516')

        send_button = self.driver.find_element_by_xpath('//*[@id="submit_btn"]')
        send_button.click()

    
    def get_sun_data(self):
            
            # # Retorna um Dataframe com as nformação de radiação das estações e uma lista de nosmes das estações.

        data = pd.DataFrame()

        head_line = ['Estação','Distância', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        
        nomes_colunas = data['Est_Dist'] = head_line
   

        print('Adquirindo os dados solares...')
        loc_prox = self.driver.find_element_by_xpath('//*[@id="tb_sundata"]/tbody')
        list_of_lists=[]
        stations_list=[]

        for row in range(1,4):
            list=[]
            loc_element = '//*[@id="tb_sundata"]/tbody/tr[{}]/td[{}]'.format(row, 3)
            loc_string = self.driver.find_element_by_xpath(loc_element).text
            list.append(loc_string)

            for element in range(8,23):
                data_string = '//*[@id="tb_sundata"]/tbody/tr[{}]/td[{}]'.format(row, element)
                loc_prox = self.driver.find_element_by_xpath(data_string).text
                if loc_prox != '':
                    list.append(loc_prox)
                else:
                    list.append('-')
            list_of_lists.append(list)
        
        for i in list_of_lists:
            # print(i)
            string_name = '{}_{}'.format(i[0],i[1])
            stations_list.append(string_name)
            data[string_name] = i[0:14]

        return(data, stations_list)


# # # # # # # # # # #


    def get_angle_data(self):
        resp=[]

            # # Cria um dict com as informações de radiação por inclinação de cada estação.
        
        print('Adquirindo os dados de inclinação...')
        # loc_prox = self.driver.find_element_by_xpath('//*[@id="data_output"]/table[2]/tbody') 
        
        for tables in range(2,5):
     
            list_of_lists = []

            for row in range(1,5):
                list = []
        
                for element in range(2,18):
                    data_string = '//*[@id="data_output"]/table[{}]/tbody/tr[{}]/td[{}]'.format(tables, row, element)
                    loc_prox = self.driver.find_element_by_xpath(data_string).text
                    if loc_prox != '':
                        list.append(str_to_float(loc_prox))
                    else:
                        list.append('-')

                list_of_lists.append(list)

            # print(list_of_lists)
            # print(self.get_sun_data()[1])
            resp.append(list_of_lists)
            print('.')

        # print(resp)
        return(resp)

