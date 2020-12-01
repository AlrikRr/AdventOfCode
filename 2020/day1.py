#!/usr/bin/env python3

nums = []

with open("day1/puzzle.txt",'r') as f:
    for line in f:
            nums.append(line.rstrip("\n"))

for i in range(200):
    for y in range(200):
        #print(str(nums[i])+" + "+str(nums[y]))
        res = int(nums[i]) + int(nums[y])
        #print(res)
        if res == 2020:
            print("Finish : "+str(nums[i])+" + "+str(nums[y])+" = "+str(res))
            key = int(nums[i]) * int(nums[y])
            print("Key : "+str(key))
            exit()
