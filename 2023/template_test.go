package _023

import (
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"os"
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

func check(test testCase, fn solveFunc) func(t *testing.T) {
	return func(t *testing.T) {
		file, err := os.Open(test.filename)
		require.NoError(t, err)
		got, err := fn(file)
		require.NoError(t, err)
		assert.Equal(t, test.want, got)
	}
}
