package _023

import (
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"os"
	"testing"
)

type testCase struct {
	filename string
	want     int
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
