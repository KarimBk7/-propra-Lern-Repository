package main

import (
	"fmt"
)

func main() {
	testFunctions()
}

// A1
func divide(a, b float64) (result float64, err error) {

	if b == 0 {
		return 0.0, fmt.Errorf("division by zero")
	} else {
		result = a / b
		return result, nil
	}

}

// A2
func reduce(initialValue int, operation func(int, int) int, xs ...int) int {

	if len(xs) == 0 {
		return 0
	} else if len(xs) == 1 {
		return operation(initialValue, xs[0])
	}

	return reduce(operation(initialValue, xs[0]), operation, xs[1:]...)
}

// A3
func testFunctions() {
	fmt.Println(divide(5, 2))
	fmt.Println(divide(5, 0))
	fmt.Println(
		reduce(
			0,
			func(acc, arg int) int { return acc + arg*arg },
			2, 3, 5, 7, 11, 13, 17, 19,
		),
	)
}
