package _023

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"os"
	"testing"
)

func TestDay07Part1(t *testing.T) {
	tests := []testCase{
		{"inputs/day07_test1", 6440},
		{"inputs/day07", 246424613},
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day07Part1))
	}
}

func TestDay07Part2(t *testing.T) {
	tests := []testCase{
		{"inputs/day07_test1", 5905},
		{"inputs/day07_test2", 5911},
		{"inputs/day07", 0}, // 247974245 is too low
	}
	for _, test := range tests {
		t.Run(test.filename, check(test, Day07Part2))
	}
	t.Run("247974245 is too low", func(t *testing.T) {
		file, err := os.Open("inputs/day07")
		require.NoError(t, err)
		got, err := Day07Part2(file)
		require.NoError(t, err)
		assert.Greater(t, got, 247974245)
	})
}

func TestDay07HandValueP1(t *testing.T) {
	tests := []struct {
		hand     string
		expected int
	}{
		{"AAAAA", d07HandFive},
		{"AAAA2", d07HandFour},
		{"AA2AA", d07HandFour},
		{"3KKK3", d07HandHouse},
		{"3KKK4", d07HandThree},
		{"KKQQT", d07HandTwoPairs},
		{"KQTQK", d07HandTwoPairs},
		{"QQ567", d07HandPair},
		{"T6862", d07HandPair},
		{"A2345", d07HandHigh},
	}
	for _, test := range tests {
		t.Run(test.hand, func(t *testing.T) {
			assert.Equal(t, test.expected, d07HandValueP1(test.hand))
		})
	}
}

func TestDay07HandValueP2(t *testing.T) {
	tests := []struct {
		hand     string
		expected int
	}{
		{"AAAAA", d07HandFive},
		{"AAJJJ", d07HandFive},
		{"AAAA2", d07HandFour},
		{"JJAJ2", d07HandFour},
		{"JKKK2", d07HandFour},
		{"QJJQ2", d07HandFour},
		{"AA2AA", d07HandFour},
		{"AJ2JA", d07HandFour},
		{"3KKK3", d07HandHouse},
		{"3KJK3", d07HandHouse},
		{"3KKK4", d07HandThree},
		{"3KKJ4", d07HandThree},
		{"KKQQT", d07HandTwoPairs},
		{"KQTQK", d07HandTwoPairs},
		{"QQ567", d07HandPair},
		{"JQ567", d07HandPair},
		{"T6862", d07HandPair},
		{"T68J2", d07HandPair},
		{"A2345", d07HandHigh},
	}
	for _, test := range tests {
		t.Run(test.hand, func(t *testing.T) {
			assert.Equal(t, test.expected, d07HandValueP2(test.hand))
		})
	}
}

func TestD07CmpHands(t *testing.T) {
	type args struct {
		a string
		b string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "five and four",
			args: args{"AAAAA", "KAAAA"},
			want: 1,
		},
		{
			name: "four and four",
			args: args{"2AAAA", "33332"},
			want: -1,
		},
		{
			name: "house and house",
			args: args{"77888", "77788"},
			want: 1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			assert.Equalf(t, tt.want, d07CmpHands(newD07Hand(tt.args.a, 0), newD07Hand(tt.args.b, 0)), "d07CmpHands(%v, %v)", tt.args.a, tt.args.b)
		})
	}
}

func TestD07CmpHandsP2(t *testing.T) {
	type args struct {
		a string
		b string
	}
	tests := []struct {
		args args
		want int
	}{
		{
			args: args{"T55J5", "KTJJT"},
			want: -1,
		},
		{
			args: args{"KTJJT", "QQQJA"},
			want: 1,
		},
		{
			args: args{"T55J5", "QQQJA"},
			want: -1,
		},
		{
			args: args{"J55T5", "JQQQA"},
			want: -1,
		},
		{
			args: args{"555T5", "JQQQA"},
			want: 1,
		},
		{
			args: args{"QQQQ2", "JKKK2"},
			want: 1,
		},
	}
	for _, tt := range tests {
		char := "<"
		if tt.want == 1 {
			char = ">"
		}
		t.Run(fmt.Sprintf("%v%v%v", tt.args.a, char, tt.args.b), func(t *testing.T) {
			assert.Equalf(t, tt.want, d07CmpHandsP2(newD07HandP2(tt.args.a, 0), newD07HandP2(tt.args.b, 0)), "d07CmpHandsP2(%v, %v)", tt.args.a, tt.args.b)
		})
	}
}
