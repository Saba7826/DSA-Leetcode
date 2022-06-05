def is_palindrome(self, s: str) -> bool:
    # initialise two pointer
    left = 0
    right = len(s) - 1

    # convert into lower case string
    s = s.lower()

    while left <= right:  # compare until they are equal

        if not self.is_alphanum(s[left]):        # 'a'->97 <= s[left] <= 'z'->122
            left += 1
        elif not self.is_alphanum(s[right]):        # 'a'->97 <= s[left] <= 'z'->122
            right -= 1
        elif s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False

    return True


def is_alphanum(self, char):
    return (ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9'))


s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))

# Time: O(n), n is the length of string
# Space: O(1), no extra space is used

