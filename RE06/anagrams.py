def anagrams(l):
    r = []

    while len(l) > 0:
        s = l.pop()
        ss = [s]
        r.append(ss)

        cleaned_up = sorted(s.lower().replace(" ", ""))
        for other in l.copy():
            cleaned_up_other = sorted(other.lower().replace(" ", ""))
            if cleaned_up_other == cleaned_up:
                ss.append(other)
                l.remove(other)

        ss.sort()

    r.sort(key=lambda x: x[0].lower())
    return r