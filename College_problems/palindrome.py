def palindrome(n):
    i = 0
    j = len(n)-1
    while i <= j:
        if n[i] == n[j]:
            i += 1
            j -= 1
        else:
            return False
    return True