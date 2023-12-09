package _023

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestDay09Part1(t *testing.T) {
	tests := []testCase{
		{"inputs/day09_test1", 114},
		{"inputs/day09", 1904165718},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day09Part1))
	}
}

func TestDay09Part2(t *testing.T) {
	tests := []testCase{
		{"inputs/day09_test1", 2},
		{"inputs/day09", 964},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day09Part2))
	}
}

func Test_day09Difference(t *testing.T) {
	tests := []struct {
		line []int
		want []int
	}{
		{[]int{0, 3, 6, 9, 12, 15}, []int{3, 3, 3, 3, 3}},
		{[]int{1, 3, 6, 10, 15, 21}, []int{2, 3, 4, 5, 6}},
	}
	for _, tt := range tests {
		t.Run(fmt.Sprint(tt.line), func(t *testing.T) {
			assert.Equalf(t, tt.want, day09Difference(tt.line), "day09Difference(%v)", tt.line)
		})
	}
}
