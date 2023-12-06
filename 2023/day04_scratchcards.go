package _023

import (
	"bufio"
	"io"
	"math"
	"regexp"
	"slices"
	"strings"
)

func Day04Part1(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)
	whitespace := regexp.MustCompile(`\s+`)
	total := 0
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ":")
		numbers := strings.Split(line[1], "|")
		winning := whitespace.Split(strings.TrimSpace(numbers[0]), -1)
		ours := whitespace.Split(strings.TrimSpace(numbers[1]), -1)
		count := 0
		for _, number := range ours {
			if slices.Contains(winning, number) {
				count++
			}
		}
		if count != 0 {
			lineRes := int(math.Pow(2, float64(count-1)))
			total += lineRes
		}
	}

	return total, nil
}

func Day04Part2(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)
	whitespace := regexp.MustCompile(`\s+`)
	var total [206]int
	index := 0
	sum := 0
	for scanner.Scan() {
		total[index]++
		sum += total[index]
		line := strings.Split(scanner.Text(), ":")
		numbers := strings.Split(line[1], "|")
		winning := whitespace.Split(strings.TrimSpace(numbers[0]), -1)
		ours := whitespace.Split(strings.TrimSpace(numbers[1]), -1)
		count := 0
		for _, number := range ours {
			if slices.Contains(winning, number) {
				count++
			}
		}
		for i := 1; i <= count; i++ {
			total[index+i] += total[index]
		}
		index++
	}

	return sum, nil
}
