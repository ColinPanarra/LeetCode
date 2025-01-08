
func countPrefixSuffixPairs(words []string) int {
    ans := 0
    length := len(words)

    for i := 0; i < length-1; i++ {
        lenI := len(words[i])

        for j := i + 1; j < length; j++ {
            jWord := words[j]
            lenJ := len(jWord)

            if lenJ >= lenI && words[i] == jWord[:lenI] && words[i] == jWord[lenJ-lenI:] {
                ans++
            }
        }
    }

    return ans
}
