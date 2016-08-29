"""Program description """

colour_codes = {"AliceBlue":"#f0f8ff","Antique White":"#faebd7", "Anrtique White1":"#ffefdb", "Aqua Marine 1":"#7fffd4","beige":"#f5f5dc"}
colour = input("Enter colour: ")
while colour not in colour_codes.keys():
    print("Colour not found")
    colour = str(input("Enter colour: "))
print (colour_codes[colour])





