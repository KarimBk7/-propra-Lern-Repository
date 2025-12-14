package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	fmt.Printf("Upper limit for fizzbuzz (Enter to proceed): ")

	scanner.Scan()
	limitStr := scanner.Text()
	n, err := strconv.ParseInt(limitStr, 10, 64)

	if err == nil {
		for i := int64(1); i <= n; i++ {
			if i%3 == 0 && i%5 == 0 {
				println("fizzbuzz")
			} else if i%5 == 0 {
				println("buzz")
			} else if i%3 == 0 {
				println("fizz")
			} else {
				println(i)
			}
		}
	}
}
