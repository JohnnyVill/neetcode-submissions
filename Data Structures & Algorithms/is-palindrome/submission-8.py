class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Approach:
        Two pointer
        create a left and right pointer.
        everytime either pointer comes across a non-alphanumeric character increment/decrement it
        at any point if the characters they are pointing to are different return false
        else if the pointer finish the while loop return true
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        left = 0
        right = len(s) - 1
    
        def validCheck(c):
            if ord(c) >= 97 and ord(c) <= 122:
                return True
            if ord(c) >= 65 and ord(c) <= 90:
                return True
            if ord(c) >= 48 and ord(c) <= 57:
                return True
            return False
        
        while left < right:
            while left < right and not validCheck(s[left]):
                left += 1
            while left < right and not validCheck(s[right]):
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
                
    
    
       
        

        
        