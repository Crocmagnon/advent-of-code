package _023

import (
	"bufio"
	"io"
	"strings"
)

func Day08Part1(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)
	scanner.Scan()
	leftRight := scanner.Text()

	scanner.Scan() // skip blank line

	nodes := make(map[string][2]string)

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " = ") // AAA = (BBB, CCC)
		node := line[0]
		rest := strings.Split(strings.NewReplacer("(", "", " ", "", ")", "").Replace(line[1]), ",")
		nodes[node] = [2]string{rest[0], rest[1]}
	}

	current := "AAA"
	step := 0
	for current != "ZZZ" {
		current = move(current, step, leftRight, nodes)
		step++
	}

	return step, nil
}

func move(current string, step int, leftRight string, nodes map[string][2]string) string {
	instruction := leftRight[step%len(leftRight)]
	paths := nodes[current]
	if instruction == 'L' {
		return paths[0]
	} else {
		return paths[1]
	}
}

func Day08Part2(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	for scanner.Scan() {
		line := scanner.Text()
		_ = line
	}

	return 0, nil
}
