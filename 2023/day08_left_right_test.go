package _023

import (
	"testing"
)

func TestDay08Part1(t *testing.T) {
	tests := []testCase{
		{"inputs/day08_test1", 2},
		{"inputs/day08_test2", 6},
		{"inputs/day08", 16271},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day08Part1))
	}
}

func TestDay08Part2(t *testing.T) {
	tests := []testCase{
		{"inputs/day08_test3", 6},
		{"inputs/day08", 14265111103729},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day08Part2))
	}
}
