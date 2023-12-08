package _023

import (
	"regexp"
	"strconv"
	"strings"
)

var reg = regexp.MustCompile(`\s+`)

func lineToInts(line string) []int {
	line = strings.TrimSpace(line)
	values := reg.Split(line, -1)
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
