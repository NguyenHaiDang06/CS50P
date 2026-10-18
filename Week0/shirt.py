import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    _, in_ext = splitext(sys.argv[1].lower())
    _, out_ext = splitext(sys.argv[2].lower())

    valid_exts = [".jpg", ".jpeg", ".png"]

    if in_ext not in valid_exts or out_ext not in valid_exts:
        sys.exit("Invalid output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")


    try:

        img = Image.open(sys.argv[1])

        shirt = Image.open("shirt.png")

        img_resized = ImageOps.fit(img, shirt.size)

        img_resized.paste(shirt, shirt)

        img_resized.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
