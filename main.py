from typing import TypeVar, List, Callable

T = TypeVar("T")  # represents generic type


def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Compares two elements using a given comparator function. The comparison can be done
    in either ascending or descending order based on the `descending` flag.

    Parameters:
    first (T): The first element to compare.
    second (T): The second element to compare.
    comparator (Callable[[T, T], bool]): A function that takes two elements and returns a boolean.
    descending (bool): If True, the comparison is done in descending order; otherwise, ascending.

    Returns:
    bool: The result of the comparison.
    """
    return comparator(second, first) if descending else comparator(first, second)


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list in place using the selection sort algorithm.

    Parameters:
    data (List[T]): The list of elements to sort.
    comparator (Callable[[T, T], bool], optional): A function that takes two elements and returns a boolean.
        Defaults to a lambda function for ascending order.
    descending (bool, optional): If True, sorts the list in descending order; otherwise, ascending. Defaults to False.
    """
    for i in range(len(data) - 1):
        index_smallest = i
        for j in range(i + 1, len(data)):
            if do_comparison(data[j], data[index_smallest], comparator, descending):
                index_smallest = j
        data[i], data[index_smallest] = data[index_smallest], data[i]


def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Sorts a list in place using the bubble sort algorithm.

    Parameters:
    data (List[T]): The list of elements to sort.
    comparator (Callable[[T, T], bool], optional): A function that takes two elements and returns a boolean.
        Defaults to a lambda function for ascending order.
    descending (bool, optional): If True, sorts the list in descending order; otherwise, ascending. Defaults to False.
    """
    while True:
        performed_swap = False
        for i in range(len(data) - 1):
            # Swap elements if they're in the wrong order
            if do_comparison(data[i + 1], data[i], comparator, descending):
                data[i], data[i + 1] = data[i + 1], data[i]
                performed_swap = True

        if not performed_swap:
            break


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list in place using the insertion sort algorithm.

    Parameters:
    data (List[T]): The list of elements to sort.
    comparator (Callable[[T, T], bool], optional): A function that takes two elements and returns a boolean.
        Defaults to a lambda function for ascending order.
    descending (bool, optional): If True, sorts the list in descending order; otherwise, ascending. Defaults to False.
    """
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and (comparator(key, data[j]) if not descending else comparator(data[j], key)):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Sorts a list in place using a hybrid merge sort algorithm. This algorithm uses merge sort
    but switches to insertion sort for small subarrays.

    Parameters:
    data (List[T]): The list of elements to sort.
    threshold (int, optional): The size below which insertion sort is used instead of merge sort. Defaults to 12.
    comparator (Callable[[T, T], bool], optional): A function that takes two elements and returns a boolean.
        Defaults to a lambda function for ascending order.
    descending (bool, optional): If True, sorts the list in descending order; otherwise, ascending. Defaults to False.
    """
    if len(data) <= 1:
        return

    # Defer to insertion sort if data length is less than threshold
    if len(data) <= threshold:
        insertion_sort(data, comparator=comparator, descending=descending)
    else:
        # Split the array in half
        middle = len(data) // 2
        left = data[:middle]
        right = data[middle:]

        hybrid_merge_sort(left, threshold=threshold, comparator=comparator, descending=descending)
        hybrid_merge_sort(right, threshold=threshold, comparator=comparator, descending=descending)

        # Set up indices to perform merge
        left_index, right_index, index = 0, 0, 0

        # Merge left and right subarrays together
        while left_index < len(left) and right_index < len(right):
            if do_comparison(left[left_index], right[right_index], comparator, descending):
                data[index] = left[left_index]
                left_index += 1
            else:
                data[index] = right[right_index]
                right_index += 1
            index += 1

        # Copy any remaining elements of the left subarray
        if left_index < len(left):
            data[index:] = left[left_index:]
        else:
            # Copy any remaining elements of the right subarray
            data[index:] = right[right_index:]

def quicksort(data: List[T]) -> None:
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first: int, last: int) -> None:
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


class Score:
    """
    Class that represents SAT scores
    NOTE: While it is possible to implement Python "magic methods" to prevent the need of a key function,
    this is not allowed for this application problems so students can learn how to create comparators of custom objects.
    Additionally, an individual section score can be outside the range [400, 800] and may not be a multiple of 10
    """

    __slots__ = ['english', 'math']

    def __init__(self, english: int, math: int) -> None:
        """
        Constructor for the Score class
        :param english: Score for the english portion of the exam
        :param math: Score for the math portion of the exam
        :return: None
        """
        self.english = english
        self.math = math

    def __repr__(self) -> str:
        """
        Represent the Score as a string
        :return: representation of the score
        """
        return str(self)

    def __str__(self) -> str:
        """
        Convert the Score to a string
        :return: string representation of the score
        """
        return f'<English: {self.english}, Math: {self.math}>'



def better_than_most(scores: List[Score], student_score: Score) -> str:
    """
    Determines if a student's SAT score is above the median in English, Math, or both.

    :param scores: List of Score objects representing SAT scores of all students.
    :param student_score: Score object representing the SAT score of the student.
    :return: A string indicating if the student's scores are above the median in English, Math, or both.
    """
    if not scores:  # Handle the case when there are no scores
        return 'Both'

    # Extract English and Math scores from all Score objects
    english_scores = [score.english for score in scores]
    math_scores = [score.math for score in scores]

    # Find the median of English scores
    english_median = find_median(english_scores, selection_sort)

    # Find the median of Math scores
    math_median = find_median(math_scores, selection_sort)

    # Check if student's scores are above the median in English, Math, or both
    if student_score.english > english_median and student_score.math > math_median:
        return 'Both'
    elif student_score.english > english_median:
        return 'English'
    elif student_score.math > math_median:
        return 'Math'
    else:
        return 'None'

def find_median(scores: List[int], sorting_algorithm: Callable[[List[int]], None]) -> float:
    """
    Finds the median of a list of scores using the specified sorting algorithm.

    :param scores: List of scores.
    :param sorting_algorithm: Sorting algorithm to use.
    :return: Median of the scores.
    """
    n = len(scores)
    hybrid_merge_sort(scores)

    if n % 2 == 0:  # Even number of elements
        return (scores[n // 2 - 1] + scores[n // 2]) / 2
    else:  # Odd number of elements
        return scores[n // 2]
