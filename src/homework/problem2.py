# Write a program that generates a list of 20 random numbers between 1 and 100. When generating
# random number use random seed as 18.
# (a) Print the list.
# (b) Print the sorted list (sort list in the descending order)
# (c) Print the average of the elements in the list.
# (d) Print how many even numbers are in the list.
# (e) Print the largest and smallest values in the list.
# (f) Print the second largest and second smallest entries in the list
# Since we use the same random seed number, your output should be exactly like this:

import random
random.seed(18)

def problem2():        
    numbers = [random.randint(1, 100) for rnd in range(20)]
    
    print("Original list:", numbers)
    
    sorted_numbers = sorted(numbers, reverse=True)
    print("Sorted list (descending):", sorted_numbers)
    
    average = sum(numbers) / len(numbers)
    print("Average of the elements:", average)
    
    even_count = sum(1 for num in numbers if num % 2 == 0)
    print("Count of even numbers:", even_count)
    
    largest = max(numbers)
    smallest = min(numbers)
    print("Largest value:", largest)
    print("Smallest value:", smallest)
    
    second_largest = sorted(set(numbers), reverse=True)[1]
    second_smallest = sorted(set(numbers))[1]
    print("Second largest value:", second_largest)
    print("Second smallest value:", second_smallest)

problem2()