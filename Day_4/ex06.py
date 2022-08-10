def strStr(haystack, needle):
    try:
        if haystack.partition(needle):
            return haystack.index(needle)
    except ValueError:
        return -1
