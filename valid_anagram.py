def validAnagram(s: str, t: str) -> bool:

    Smap, Tmap = {}, {}
    for i in range(len(s)):
        # get(keyword, value) - returns the value of item with specified key
        Smap[s[i]] = 1 + Smap.get(s[i], 0)
        print("Character count in s:", Smap)

        Tmap[t[i]] = 1 + Tmap.get(t[i], 0)
        print("character count in t:", Tmap)

    for char in Tmap:
        if Tmap[char] != Smap.get(char, 0):
            return False
    return True


s = 'anagram'
t = 'nagaram'
print("Ans:", validAnagram(s, t))

# from collections import Counter
# s = "anagram"
# Counter(s)

# Time: O(n), we need to traverse through all characters in given string
# Space: O(1), The space utilized by the counter array is constant. Bcoz we have 26 characters in English alphabets.

