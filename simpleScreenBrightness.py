import screen_brightness_control as sbc

# Get the current screen brightness
currentBrightness = sbc.get_brightness()
print(currentBrightness)

# Get the brightness of the current display
primaryBrightness = sbc.get_brightness(display=0)
print(primaryBrightness)
