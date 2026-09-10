import pyfiglet
import random
import sys

figlet = pyfiglet.Figlet()
fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font = sys.argv[2]
else:
    sys.exit("Invalid usage")

if font not in fonts:
    sys.exit("Invalid usage")

text = input("Input: ")

figlet.setFont(font=font)
print(figlet.renderText(text))

