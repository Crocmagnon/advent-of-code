def compute(lst):
    result = lst.copy()

    i = 0
    while i < len(result):
        code = result[i]
        if code == 99:
            return result
        position1, position2 = result[i + 1], result[i + 2]
        item1 = result[position1]
        item2 = result[position2]
        result_index = result[i + 3]

        if code == 1:
            result[result_index] = item1 + item2
        elif code == 2:
            result[result_index] = item1 * item2
        else:
            raise ValueError(f"Something bad happened, code={code}")

        i += 4

    return result


if __name__ == "__main__":
    for i in range(100):
        for j in range(100):
            ints = list(
                map(
                    int,
                    "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,1,6,23,27,1,10,27,31,1,5,31,35,2,6,35,39,1,5,39,43,1,5,43,47,2,47,6,51,1,51,5,55,1,13,55,59,2,9,59,63,1,5,63,67,2,67,9,71,1,5,71,75,2,10,75,79,1,6,79,83,1,13,83,87,1,10,87,91,1,91,5,95,2,95,10,99,2,9,99,103,1,103,6,107,1,107,10,111,2,111,10,115,1,115,6,119,2,119,9,123,1,123,6,127,2,127,10,131,1,131,6,135,2,6,135,139,1,139,5,143,1,9,143,147,1,13,147,151,1,2,151,155,1,10,155,0,99,2,14,0,0".split(
                        ","
                    ),
                )
            )

            ints[1] = i
            ints[2] = j

            result = compute(ints)
            if result[0] == 19690720:
                print(i, j)
