from Rascunho import solar_gather_bot



bot = solar_gather_bot()

bot.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")

Latitude = '8.0113981'
Longitude = '38.8734516'

bot.put_coords()

# resp = bot.get_sun_data()

# print('r1:', resp[0])
# print('r2:', resp[1])


resp = bot.get_angle_data()
print(resp[0][0])
print(resp[0][1])
print(resp[0][2])
print(resp[0][3])

print('')
print(resp[1][0])
print(resp[1][1])
print(resp[1][2])
print(resp[1][3])

print('')
print(resp[2][0])
print(resp[2][1])
print(resp[2][2])
print(resp[2][3])


