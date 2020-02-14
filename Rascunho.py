# http://www.cresesb.cepel.br/index.php?section=sundata&

# Acessar, preecher e pegar os dados da localização.

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
#driver.maximize_window()
driver.minimize_window()

driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")