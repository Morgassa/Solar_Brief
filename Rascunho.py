# http://www.cresesb.cepel.br/index.php?section=sundata&

# Acessar, preecher e pegar os dados da localização.
# Latitude = 8.0113981
# Longitude = 34.8734516

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
#driver.maximize_window()
driver.minimize_window()

driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")