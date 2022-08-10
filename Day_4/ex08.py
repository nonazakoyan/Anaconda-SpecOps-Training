def isPalindrome(s):
    s = s.lower()
    for i in s:
        if not i.isalnum():
            s = s.replace(i, '')
    if s == s[::-1]:
        return True
    return False

print(isPalindrome("A man, a plan, a canal: Panama"))