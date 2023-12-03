package _023

import (
	"bufio"
	"fmt"
	"io"
	"regexp"
	"slices"
	"strconv"
)

type Day03Number struct {
	lineNo int
	start  int
	end    int
	value  int
}

type Day03Symbol struct {
	row, col int
}

func Day03Part1(input io.Reader) (int, error) {
	numberReg := regexp.MustCompile(`\d+`)
	symbolReg := regexp.MustCompile(`[^\d.]`)
	scanner := bufio.NewScanner(input)
	var symbols []Day03Symbol
	var numbers []Day03Number

	lineNo := 0
	width := 0
	for scanner.Scan() {
		line := scanner.Text()
		width = len(line)
		lineNumbers := numberReg.FindAllStringIndex(line, -1)
		lineSymbols := symbolReg.FindAllStringIndex(line, -1)
		for _, symbol := range lineSymbols {
			symbols = append(symbols, Day03Symbol{lineNo, symbol[0]})
		}
		for _, number := range lineNumbers {
			value, err := strconv.Atoi(line[number[0]:number[1]])
			if err != nil {
				return 0, fmt.Errorf("parsing number: %w", err)
			}
			numbers = append(numbers, Day03Number{lineNo, number[0], number[1], value})
		}
		lineNo++
	}

	sum := 0
	for _, number := range numbers {
		if isAdjacent(number, symbols, lineNo, width) {
			sum += number.value
		}
	}

	return sum, nil
}

func isAdjacent(number Day03Number, symbols []Day03Symbol, height, width int) bool {
	minRow := max(number.lineNo-1, 0)
	maxRow := min(number.lineNo+1, height)
	minCol := max(number.start-1, 0)
	maxCol := min(number.end, width)

	for row := minRow; row <= maxRow; row++ {
		for col := minCol; col <= maxCol; col++ {
			if slices.Contains(symbols, Day03Symbol{row, col}) {
				return true
			}
		}
	}
	return false
}

func Day03Part2(input io.Reader) (int, error) {
	numberReg := regexp.MustCompile(`\d+`)
	symbolReg := regexp.MustCompile(`\*`)
	scanner := bufio.NewScanner(input)

	var (
		potentialGears []Day03Symbol
		numbers        []Day03Number
	)

	lineNo := 0
	width := 0
	for scanner.Scan() {
		line := scanner.Text()
		width = len(line)
		lineNumbers := numberReg.FindAllStringIndex(line, -1)
		lineSymbols := symbolReg.FindAllStringIndex(line, -1)
		for _, symbol := range lineSymbols {
			potentialGears = append(potentialGears, Day03Symbol{lineNo, symbol[0]})
		}
		for _, number := range lineNumbers {
			value, err := strconv.Atoi(line[number[0]:number[1]])
			if err != nil {
				return 0, fmt.Errorf("parsing number: %w", err)
			}
			numbers = append(numbers, Day03Number{lineNo, number[0], number[1], value})
		}
		lineNo++
	}

	sum := 0
	for _, potentialGear := range potentialGears {
		sum += gearRatio(potentialGear, numbers, lineNo, width)
	}

	return sum, nil
}

func gearRatio(gear Day03Symbol, numbers []Day03Number, height int, width int) int {
	minRow := max(gear.row-1, 0)
	maxRow := min(gear.row+1, height)
	minCol := max(gear.col-1, 0)
	maxCol := min(gear.col+1, width)

	var ratio []int
	for row := minRow; row <= maxRow; row++ {
		for col := minCol; col <= maxCol; col++ {
			for _, number := range numbers {
				if row == number.lineNo && col >= number.start && col < number.end {
					ratio = append(ratio, number.value)
					col = number.end
				}
			}
		}
	}
	if len(ratio) != 2 {
		return 0
	}
	return ratio[0] * ratio[1]
}
