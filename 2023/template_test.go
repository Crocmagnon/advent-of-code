package _023

import (
	"testing"
)

func TestDxxPart1(t *testing.T) {
	tests := []testCase{
		{"inputs/dayxx_test1", 0},
		{"inputs/dayxx", 0},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, DxxPart1))
	}
}

func TestDxxPart2(t *testing.T) {
	tests := []testCase{
		{"inputs/dayxx_test2", 0},
		{"inputs/dayxx", 0},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, DxxPart2))
	}
}
