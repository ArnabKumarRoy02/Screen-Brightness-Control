import screen_brightness_control as sbc

# Printing the current display brightness
print(sbc.get_brightness())

# Setting the screen brightness to some level
sbc.set_brightness(50)

# Printing the current brightness after altering the values
print(sbc.get_brightness())
