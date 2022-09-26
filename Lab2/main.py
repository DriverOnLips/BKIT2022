from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from PIL import Image


def main():
    N = 17
    r = Rectangle("синего", N, N)
    c = Circle("зеленого", N)
    s = Square("красного", 5)

    print(r)
    print(c)
    print(s)

    im = Image.open("DOL1.png")
    im.show()
    print(im.format, im.size, im.mode)

if __name__ == "__main__":
    main()
