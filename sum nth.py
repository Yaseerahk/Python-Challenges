#TODO: Write a function to calclate the sum of every nth number in a list 

"""
Input:
[1,2,3,4,5,6]
2
Output:
12

The sencond number in the list is 2,4 and 6.Their sum is 12 
"""
def sum_nth_numbers(numbers,n):
    total=0
    for i in range(n-1,len(numbers),n):
        total=total+numbers[i]
    return total