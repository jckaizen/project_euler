#  If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#  we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

sums = []
three_counter=3
five_counter=5

while three_counter < 1000:
    sums.append(three_counter)
    three_counter+=3

while five_counter < 1000:
    if five_counter in sums:
        five_counter += 5
        continue
    sums.append(five_counter)
    five_counter +=5
    

print(sum(sums))
