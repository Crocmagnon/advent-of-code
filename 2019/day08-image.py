from typing import List

WIDTH = 25
HEIGHT = 6
LAYER_SIZE = WIDTH * HEIGHT

WHITE = "1"
BLACK = "0"
TRANSPARENT = "2"


def find_pixel(layers: List[str], index: int) -> str:
    for layer in layers:
        pixel = layer[index]
        if pixel in [WHITE, BLACK]:
            return pixel
    return TRANSPARENT


def display_image(image: str) -> None:
    for i, pixel in enumerate(image):
        if i % WIDTH == 0:
            print()
        character = " "
        if pixel == WHITE:
            character = "█"
        print(character, end="")


def main():
    with open("inputs/day08") as f:
        data = f.readline().strip()
    layers = []
    position = 0
    layer = data[position : position + LAYER_SIZE]
    while layer:
        layers.append(layer)
        position += LAYER_SIZE
        layer = data[position : position + LAYER_SIZE]

    result_image = ""
    for index in range(LAYER_SIZE):
        result_image += find_pixel(layers, index)

    display_image(result_image)


if __name__ == "__main__":
    main()
