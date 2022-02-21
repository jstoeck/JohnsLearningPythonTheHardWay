name = 'Zed A. Shaw'
age = 35  # Not a lie
height = 74  # inches
height_centimeters = height * 2.54  # converting the inches to centimeters
weight = 180  # lbs
weight_kilos = weight * 0.453592
eyes = 'Blue'
teeth = "White"
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"a.k.a. {height_centimeters} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"a.k.a {round(weight_kilos)} kilos")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teach are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it examply right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
