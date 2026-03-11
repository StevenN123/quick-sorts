"""
Quick Sort - Divide & Conquer Algorithm Implementation
Author: Steven N
Description: In-place sorting algorithm using pivot-based partitioning
"""

import random
import time

def quick_sort(arr):
    """
    Functional version of quick sort - returns new sorted list
    
    This version creates new lists and is easier to understand but uses more memory.
    
    Args:
        arr: Input list to sort
    
    Returns:
        Sorted list (new list, original unchanged)
    """
    if len(arr) <= 1:
        return arr
    
    # Choose random pivot
    pivot = random.choice(arr)
    
    # Partition
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place version of quick sort (modifies original array)
    
    Args:
        arr: Input list to sort (will be modified)
        low: Starting index of subarray to sort
        high: Ending index of subarray to sort
    
    Returns:
        Sorted list (same reference as input)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array and get pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after pivot
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    Partition array around pivot for in-place quick sort
    
    This function rearranges elements so that all elements less than pivot
    come before it, and all greater elements come after it.
    
    Args:
        arr: Array to partition
        low: Starting index of partition range
        high: Ending index of partition range
    
    Returns:
        Final position of pivot after partitioning
    """
    # Choose random pivot to improve performance on sorted arrays
    random_index = random.randint(low, high)
    
    # Swap random pivot with last element
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


def quick_sort_detailed(arr, low=0, high=None, depth=0):
    """
    Detailed version with step-by-step output for learning
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
        depth: Recursion depth for indentation
    
    Returns:
        Sorted array
    """
    if high is None:
        high = len(arr) - 1
        print("\n" + "=" * 60)
        print("QUICK SORT - DETAILED WALKTHROUGH")
        print("=" * 60)
        print(f"Initial array: {arr}")
    
    indent = "  " * depth
    
    if low < high:
        print(f"\n{indent}Sorting subarray {arr[low:high+1]} (indices {low}-{high})")
        
        # Choose pivot
        pivot_idx = random.randint(low, high)
        pivot_value = arr[pivot_idx]
        print(f"{indent}Chosen pivot: {pivot_value} at index {pivot_idx}")
        
        # Partition
        print(f"{indent}Partitioning...")
        pivot_final = partition_detailed(arr, low, high, depth)
        
        print(f"{indent}After partition: {arr[low:high+1]}")
        print(f"{indent}Pivot {pivot_value} is now at index {pivot_final}")
        
        # Recursively sort left and right
        quick_sort_detailed(arr, low, pivot_final - 1, depth + 1)
        quick_sort_detailed(arr, pivot_final + 1, high, depth + 1)
    else:
        if low == high:
            print(f"{indent}Base case: single element [{arr[low]}]")
    
    return arr


def partition_detailed(arr, low, high, depth=0):
    """
    Detailed partition with step-by-step output
    """
    indent = "  " * depth
    
    # Choose random pivot
    random_index = random.randint(low, high)
    pivot_value = arr[random_index]
    
    print(f"{indent}  Moving pivot {pivot_value} from index {random_index} to the end")
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    pivot = arr[high]
    i = low - 1
    
    print(f"{indent}  i = {i} (index of last element < pivot)")
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            if i != j:
                print(f"{indent}  j={j}: arr[{j}]={arr[j]} ≤ pivot → swap with arr[{i}]={arr[i]}")
                arr[i], arr[j] = arr[j], arr[i]
                print(f"{indent}    Array now: {arr[low:high+1]}")
            else:
                print(f"{indent}  j={j}: arr[{j}]={arr[j]} ≤ pivot, i={i} (same index, no swap)")
        else:
            print(f"{indent}  j={j}: arr[{j}]={arr[j]} > pivot → no swap")
    
    # Place pivot
    print(f"{indent}  Placing pivot at index {i+1}")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"{indent}  Final partitioned section: {arr[low:high+1]}")
    
    return i + 1


def quick_sort_optimized(arr, low=0, high=None, threshold=10):
    """
    Optimized quick sort with insertion sort for small subarrays
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
        threshold: Size threshold for using insertion sort
    
    Returns:
        Sorted array
    """
    if high is None:
        high = len(arr) - 1
    
    # Use insertion sort for small subarrays
    if high - low < threshold:
        insertion_sort(arr, low, high)
        return arr
    
    if low < high:
        pivot_index = partition_median_of_three(arr, low, high)
        quick_sort_optimized(arr, low, pivot_index - 1, threshold)
        quick_sort_optimized(arr, pivot_index + 1, high, threshold)
    
    return arr


def partition_median_of_three(arr, low, high):
    """
    Partition using median-of-three pivot selection
    """
    mid = (low + high) // 2
    
    # Sort low, mid, high
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Use median as pivot (place at high-1)
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    pivot = arr[high - 1]
    
    i = low
    for j in range(low, high - 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high - 1] = arr[high - 1], arr[i]
    return i


def insertion_sort(arr, low, high):
    """Insertion sort for small subarrays"""
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort_iterative(arr):
    """
    Iterative version of quick sort using explicit stack
    
    Args:
        arr: Array to sort
    
    Returns:
        Sorted array
    """
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pivot_index = partition(arr, low, high)
            
            # Push larger subarray first to minimize stack size
            if pivot_index - low < high - pivot_index:
                stack.append((pivot_index + 1, high))
                stack.append((low, pivot_index - 1))
            else:
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))
    
    return arr


def three_way_partition(arr, low, high):
    """
    Three-way partition for handling duplicates (Dutch National Flag)
    
    Returns:
        Tuple of (lt, gt) indices
    """
    pivot = arr[low]
    lt = low      # arr[low+1..lt] < pivot
    gt = high     # arr[gt..high] > pivot
    i = low + 1   # arr[lt+1..i-1] = pivot
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    return lt, gt


def quick_sort_3way(arr, low=0, high=None):
    """
    Quick sort with three-way partitioning for arrays with many duplicates
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        lt, gt = three_way_partition(arr, low, high)
        quick_sort_3way(arr, low, lt - 1)
        quick_sort_3way(arr, gt + 1, high)
    
    return arr


