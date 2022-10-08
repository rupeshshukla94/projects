func maxArea(H []int) int {
	i, j := 0, len(H)-1
	total := min(H[i], H[j]) * (j - i)

	for i <= j && i < len(H)-1 && j > 0 {
		// fmt.Printf("i: H[%d] = %d - j: H[%d] = %d\n", i, H[i], j, H[j])
		if H[i] < H[j] {
			i++
		} else {
			j--
		}

		cur := min(H[i], H[j]) * (j - i)
		total = max(cur, total)
	}

	return total
}

func min(i, j int) int {
	if i < j {
		return i
	} else {
		return j
	}
}

func max(i, j int) int {
	if i > j {
		return i
	} else {
		return j
	}
}
