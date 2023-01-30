def palindrome(name, left_index, right_index=-1):
    if left_index == len(name) // 2:
        return f"{name} is a palindrome"

    if name[left_index] != name[right_index]:
        return f"{name} is not a palindrome"

    return palindrome(name, left_index + 1, right_index - 1)



print(palindrome("abcba", 0))
