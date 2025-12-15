package main

import (
	"fmt"
	"math"
)

// A7
func main() {
	testMethods()
	testEmbedding()
}

// A1
type Circle struct {
	radius float64
}

// A2
func (c Circle) Circumference() float64 {
	return 2 * c.radius * math.Pi
}

func (c Circle) Area() float64 {
	return math.Pi * c.radius * c.radius
}

// A3
func testMethods() {
	c := Circle{10}
	fmt.Println("area: ", c.Area())
	fmt.Println("circumference: ", c.Circumference())
}

type Person struct {
	FirstName string
	LastName  string
	Age       int
}

// A4
type Employee struct {
	Person
	Position string
}

// A5
func (p Person) Print() {
	println(p.FirstName, p.LastName, p.Age)
}

// A6
func testEmbedding() {
	e := Employee{
		Person: Person{
			FirstName: "Mark",
			LastName:  "Mustermann",
			Age:       25,
		},
		Position: "Accountant",
	}

	e.Print()
	e.Person.Print()
}
