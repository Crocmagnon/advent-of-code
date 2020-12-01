def main():
    lines = []
    with open("inputs/day01") as f:
        for line in f:
            lines.append(int(line.strip()))

    stop = len(lines)
    for i, value in enumerate(lines):
        for j in range(i+1, stop):
            other = lines[j]
            addition = other + value
            if addition == 2020:
                print("result is", other * value)


if __name__ == '__main__':
    main()
