package _023

import (
	"bufio"
	"io"
	"math"
	"strings"
)

func Day06Part1(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	scanner.Scan()
	times := lineToInts(strings.TrimPrefix(scanner.Text(), "Time:"))
	scanner.Scan()
	distances := lineToInts(strings.TrimPrefix(scanner.Text(), "Distance:"))

	margin := 1

	for i := 0; i < len(times); i++ {
		x1, x2 := day06Zeros(times[i], distances[i])
		if distance(x1, times[i]) <= distances[i] {
			x1++
		}
		margin *= x2 - x1
	}

	return margin, nil
}

func day06Zeros(time, distance int) (int, int) {
	t, d := float64(time), float64(distance)
	delta := math.Sqrt(math.Pow(t, 2) - 4*d)
	return int(math.Ceil((t - delta) / 2)), int(math.Ceil((t + delta) / 2))
}

func distance(timePress, timeMax int) int {
	return timePress * (timeMax - timePress)
}

func Day06Part2(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	scanner.Scan()
	times := lineToInts(strings.ReplaceAll(strings.TrimPrefix(scanner.Text(), "Time:"), " ", ""))
	scanner.Scan()
	distances := lineToInts(strings.ReplaceAll(strings.TrimPrefix(scanner.Text(), "Distance:"), " ", ""))

	margin := 1

	for i := 0; i < len(times); i++ {
		x1, x2 := day06Zeros(times[i], distances[i])
		if distance(x1, times[i]) <= distances[i] {
			x1++
		}
		margin *= x2 - x1
	}

	return margin, nil
}
