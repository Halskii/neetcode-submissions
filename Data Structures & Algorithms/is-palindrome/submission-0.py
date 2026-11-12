class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_string = [c.lower() for c in s if c.isalnum()]

        if(filtered_string[::-1] == filtered_string):
            return True
        return False