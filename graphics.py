from Rascunho import solar_gather_bot


Latitude = '8.0113981'
Longitude = '34.8734516'


bot = solar_gather_bot()

bot.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")
bot.put_coords()
bot.get_gata()

head = ['Estação', 'Distância', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Média', 'Delta']