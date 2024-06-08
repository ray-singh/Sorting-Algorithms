# Sorting-Algorithms

This repository contains implementations of various sorting algorithms in Python. The sorting algorithms are generic and can be used to sort lists of any comparable elements. The provided sorting algorithms include:
- Selection Sort
- Bubble Sort
- Insertion Sort
- Hybrid Merge Sort (Merge Sort with Insertion Sort for small subarrays)
- Quicksort

Additionally, there are utility functions and a class to represent SAT scores and determine if a student's score is above the median. This was the second project I coded for my data structures and algorithms class.

## Usage
Each sorting function sorts a list in place. You can use a custom comparator and specify whether the sorting should be in descending order.

## Class 
### Score
This a class representing SAT scores. It contains two attributes - english and math - to store a student's results for each section of the SAT.

## Functions

### do_comparision
Compares two elements using a given comparator function. The comparison can be done in either ascending or descending order based on the descending flag.

Parameters:
- first (T): The first element to compare.
- second (T): The second element to compare.
- comparator (Callable[[T, T], bool]): A function that takes two elements and returns a boolean.
- descending (bool): If True, the comparison is done in descending order; otherwise, ascending.

Returns:
- bool: the result of a comparision

### selection_sort
Sorts a list in place using the selection sort algorithm.

Parameters:
- data (List[T]): The list of elements to sort.
- comparator (Callable[[T, T], bool], optional)': A function that takes two elements and returns a boolean. Defaults to a lambda function for ascending order.
- descending (bool, optional)': If True, sorts the list in descending order; otherwise, ascending. Defaults to False.

### bubble_sort
Sorts a list in place using the bubble sort algorithm.

Parameters:
- data (List[TI)': The list of elements to sort.
- comparator (Callable[[T, T], booll, optional)': A function that takes two elements and returns a boolean. Defaults to a lambda function for ascending order.
- descending (bool, optional)': If True, sorts the list in descending order; otherwise, ascending. Defaults to False.

### insertion_sort
Sorts a list in place using the insertion sort algorithm.

Parameters:
- data (List[T]): The list of elements to sort.
- comparator (Callable[[T, T], booll, optional)': A function that takes two elements and returns a boolean. Defaults to a lambda function for ascending order.
- descending (bool, optional)': If True, sorts the list in descending order; otherwise, ascending. Defaults to False.

### hybrid_merge_sort
Sorts a list in place using a hybrid merge sort algorithm. This algorithm uses merge sort but switches to insertion sort for small subarrays.

Parameters:
- data (List[T])': The list of elements to sort.
- threshold (int, optional): The size below which insertion sort is used instead of merge sort. Defaults to 12.
- comparator (Callable[[T, T1, booll, optional)': A function that takes two elements and returns a boolean. Defaults to a lambda function for ascending order.
- descending (bool, optional)': If True, sorts the list in descending order; otherwise, ascending. Defaults to False.

### quicksort
Sorts a list in place using the quicksort algorithm.

Parameters:
- data (List[TI)': The list of elements to sort.

### better_than_most
Determines if a student's SAT score is above the median in English, Math, or both.

Parameters:
- scores (List[Scorel)': List of 'Score objects representing SAT scores of all students.
- student_score (Score): 'Score object representing the SAT score of the student.

Returns:
- str: A string indicating if the student's scores are above the median in English, Math, or both.







