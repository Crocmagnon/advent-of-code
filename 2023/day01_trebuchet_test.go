package _023

import (
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"os"
	"testing"
)

func TestPart1(t *testing.T) {
	tests := []testCase{
		{"inputs/day01_test1", 142},
		{"inputs/day01", 53974},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Part1))
	}
}

func TestPart2(t *testing.T) {
	tests := []testCase{
		{"inputs/day01_test2", 281},
		{"inputs/day01_test3", 277},
		{"inputs/day01", 52840},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Part2))
	}
}

func check(test testCase, fn solveFunc) func(t *testing.T) {
	return func(t *testing.T) {
		file, err := os.Open(test.filename)
		require.NoError(t, err)
		got, err := fn(file)
		require.NoError(t, err)
		assert.Equal(t, test.want, got)
	}
}
