'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    rev = 0
    negative = x < 0
    x = abs(x)

    while x != 0:
        digit = x % 10
        x //= 10

        if rev > (INT_MAX - digit) // 10:
            return 0

        rev = rev * 10 + digit

    return -rev if negative else rev
    