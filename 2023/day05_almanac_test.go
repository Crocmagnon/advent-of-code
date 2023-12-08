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
		{"inputs/day05_test2", 46},
		{"inputs/day05", 78775051},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day05Part2))
	}
}

func TestDay05Ranges(t *testing.T) {
	tests := []struct {
		name      string
		dRange    day05Range
		seedRange day05SeedRange
		expected  []day05SeedRange
	}{
		{
			"seed included in range",
			day05Range{0, 5, 5},
			day05SeedRange{6, 8},
			[]day05SeedRange{{1, 3}},
		},
		{
			"range included in seed",
			day05Range{0, 10, 2},
			day05SeedRange{9, 13},
			[]day05SeedRange{{0, 2}, {9, 10}, {12, 13}},
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := day05Map{test.dRange}.convertRange(test.seedRange)
			assert.Equal(t, test.expected, got)
		})
	}
}
