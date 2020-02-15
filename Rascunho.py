# http://www.cresesb.cepel.br/index.php?section=sundata&

# Acessar, preecher e pegar os dados da localização.
Latitude = 8.0113981
Longitude = 34.8734516

from selenium import webdriver

class solar_gather_bot():
    
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def acess_site():
        self.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")

        lat_in = self.driver.find_element_by_xpath('//*[@id="latitude_dec"]')
        lat_in.send_keys(Latitude)

        long_in = self.driver.find_element_by_xpath('//*[@id="longitude_dec"]')
        long_in.send_keys(Latitude)


        send_button = self.driver.find_element_by_xpath('//*[@id="submit_btn"]')
        send_button.click()

    def get_sun_data():
        


    #driver.maximize_window()
    #driver.minimize_window()

    

    #lat_in = driver.find_elemnt_by_xpath('^[[200~//*[@id="latitude_dec"]~')
    #lat_in.send_keys('amadeu@')