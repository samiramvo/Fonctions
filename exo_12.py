def palindrome(mot):
    if mot==mot[::-1]:
        return True
    return False

print(palindrome("ala"))
print(palindrome("villa"))