package _023

import (
	"testing"
)

func TestDay04Part1(t *testing.T) {
	tests := []testCase{
		{"inputs/day04_test1", 13},
		{"inputs/day04", 23028},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day04Part1))
	}
}

func TestDay04Part2(t *testing.T) {
	tests := []testCase{
		{"inputs/day04_test1", 30},
		{"inputs/day04", 9236992},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day04Part2))
	}
}
