package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

/*
ex:
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
*/
func main() {
	s := bufio.NewScanner(os.Stdin)
	n := 0
	m := 0
	for s.Scan() {
		fields := strings.Fields(s.Text())
		bounds := strings.SplitN(fields[0], "-", 2)
		minCt, _ := strconv.Atoi(bounds[0])
		maxCt, _ := strconv.Atoi(bounds[1])
		chr := strings.TrimSuffix(fields[1], ":")
		pass := fields[2]

		ct := strings.Count(pass, chr)
		if ct >= minCt && ct <= maxCt {
			fmt.Println(s.Text())
			n++
		}

		// fmt.Println(minCt, maxCt, chr)
		// fmt.Println(pass)
		// for i := 0; i < (minCt - 1); i++ {
		// 	fmt.Print(" ")
		// }
		// fmt.Print(chr)
		// for i := 0; i < (maxCt - minCt); i++ {
		// 	fmt.Print(" ")
		// }
		// fmt.Println(chr)
		matches := 0
		if pass[minCt-1] == chr[0] {
			matches++
		}
		if pass[maxCt-1] == chr[0] {
			matches++
		}
		m += matches % 2
	}
	fmt.Println(n, m)
}
