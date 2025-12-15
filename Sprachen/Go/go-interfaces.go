package main

import "fmt"

// A1
type Dog struct{}

type Cat struct{}

type Speaker interface {
	Speak() string
}

func (c Dog) Speak() string { return "Woof!" }

func (c Cat) Speak() string { return "Meow!" }

// A2
type MyString struct {
	value        string
	lastByteRead int
}

func NewString() *MyString {
	return &MyString{
		value:        "",
		lastByteRead: 0,
	}
}

func (s MyString) String() string {
	return s.value
}

// A3
func (s MyString) Read(p []byte) (int, error) {

	if len(p) == 0 {
		return 0, nil
	}

	data := []byte(s.value)

	if s.lastByteRead >= len(data) {
		return 0, fmt.Errorf("EOF")
	}

	n := copy(p, data[s.lastByteRead:])
	s.lastByteRead += n

	if s.lastByteRead >= len(data) {
		return n, fmt.Errorf("EOF")
	}

	return n, nil
}

// A4
func (s *MyString) Write(p []byte) (int, error) {
	s.value += string(p)
	return len(p), nil
}

// A5
type HTTPError struct {
	statusCode int
}

func (e HTTPError) Error() string {
	return fmt.Sprintf("HTTPError: Status-Code %d", e.statusCode)
}

type FileError struct {
	reason string
}

func (e FileError) Error() string {
	return fmt.Sprintf("FileError: %s", e.reason)
}

// A6
func HandleSpeaker(s Speaker) {
	switch v := s.(type) {
	case Cat:
		fmt.Println("Speaker ist Cat:", v.Speak())
	case Dog:
		fmt.Println("Speaker ist Dog:", v.Speak())
	default:
		fmt.Println("Speaker ist nicht bekannt")
	}
}

func mytest() {
	// A1 Test
	speakers := []Speaker{Cat{}, Dog{}}

	for _, speaker := range speakers {
		fmt.Println(speaker.Speak())
	}

	// A3 Test
	ms := NewString()
	ms.value = "Hall"

	buf := make([]byte, 4)
	for {
		n, err := ms.Read(buf)
		fmt.Println(string(buf[:n]))
		if err != nil {
			break
		}
	}

	// A4 Test
	ms = NewString()
	n, err := ms.Write([]byte("Test: "))
	fmt.Println(n, err, ms)

	n, err = ms.Write([]byte("A4!"))
	fmt.Println(n, err, ms)
}

func main() {
	testCatsAndDogs()
	testReadWrite()
	testStringer()
	testError()
	testSpeaker()
}

func testCatsAndDogs() {
	speakers := []Speaker{Cat{}, Dog{}}

	for _, speaker := range speakers {
		fmt.Println(speaker.Speak())
	}
}

func testReadWrite() {
	s := NewString()
	fmt.Printf("created empty string: %v\n", s.value == "")
	fmt.Println("writing 'hi there'...")
	_, _ = s.Write([]byte("hi "))
	_, _ = s.Write([]byte("there"))
	fmt.Printf("'hi there' has been written: %v\n", s.value == "hi there")
}

func testStringer() {
	testString := "hello there"
	s := NewString()
	_, _ = s.Write([]byte(testString))
	fmt.Printf("string produced via .String() is correct: %v\n", fmt.Sprintf(s.String()) == testString)
}

func testError() {
	errors := []error{
		FileError{},
		HTTPError{},
		fmt.Errorf("I am a custom error"),
	}

	messages := make(map[string]bool)

	for _, err := range errors {
		messages[err.Error()] = true
	}

	fmt.Printf("every error got a unique message: %v\n", len(messages) == len(errors))
}

type Cow struct{}

func (c Cow) Speak() string {
	return "Moo!"
}

func testSpeaker() {
	speakers := []Speaker{Cat{}, Dog{}, Cow{}}

	for _, err := range speakers {
		HandleSpeaker(err)
	}
}
