'''
Same but using count method. Here we make a list of 26 0's and increment the count
of those letters present in s string based on their appearance. 
We do the same with t string, only that we delete them instead of adding.
If they are anagrams, the list will be full of 0's. If there's no 0, then it's an 
anagram. 
'''
def isAnagram(self, s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    
    count = [0] *26

    for i in range(len(s)):
        count[ord(s[i])-ord('a')] +=1
        count[ord(t[i])-ord('a')] -=1

    for val in count:
        if val!=0:
            return False
    return True


