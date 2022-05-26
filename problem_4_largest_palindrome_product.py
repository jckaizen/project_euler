# A palindromic number reads the same both ways.
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


x = 999
y = 999
z = 0


# Assumption: It's pointless to check all the way towards 100s and slightly
# higher. So I'll just look in 900s since the chances are higher that
# the largest palindrome product is here.
for i in range(900,999):
    for j in range(900,999):
        f = i * j
        reversed_str = str(f)[::-1]
        nor_str = str(f)
        if reversed_str == nor_str and f > z:
            z = f

print(z) 
