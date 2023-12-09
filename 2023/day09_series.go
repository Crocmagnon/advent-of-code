package _023

import (
	"bufio"
	"io"
	"slices"
)

func Day09Part1(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	sum := 0
	for scanner.Scan() {
		line := lineToInts(scanner.Text())
		diffs := [][]int{line}
		for !day09AllZeros(line) {
			line = day09Difference(line)
			diffs = append(diffs, line)
		}
		lenDiffs := len(diffs)
		diffs[lenDiffs-1] = append(diffs[lenDiffs-1], 0) // add a zero to the zeros list
		for i := lenDiffs - 2; i >= 0; i-- {             //starting with the last non 0
			current := diffs[i]
			prev := diffs[i+1]
			current = append(current, current[len(current)-1]+prev[len(prev)-1])
			diffs[i] = current
		}
		sum += diffs[0][len(diffs[0])-1]
	}

	return sum, nil
}

func day09Difference(line []int) []int {
	diff := make([]int, len(line)-1)
	for i := 0; i < len(line)-1; i++ {
		diff[i] = line[i+1] - line[i]
	}
	return diff
}

func day09AllZeros(line []int) bool {
	for _, d := range line {
		if d != 0 {
			return false
		}
	}
	return true
}

func Day09Part2(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	sum := 0
	for scanner.Scan() {
		line := lineToInts(scanner.Text())
		slices.Reverse(line)
		diffs := [][]int{line}
		for !day09AllZeros(line) {
			line = day09Difference(line)
			diffs = append(diffs, line)
		}
		lenDiffs := len(diffs)
		diffs[lenDiffs-1] = append(diffs[lenDiffs-1], 0) // add a zero to the zeros list
		for i := lenDiffs - 2; i >= 0; i-- {             //starting with the last non 0
			current := diffs[i]
			prev := diffs[i+1]
			current = append(current, current[len(current)-1]+prev[len(prev)-1])
			diffs[i] = current
		}
		sum += diffs[0][len(diffs[0])-1]
	}

	return sum, nil
}
