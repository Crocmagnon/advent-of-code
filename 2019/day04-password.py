def matches(num):
    previous = ""
    two_adjacents = False
    for digit in str(num):
        if digit == previous:
            two_adjacents = True
        if digit < previous:
            return 0
        previous = digit

    return 1 if two_adjacents else 0


def main():
    count = 0
    for password in range(271973, 785961 + 1):
        count += matches(password)

    print(count)


if __name__ == "__main__":
    main()
