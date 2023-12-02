package _023

import (
	"bufio"
	"io"
	"regexp"
	"strconv"
)

func D01Part1(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)
	sum := 0

	for scanner.Scan() {
		begValue, endValue := 0, 0
		line := scanner.Text()

		for i := 0; i < len(line); i++ {
			beg := line[i]
			if val, err := strconv.Atoi(string(beg)); err == nil && begValue == 0 {
				begValue = val
			}

			j := len(line) - 1 - i
			end := line[j]
			if val, err := strconv.Atoi(string(end)); err == nil && endValue == 0 {
				endValue = val
			}

			if begValue > 0 && endValue > 0 {
				break
			}
		}

		sum += begValue*10 + endValue
	}

	return sum, nil
}

func D01Part2(input io.Reader) (int, error) {
	reg, err := regexp.Compile(`[0-9]|one|two|three|four|five|six|seven|eight|nine`)
	if err != nil {
		return 0, err
	}

	scanner := bufio.NewScanner(input)
	sum := 0

	for scanner.Scan() {
		line := scanner.Text()
		begValue, endValue := 0, 0

		for i := 0; i < len(line); i++ {
			beg := reg.FindString(line[:i])
			if value := translate(beg); value > 0 && begValue == 0 {
				begValue = value
			}

			j := len(line) - i - 1
			end := reg.FindString(line[j:])
			if value := translate(end); value > 0 && endValue == 0 {
				endValue = value
			}

			if begValue > 0 && endValue > 0 {
				break
			}
		}

		if begValue == 0 {
			begValue = endValue
		}

		sum += begValue*10 + endValue
	}

	return sum, nil
}

func translate(digit string) int {
	switch digit {
	case "1", "one":
		return 1
	case "2", "two":
		return 2
	case "3", "three":
		return 3
	case "4", "four":
		return 4
	case "5", "five":
		return 5
	case "6", "six":
		return 6
	case "7", "seven":
		return 7
	case "8", "eight":
		return 8
	case "9", "nine":
		return 9
	default:
		return 0
	}
}
