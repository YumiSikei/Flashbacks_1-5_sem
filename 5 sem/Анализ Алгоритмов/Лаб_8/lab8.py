NO_OF_CHARS = 256

# Knuth - Morris - Pratt algorithm
def KMPSearch(pattern, text):
    M = len(pattern)
    N = len(text)
    longestPrefixSuffix = [0]*M
    j = 0
    computeLPSArray(pattern, M, longestPrefixSuffix)
    i = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            print("Found pattern at index " + str(i - j))
            j = longestPrefixSuffix[j-1]
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = longestPrefixSuffix[j-1]
            else:
                i += 1

def computeLPSArray(pattern, M, longestPrefixSuffix):
    len = 0
    longestPrefixSuffix[0]
    i = 1
    while i < M:
        if pattern[i]== pattern[len]:
            len += 1
            longestPrefixSuffix[i] = len
            i += 1
        else:
            if (len != 0):
                len = longestPrefixSuffix[len-1]
            else:
                longestPrefixSuffix[i] = 0
                i += 1

# Boyer - Moore algorithm
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

if __name__ == '__main__':
    text1 = "ABABDABACDABABCABAB"
    pattern1 = "ABABCABAB"
    KMPSearch(pattern1, text1)
    text2 = "ABAAABCD"
    pattern2 = "ABC"
    BMSearch(text2, pattern2)
