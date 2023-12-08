package _023

import (
	"testing"
)

func TestDay06Part1(t *testing.T) {
	tests := []testCase{
		{"inputs/day06_test1", 288},
		{"inputs/day06", 1660968},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day06Part1))
	}
}

func TestDay06Part2(t *testing.T) {
	tests := []testCase{
		{"inputs/day06_test1", 71503},
		{"inputs/day06", 26499773},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day06Part2))
	}
}
