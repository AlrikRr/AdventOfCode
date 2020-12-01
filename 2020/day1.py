#!/usr/bin/env python3

# Array used to store the numbers
nums = []

with open("day1/puzzle.txt",'r') as f:
    for line in f:
            # Put each numbers into the nums array, don't forget rstrip ! 
            nums.append(line.rstrip("\n"))

# So here I decided to use the simple way.
# There are 200 numbers, I get the sum of the 1st element of x with the 1st element of y
# Then the Sum of the 1st element of x and the 2nd element of y ......
# Until a result returns 2020. Not the fastest way but it works !
for i in range(200):
    for y in range(200):
        res = int(nums[i]) + int(nums[y])
        if res == 2020:
            print("Finish : "+str(nums[i])+" + "+str(nums[y])+" = "+str(res))
            key = int(nums[i]) * int(nums[y])
            print("Key : "+str(key))
            exit()
