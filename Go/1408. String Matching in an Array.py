import "strings"
func stringMatching(words []string) []string {
    ans := []string{}
    length := len(words)
    for i:=0; i<length; i++{
        for j:=0; j<length;j++{
            if strings.Contains(words[j],words[i]) && i!=j{
                ans = append(ans, words[i]) 
                break 
            }
        }
    }

    return ans

}
