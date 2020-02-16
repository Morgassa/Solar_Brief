from Rascunho import solar_gather_bot


Latitude = '8.0113981'
Longitude = '38.8734516'


bot = solar_gather_bot()

bot.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")
bot.put_coords()
# # print(bot.get_gata())
# print(bot.sun_data_database())

bot.get_angle_data()
# print(bot.get_angle_data())