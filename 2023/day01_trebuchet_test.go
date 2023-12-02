package _023

import (
	"testing"
)

func TestD01Part1(t *testing.T) {
	tests := []testCase{
		{"inputs/day01_test1", 142},
		{"inputs/day01", 53974},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, D01Part1))
	}
}

func TestD01Part2(t *testing.T) {
	tests := []testCase{
		{"inputs/day01_test2", 281},
		{"inputs/day01_test3", 277},
		{"inputs/day01", 52840},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, D01Part2))
	}
}
