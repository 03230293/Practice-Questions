# Write a Python program to print the even numbers from a given list.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]
nums= [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(num):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)  # Add even numbers to a new list
    print (even_list)
    # for num in nums:
    #         if num%2==0:
    #             print(num)
even(nums)