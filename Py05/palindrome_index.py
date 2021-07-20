def palindrome_index(s):
    if s[::-1] == s:
        return -1

    for i in range(len(s)):
        p = s[:i] + s[i+1:]
        if p[::-1] == p:
            return i

    return -1