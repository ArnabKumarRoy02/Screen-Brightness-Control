import screen_brightness_control as sbc

# Printing the current brightness
print(sbc.get_brightness())

# Fade the brightness from the current level to 50
sbc.fade_brightness(50)
print(sbc.get_brightness())

# Fade the brightness from 25% to 75%
sbc.fade_brightness(75, start=25)
print(sbc.get_brightness())

# Fade the brightness from the current brightness
# to 100% incrementing by 10
sbc.fade_brightness(100, increment=10)
sbc.get_brightness()
