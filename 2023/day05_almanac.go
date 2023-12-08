package _023

import (
	"bufio"
	"io"
	"slices"
	"strconv"
	"strings"
)

func Day05Part1(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	scanner.Scan()
	seeds := lineToInts(strings.TrimPrefix(scanner.Text(), "seeds: "))

	scanner.Scan()

	inMap := false
	var currentMap day05Map
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			for i, seed := range seeds {
				seeds[i] = currentMap.convert(seed)
			}
			inMap = false
			currentMap = nil
		} else if strings.HasSuffix(line, "map:") {
			inMap = true
		} else if inMap {
			currentMap = append(currentMap, newDay05Range(line))
		}
	}

	if inMap {
		// Convert one last time if necessary
		for i, seed := range seeds {
			seeds[i] = currentMap.convert(seed)
		}
	}

	return slices.Min(seeds), nil
}

func Day05Part2(input io.Reader) (int, error) {
	scanner := bufio.NewScanner(input)

	scanner.Scan()
	seedRanges := parseSeedRanges(lineToInts(strings.TrimPrefix(scanner.Text(), "seeds: ")))

	scanner.Scan()

	inMap := false
	var currentMap day05Map
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			var newRanges []day05SeedRange
			for _, sRange := range seedRanges {
				newRanges = append(newRanges, currentMap.convertRange(sRange)...)
			}
			seedRanges = newRanges
			inMap = false
			currentMap = nil
		} else if strings.HasSuffix(line, "map:") {
			inMap = true
		} else if inMap {
			currentMap = append(currentMap, newDay05Range(line))
		}
	}

	if inMap {
		// Convert one last time if necessary
		var newRanges []day05SeedRange
		for _, sRange := range seedRanges {
			newRanges = append(newRanges, currentMap.convertRange(sRange)...)
		}
		seedRanges = newRanges
		inMap = false
		currentMap = nil
	}

	mini := int(^uint(0) >> 1) // highest int
	for _, r := range seedRanges {
		if r.start < mini {
			mini = r.start
		}
	}

	return mini, nil
}

func parseSeedRanges(ints []int) []day05SeedRange {
	ranges := make([]day05SeedRange, len(ints)/2)
	for i := 0; i < len(ints)-1; i += 2 {
		ranges[i/2] = day05SeedRange{start: ints[i], end: ints[i] + ints[i+1]}
	}
	return ranges
}

// range is [start; end)
// start is included, end is not.
type day05SeedRange struct {
	start, end int
}

func lineToInts(line string) []int {
	values := strings.Split(line, " ")
	ints := make([]int, len(values))
	for i, value := range values {
		number, err := strconv.Atoi(value)
		if err != nil {
			panic(err)
		}
		ints[i] = number
	}
	return ints
}

type day05Range struct {
	destStart, sourceStart, length int
}

func newDay05Range(line string) day05Range {
	ints := lineToInts(line)
	return day05Range{
		destStart:   ints[0],
		sourceStart: ints[1],
		length:      ints[2],
	}
}

func (r day05Range) sourceEnd() int {
	return r.sourceStart + r.length
}

func (r day05Range) destEnd() int {
	return r.destStart + r.length
}

func (r day05Range) convert(n int) (int, bool) {
	if n >= r.sourceStart && n < r.sourceEnd() {
		return r.mustConvert(n), true
	}
	return n, false
}

func (r day05Range) mustConvert(n int) int {
	return n - r.sourceStart + r.destStart
}

func (r day05Range) convertRange(s day05SeedRange) (converted []day05SeedRange, notConverted []day05SeedRange) {
	if r.sourceStart <= s.start && s.end <= r.sourceEnd() {
		//   s-----s
		// r--------r
		return []day05SeedRange{{start: r.mustConvert(s.start), end: r.mustConvert(s.end)}}, nil
	} else if s.start < r.sourceStart && r.sourceStart <= s.end && s.end <= r.sourceEnd() {
		// s-------s
		//    r--------r
		return []day05SeedRange{{start: r.destStart, end: r.mustConvert(s.end)}}, []day05SeedRange{{start: s.start, end: r.sourceStart}}
	} else if r.sourceStart <= s.start && s.start <= r.sourceEnd() && r.sourceEnd() < s.end {
		//    s-------s
		// r--------r
		return []day05SeedRange{{start: r.mustConvert(s.start), end: r.destEnd()}}, []day05SeedRange{{start: r.sourceEnd(), end: s.end}}
	} else if s.start <= r.sourceStart && r.sourceEnd() < s.end {
		// s------------s
		//   r--------r
		return []day05SeedRange{{start: r.destStart, end: r.destEnd()}}, []day05SeedRange{{start: s.start, end: r.sourceStart}, {start: r.sourceEnd(), end: s.end}}
	} else {
		// s---s
		//        r-----r
		return nil, []day05SeedRange{s}
	}
}

type day05Map []day05Range

func (m day05Map) convert(n int) int {
	for _, dRange := range m {
		if conv, ok := dRange.convert(n); ok {
			return conv
		}
	}
	return n
}

func (m day05Map) convertRange(s day05SeedRange) []day05SeedRange {
	var converted []day05SeedRange
	toConvert := []day05SeedRange{s}
	for _, dRange := range m {
		var toConvertNext []day05SeedRange
		for _, c := range toConvert {
			var conv []day05SeedRange
			conv, toConvertNext = dRange.convertRange(c)
			converted = append(converted, conv...)
		}
		toConvert = toConvertNext
	}
	converted = append(converted, toConvert...)
	return converted
}
