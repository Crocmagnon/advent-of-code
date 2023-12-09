package _023

import (
	"bufio"
	"fmt"
	"io"
	"slices"
	"strconv"
	"strings"
)

const d07CardsP1 = "23456789TJQKA"
const d07CardsP2 = "J23456789TQKA"

const (
	d07HandHigh = iota
	d07HandPair
	d07HandTwoPairs
	d07HandThree
	d07HandHouse
	d07HandFour
	d07HandFive
)

type d07Hand struct {
	hand  string
	bid   int
	value int
}

func newD07Hand(hand string, bid int) d07Hand {
	return d07Hand{
		hand:  hand,
		bid:   bid,
		value: d07HandValueP1(hand),
	}
}

func Day07Part1(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	var hands []d07Hand
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")
		hand, bidS := line[0], line[1]
		bid, err := strconv.Atoi(bidS)
		if err != nil {
			return 0, fmt.Errorf("converting bid to int on line %v: %w", line, err)
		}
		hands = append(hands, newD07Hand(hand, bid))
	}

	slices.SortFunc(hands, d07CmpHands)

	sum := 0
	for i, hand := range hands {
		sum += (i + 1) * hand.bid
	}

	return sum, nil
}

func d07CmpHands(a d07Hand, b d07Hand) int {
	// cmp(a, b) should return a negative number when a < b, a positive number when
	// a > b and zero when a == b.
	if a.value < b.value {
		return -1
	}
	if a.value > b.value {
		return 1
	}

	for i := 0; i < len(a.hand); i++ {
		aValue := strings.Index(d07CardsP1, a.hand[i:i+1])
		bValue := strings.Index(d07CardsP1, b.hand[i:i+1])
		if aValue > bValue {
			return 1
		}
		if aValue < bValue {
			return -1
		}
	}

	return 0
}

func d07HandValueP1(hand string) int {
	count := make(map[rune]byte)
	var maxCount byte = 1
	var maxFor rune
	var secondMax byte = 1
	for _, c := range hand {
		v := count[c]
		v++
		if v > maxCount {
			maxCount = v
			maxFor = c
		}
		count[c] = v
	}
	for c, v := range count {
		if secondMax < v && c != maxFor {
			secondMax = v
		}
	}
	switch {
	case maxCount == 5:
		return d07HandFive
	case maxCount == 4:
		return d07HandFour
	case maxCount == 3 && secondMax == 2:
		return d07HandHouse
	case maxCount == 3 && secondMax == 1:
		return d07HandThree
	case maxCount == 2 && secondMax == 2:
		return d07HandTwoPairs
	case maxCount == 2 && secondMax == 1:
		return d07HandPair
	default:
		return d07HandHigh
	}
}

func Day07Part2(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	var hands []d07Hand
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")
		hand, bidS := line[0], line[1]
		bid, err := strconv.Atoi(bidS)
		if err != nil {
			return 0, fmt.Errorf("converting bid to int on line %v: %w", line, err)
		}
		hands = append(hands, newD07HandP2(hand, bid))
	}

	slices.SortFunc(hands, d07CmpHandsP2)

	sum := 0
	for i, hand := range hands {
		sum += (i + 1) * hand.bid
	}

	return sum, nil
}

func newD07HandP2(hand string, bid int) d07Hand {
	return d07Hand{
		hand:  hand,
		bid:   bid,
		value: d07HandValueP2(hand),
	}
}

func d07HandValueP2(hand string) int {
	count := make(map[rune]byte)
	var maxCount byte = 0
	var maxFor rune
	var secondMax byte = 0
	for _, c := range hand {
		v := count[c]
		v++
		if v > maxCount && c != 'J' {
			maxCount = v
			maxFor = c
		}
		count[c] = v
	}
	joker, ok := count['J']
	maxCount += joker
	if ok {
		delete(count, 'J')
	}
	for c, v := range count {
		if secondMax < v && c != maxFor {
			secondMax = v
		}
	}
	switch {
	case maxCount == 5:
		return d07HandFive
	case maxCount == 4:
		return d07HandFour
	case maxCount == 3 && secondMax == 2:
		return d07HandHouse
	case maxCount == 3 && secondMax == 1:
		return d07HandThree
	case maxCount == 2 && secondMax == 2:
		return d07HandTwoPairs
	case maxCount == 2 && secondMax == 1:
		return d07HandPair
	default:
		return d07HandHigh
	}
}

func d07CmpHandsP2(a d07Hand, b d07Hand) int {
	// cmp(a, b) should return a negative number when a < b, a positive number when
	// a > b and zero when a == b.
	if a.value < b.value {
		return -1
	}
	if a.value > b.value {
		return 1
	}

	for i := 0; i < len(a.hand); i++ {
		aValue := strings.Index(d07CardsP2, a.hand[i:i+1])
		bValue := strings.Index(d07CardsP2, b.hand[i:i+1])
		if aValue > bValue {
			return 1
		}
		if aValue < bValue {
			return -1
		}
	}

	return 0
}
