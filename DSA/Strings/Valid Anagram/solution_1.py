'''
To check if two strings are valid anagrams. An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
Eg: s = 'racecar' | t = 'carrace' -> Output: True
    s = "jar" | t = "jam" -> Output: False
'''

def isAnagram(s:str, t: str):
    # Using Hashmap or Dictionary

    if len(s)!=len(t):
        return False

    hash_s = {}
    hash_t = {}

    for i in range(len(s)):
        if s[i] not in hash_s:
            hash_s[s[i]] = 1
        else:
            hash_s[s[i]]+=1

        if t[i] not in hash_t:
            hash_t[t[i]] = 1
        else:
            hash_t[t[i]]+=1

    return hash_s==hash_t

        
