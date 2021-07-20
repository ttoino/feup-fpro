def palindrome(s):
    count = 0

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            substr = s[i:j+1]
            if substr == substr[::-1]:
                count += 1

    return f"The string '{s}' contains {count} palindrome substrings."