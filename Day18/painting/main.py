import colorgram
colors = colorgram.extract("Day18/painting/image.jpg", 25)
rgb_color=[]

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r,g,b)
    rgb_color.append(rgb)

print(rgb_color)

