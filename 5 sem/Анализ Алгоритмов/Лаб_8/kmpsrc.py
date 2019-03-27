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
