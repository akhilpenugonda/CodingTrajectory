class Solution(object):
     
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        result_list = []
        if len(digits) == 0:
            return result_list
        result_list.append("")
        for digit in digits:
            temp_list = []
            for result in result_list:
                for letter in self.get_letters(digit):
                    temp_list.append(result + letter)
            result_list = temp_list
        return result_list
    def get_letters(self, digit):
        if digit == "2":
            return "abc"
        elif digit == "3":
            return "def"
        elif digit == "4":
            return "ghi"
        elif digit == "5":
            return "jkl"
        elif digit == "6":
            return "mno"
        elif digit == "7":
            return "pqrs"
        elif digit == "8":
            return "tuv"
        elif digit == "9":
            return "wxyz"
        else:
            return ""
   