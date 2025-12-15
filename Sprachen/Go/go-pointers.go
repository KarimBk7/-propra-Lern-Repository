package main

// A1
func inc(a *int) {
	*a = *a + 1
}

func main() {
	var x = 5
	inc(nil)
	println(x)
}
