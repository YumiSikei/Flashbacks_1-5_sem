def badCharHeuristic(string, size):
    badChar = [-1] * NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i;
    return badChar

def BMSearch(text, pattern):
    m = len(pattern)
    n = len(text)
    badChar = badCharHeuristic(pattern, m)
    s = 0
    while(s <= (n - m)):
        j = m - 1
        while (j >= 0 and pattern[j] == text[s+j]):
            j -= 1
        if (j < 0):
            print("Pattern occur at shift = {}".format(s))
            s += (m-badChar[ord(text[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(text[s+j])])
