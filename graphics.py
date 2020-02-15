from Rascunho import solar_gather_bot


bot = solar_gather_bot()

bot.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")
bot.put_coords()