def analyze_sorting_algorithm(arr, func, name):
    """Analyze performance of a sorting algorithm"""
    arr_copy = arr.copy()
    
    start = time.time()
    result = func(arr_copy)
    end = time.time()
    
    print(f"\n{name}:")
    print(f"  Time: {(end - start) * 1000:.4f} ms")
    print(f"  Result: {result[:10]}..." if len(result) > 10 else f"  Result: {result}")
    
    return result


def generate_test_arrays():
    """Generate test arrays for performance analysis"""
    return {
        "Random": [random.randint(1, 1000) for _ in range(100)],
        "Sorted": list(range(100)),
        "Reverse Sorted": list(range(100, 0, -1)),
        "Many Duplicates": [random.randint(1, 10) for _ in range(100)],
        "Small": [5, 2, 8, 1, 9, 3, 7, 4, 6]
    }


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("QUICK SORT ALGORITHM DEMONSTRATION")
    print("=" * 60)
    
    # Basic example
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal array: {arr}")
    
    # Functional version
    sorted_arr = quick_sort(arr)
    print(f"Sorted (functional): {sorted_arr}")
    
    # In-place version
    arr_copy = arr.copy()
    quick_sort_inplace(arr_copy)
    print(f"Sorted (in-place): {arr_copy}")
    
    # Detailed walkthrough
    print("\n" + "=" * 60)
    print("DETAILED WALKTHROUGH")
    print("=" * 60)
    test_arr = [64, 34, 25, 12, 22, 11, 90].copy()
    quick_sort_detailed(test_arr)
    
    # Test different pivot strategies
    print("\n" + "=" * 60)
    print("PIVOT STRATEGY COMPARISON")
    print("=" * 60)
    
    test_arrays = generate_test_arrays()
    
    for arr_name, test_arr in test_arrays.items():
        print(f"\n{arr_name} Array (size: {len(test_arr)}):")
        
        # Test different versions
        analyze_sorting_algorithm(test_arr, quick_sort, "Standard (functional)")
        analyze_sorting_algorithm(test_arr, quick_sort_inplace, "In-place (random pivot)")
        
        # Create wrapper for optimized version
        def opt_wrapper(a):
            return quick_sort_optimized(a.copy(), threshold=10)
        
        analyze_sorting_algorithm(test_arr, opt_wrapper, "Optimized (with insertion sort)")
    
    # Demonstrate three-way partitioning for duplicates
    print("\n" + "=" * 60)
    print("THREE-WAY PARTITIONING FOR DUPLICATES")
    print("=" * 60)
    
    dup_arr = [3, 7, 3, 1, 3, 9, 3, 2, 3, 5]
    print(f"Original with duplicates: {dup_arr}")
    
    sorted_dup = quick_sort_3way(dup_arr.copy())
    print(f"Sorted (3-way): {sorted_dup}")
    
    # Compare with standard quick sort
    std_sorted = quick_sort(dup_arr)
    print(f"Sorted (standard): {std_sorted}")
    
    print("\n" + "=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60)
    print("""
    1. Pivot selection is crucial: random pivot avoids worst-case O(n²)
    2. In-place version uses O(log n) space for recursion stack
    3. Three-way partitioning handles duplicates efficiently
    4. Hybrid with insertion sort for small subarrays improves performance
    5. Iterative version avoids recursion depth issues
    """)
