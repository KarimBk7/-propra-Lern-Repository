package main

import "fmt"

func main() {

	// A1
	//var x = [3]string{"Alice", "Bob", "Eva"}

	var evenNumbers = [6]int{2, 4, 6, 8, 10, 12}

	// A2 und A3
	evenNumbersSlice := evenNumbers[:4]

	evenNumbersSlice[0] = 9

	fmt.Println(evenNumbers, evenNumbersSlice)

	// A4
	a := make([]int, 5)

	for i := 0; i <= 4; i++ {
		a[i] = i
	}

	// A5
	primes := [5]int{1, 3, 5, 7, 11}
	var primesCopy [10]int

	copy(primesCopy[:], primes[:])
	fmt.Println(primesCopy)
	// Die Werte Landen in den ersten Plätzen des Ziel-Slices bzw. beginnen von Links es zuz befüllen

	// A9
	testSlices()

}

// A6
func AddElement(slice []int, element, at int) []int {
	n := len(slice)

	if at < 0 {
		at = 0
	} else if at > n {
		at = n
	}

	slice = append(slice, 0)
	copy(slice[at+1:], slice[at:])
	slice[at] = element
	return slice
}

// A7
func RemoveElement(slice []int, at int) []int {
	n := len(slice)

	if at < 0 {
		at = 0
	} else if at >= n {
		at = n - 1
	}

	copy(slice[at:], slice[at+1:])
	return slice[:n-1]
}

// A8
func testSlices() {
	fmt.Println("testing AddElement...")
	s := []int{1, 2, 3}
	for i := 0; i < len(s)+1; i++ {
		sc := make([]int, len(s))
		copy(sc, s)
		fmt.Println(AddElement(sc, 4, i))
	}

	fmt.Println("testing RemoveElement...")
	for i := 0; i < len(s)+1; i++ {
		sc := make([]int, len(s))
		copy(sc, s)
		fmt.Println(RemoveElement(sc, i))
	}
}
