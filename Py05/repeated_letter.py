def repeated_letter(s):
    for i in s:
        if s.count(i) >= 2:
            return i