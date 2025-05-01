def isPalindrome(strr):
    inpString=str(strr)
    revString=inpString[::-1]
    if inpString==revString:
        return "The given string is palindrome"
    else:
        return "The given string is not a palindrome"


print(isPalindrome(123))