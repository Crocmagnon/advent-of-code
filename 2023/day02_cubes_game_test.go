package _023

import (
	"testing"
)

func TestDay02Part1(t *testing.T) {
	tests := []testCase{
		{"inputs/day02_test1", 8},
		{"inputs/day02", 2317},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day02Part1))
	}
}

func TestDay02Part2(t *testing.T) {
	tests := []testCase{
		{"inputs/day02_test1", 2286},
		{"inputs/day02", 74804},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day02Part2))
	}
}
