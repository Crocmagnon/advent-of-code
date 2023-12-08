package _023

import (
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"os"
	"testing"
)

func TestDay05Part1(t *testing.T) {
	tests := []testCase{
		{"inputs/day05_test1", 1},
		{"inputs/day05", 227653707},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day05Part1))
	}
	t.Run("inputs/day05", func(t *testing.T) {
		file, err := os.Open("inputs/day05")
		require.NoError(t, err)
		got, err := Day05Part1(file)
		require.NoError(t, err)
		assert.Less(t, got, 392296326) // 392296326 is too high
	})
}

func TestDay05Part2(t *testing.T) {
	tests := []testCase{
		{"inputs/day05_test2", 0},
		{"inputs/day05", 0},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day05Part2))
	}
}
