package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func twosum(expenses []int) (int) {
	for i, a := range expenses {
		for _, b := range expenses[i+1:] {
			if a + b == 2020 {
				return a * b
			}
		}
	}
	return -1
}

func main() {
	var expenses []int
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic("couldn't deal with some input")
		}
		expenses = append(expenses, i)
	}

	fmt.Println(twosum(expenses))

	for _, a := range expenses {
		for _, b := range expenses {
			for _, c := range expenses {
				if a + b + c == 2020 {
					fmt.Println(a * b * c)
					return
				}
			}
		}
	}

}
