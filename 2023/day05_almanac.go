package _023

import (
	"bufio"
	"io"
	"slices"
	"strconv"
	"strings"
)

func Day05Part1(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	scanner.Scan()
	seeds := lineToInts(strings.TrimPrefix(scanner.Text(), "seeds: "))

	scanner.Scan()

	inMap := false
	var currentMap day05Map
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			for i, seed := range seeds {
				seeds[i] = currentMap.convert(seed)
			}
			inMap = false
			currentMap = nil
		} else if strings.HasSuffix(line, "map:") {
			inMap = true
		} else if inMap {
			currentMap = append(currentMap, newDay05Range(line))
		}
	}

	if inMap {
		// Convert one last time if necessary
		for i, seed := range seeds {
			seeds[i] = currentMap.convert(seed)
		}
	}

	return slices.Min(seeds), nil
}

func Day05Part2(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	for scanner.Scan() {
		line := scanner.Text()
		_ = line
	}

	return 0, nil
}

func lineToInts(line string) []int {
	values := strings.Split(line, " ")
	ints := make([]int, len(values))
	for i, value := range values {
		number, err := strconv.Atoi(value)
		if err != nil {
			panic(err)
		}
		ints[i] = number
	}
	return ints
}

type day05Range struct {
	destination, source, length int
}

func newDay05Range(line string) day05Range {
	ints := lineToInts(line)
	return day05Range{
		destination: ints[0],
		source:      ints[1],
		length:      ints[2],
	}
}

func (r day05Range) convert(n int) (int, bool) {
	if n >= r.source && n < r.source+r.length {
		return n - r.source + r.destination, true
	}
	return n, false
}

type day05Map []day05Range

func (m day05Map) convert(n int) int {
	for _, dRange := range m {
		if conv, ok := dRange.convert(n); ok {
			return conv
		}
	}
	return n
}
