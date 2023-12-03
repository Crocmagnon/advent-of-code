package _023

import (
	"testing"
)

func TestDay03Part1(t *testing.T) {
	tests := []testCase{
		{"inputs/day03_test1", 4361},
		{"inputs/day03", 529618},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day03Part1))
	}
}

func TestDay03Part2(t *testing.T) {
	tests := []testCase{
		{"inputs/day03_test1", 467835},
		{"inputs/day03", 77509019},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day03Part2))
	}
}
