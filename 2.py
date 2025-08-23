#Write a python program to find the sum of even numbers using command line arguments.
import sys

sum_even=0
for i in range(1, len(sys.argv)):
    num=int(sys.argv[i])
    if num%2==0:
        sum_even+=num
print("Sum of even numbers : ",sum_even)