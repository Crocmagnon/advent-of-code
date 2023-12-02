package _023

import (
	"bufio"
	"fmt"
	"io"
	"regexp"
	"strconv"
	"strings"
)

func Day02Part1(input io.Reader) (int, error) {
	const maxRed, maxGreen, maxBlue = 12, 13, 14

	scanner := bufio.NewScanner(input)
	redReg := regexp.MustCompile(`(\d+) red`)
	greenReg := regexp.MustCompile(`(\d+) green`)
	blueReg := regexp.MustCompile(`(\d+) blue`)
	sum := 0

LINES:
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ": ")
		game := strings.Split(line[1], "; ")
		for _, round := range game {
			if matches := redReg.FindStringSubmatch(round); len(matches) == 2 {
				red, err := strconv.Atoi(matches[1])
				if err != nil {
					return 0, fmt.Errorf("converting red to int: %w", err)
				}
				if red > maxRed {
					continue LINES
				}
			}
			if matches := greenReg.FindStringSubmatch(round); len(matches) == 2 {
				green, err := strconv.Atoi(matches[1])
				if err != nil {
					return 0, fmt.Errorf("converting green to int: %w", err)
				}
				if green > maxGreen {
					continue LINES
				}
			}
			if matches := blueReg.FindStringSubmatch(round); len(matches) == 2 {
				blue, err := strconv.Atoi(matches[1])
				if err != nil {
					return 0, fmt.Errorf("converting blue to int: %w", err)
				}
				if blue > maxBlue {
					continue LINES
				}
			}
		}
		gameID, err := strconv.Atoi(strings.TrimPrefix(line[0], "Game "))
		if err != nil {
			return 0, fmt.Errorf("converting game ID to int: %w", err)
		}
		sum += gameID
	}

	return sum, nil
}

func Day02Part2(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)
	redReg := regexp.MustCompile(`(\d+) red`)
	greenReg := regexp.MustCompile(`(\d+) green`)
	blueReg := regexp.MustCompile(`(\d+) blue`)
	sum := 0

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ": ")
		game := strings.Split(line[1], "; ")
		maxRed, maxGreen, maxBlue := 0, 0, 0
		for _, round := range game {
			if matches := redReg.FindStringSubmatch(round); len(matches) == 2 {
				red, err := strconv.Atoi(matches[1])
				if err != nil {
					return 0, fmt.Errorf("converting red to int: %w", err)
				}
				if red > maxRed {
					maxRed = red
				}
			}
			if matches := greenReg.FindStringSubmatch(round); len(matches) == 2 {
				green, err := strconv.Atoi(matches[1])
				if err != nil {
					return 0, fmt.Errorf("converting green to int: %w", err)
				}
				if green > maxGreen {
					maxGreen = green
				}
			}
			if matches := blueReg.FindStringSubmatch(round); len(matches) == 2 {
				blue, err := strconv.Atoi(matches[1])
				if err != nil {
					return 0, fmt.Errorf("converting blue to int: %w", err)
				}
				if blue > maxBlue {
					maxBlue = blue
				}
			}
		}
		sum += maxRed * maxGreen * maxBlue
	}

	return sum, nil
}
