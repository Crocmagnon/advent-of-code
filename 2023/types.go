package _023

import "io"

type testCase struct {
	filename string
	want     int
}

type solveFunc func(reader io.Reader) (int, error)
