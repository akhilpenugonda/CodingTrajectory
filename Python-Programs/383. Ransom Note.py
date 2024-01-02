class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #create a dictionary to store the letters in magazine
        dic = {}
        for i in magazine:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        #check if the letters in ransomNote are in the dictionary
        for i in ransomNote:
            if i not in dic or dic[i] == 0:
                return False
            else:
                dic[i] -= 1
        return True
    
        

from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Count the letters in magazine and ransomNote
        magazine_counts = Counter(magazine)
        ransomNote_counts = Counter(ransomNote)

        # Check if the letters in ransomNote are in the magazine
        for letter, count in ransomNote_counts.items():
            if magazine_counts[letter] < count:
                return False

        return True
    
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Create dictionaries to count the letters in magazine and ransomNote
        magazine_counts = {}
        ransomNote_counts = {}

        for letter in magazine:
            if letter in magazine_counts:
                magazine_counts[letter] += 1
            else:
                magazine_counts[letter] = 1

        for letter in ransomNote:
            if letter in ransomNote_counts:
                ransomNote_counts[letter] += 1
            else:
                ransomNote_counts[letter] = 1

        # Check if the letters in ransomNote are in the magazine
        for letter, count in ransomNote_counts.items():
            if letter not in magazine_counts or magazine_counts[letter] < count:
                return False

        return True