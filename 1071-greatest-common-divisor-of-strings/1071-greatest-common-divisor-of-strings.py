class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Check if both strings can be built from a common base
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Find GCD of the lengths
        gcd_len = math.gcd(len(str1), len(str2))
        
        # Step 3: Return the prefix of str1 of length gcd_len
        return str1[:gcd_len]