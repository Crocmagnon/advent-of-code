import math


def main():
    width = 25
    height = 6
    with open("inputs/day08") as f:
        data = f.readline().strip()
    layers = []
    layer_size = width * height
    position = 0
    layer = data[position : position + layer_size]
    number_of_zero_digits = math.inf
    layer_index = -1
    while layer:
        count = layer.count("0")
        if count < number_of_zero_digits:
            layer_index = int(position / layer_size)
            number_of_zero_digits = count
        layers.append(layer)
        position += layer_size
        layer = data[position : position + layer_size]

    print(layer_index)
    layer = layers[layer_index]
    print(layer.count("1") * layer.count("2"))


if __name__ == "__main__":
    main()
