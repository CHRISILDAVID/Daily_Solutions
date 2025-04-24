package main

import (
    "fmt"
    "strconv"
)

func main() {
  s := "aaaabbbbbvvcv"
  res := ""
  i := 0
  for (i < len(s)){
      j := i + 1
      for (j < len(s)) && (s[j]==s[i]){
          j += 1
      }
      //fmt.Println(j - i)
      //fmt.Println(string(s[i]) + string(j - i))
      res += string(s[i]) + strconv.Itoa(j-i)
      i = j
  }
  fmt.Println(res)
}
