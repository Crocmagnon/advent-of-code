def matches(num):
    two_adjacents = False
    num = str(num)
    i = 0
    while i < len(num):
        current = num[i]
        previous = ""
        before_previous = ""
        next_ = ""
        if i > 0:
            previous = num[i - 1]
        if i > 1:
            before_previous = num[i - 2]
        if i < len(num) - 1:
            next_ = num[i + 1]
        if current == previous and current != before_previous and current != next_:
            two_adjacents = True
        if current < previous:
            return 0
        i += 1

    return 1 if two_adjacents else 0


def main():
    count = 0
    for password in range(271973, 785961 + 1):
        count += matches(password)

    print(count)


if __name__ == "__main__":
    main()
