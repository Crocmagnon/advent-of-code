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
	scanner.Scan()
	leftRight := scanner.Text()

	scanner.Scan() // skip blank line

	nodes := make(map[string][2]string)
	var positions []string

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " = ") // AAA = (BBB, CCC)
		node := line[0]
		rest := strings.Split(strings.NewReplacer("(", "", " ", "", ")", "").Replace(line[1]), ",")
		nodes[node] = [2]string{rest[0], rest[1]}
		if strings.HasSuffix(node, "A") {
			positions = append(positions, node)
		}
	}

	step := 0
	reachedZ := make([]int, len(positions))
	for !allFinished(positions, reachedZ, step) {
		for i := 0; i < len(positions); i++ {
			positions[i] = move(positions[i], step, leftRight, nodes)
		}
		step++
	}

	return LCM(reachedZ[0], reachedZ[1], reachedZ[2:]...), nil
}

func allFinished(positions []string, reachedZ []int, step int) bool {
	for i, pos := range positions {
		if strings.HasSuffix(pos, "Z") && reachedZ[i] == 0 {
			reachedZ[i] = step
		}
	}
	for _, z := range reachedZ {
		if z == 0 {
			return false
		}
	}
	return true
}

// GCD and LCM from https://siongui.github.io/2017/06/03/go-find-lcm-by-gcd/
func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

func LCM(a, b int, integers ...int) int {
	result := a * b / GCD(a, b)

	for i := 0; i < len(integers); i++ {
		result = LCM(result, integers[i])
	}

	return result
}
