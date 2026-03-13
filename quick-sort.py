"""
Quick Sort - Divide & Conquer Algorithm Implementation
Author: Steven N
Description: In-place sorting algorithm using pivot-based partitioning
"""

# Import random module to generate random pivot indices
import random
# Import time module to measure execution time for performance analysis
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
    # Base case: if array has 0 or 1 element, it's already sorted
    # This is the termination condition for our recursion
    if len(arr) <= 1:
        # Return the array as-is (already sorted)
        return arr
    
    # Choose random pivot to avoid worst-case O(n²) on sorted arrays
    # random.choice selects a random element from the list
    pivot = random.choice(arr)
    
    # Partition: create three lists based on comparison with pivot
    # List comprehension: [x for x in arr if condition]
    # This creates a new list containing all elements less than pivot
    left = [x for x in arr if x < pivot]
    
    # Create list containing all elements equal to pivot
    # This handles duplicates efficiently
    middle = [x for x in arr if x == pivot]
    
    # Create list containing all elements greater than pivot
    right = [x for x in arr if x > pivot]
    
    # Recursively sort left and right, then combine with middle
    # List sequence using + operator joins the three sorted parts
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place version of quick sort (modifies original array)
    This version is more memory-efficient as it doesn't create new lists.
    
    Args:
        arr: Input list to sort (will be modified)
        low: Starting index of subarray to sort
        high: Ending index of subarray to sort
    
    Returns:
        Sorted list (same reference as input)
    """
    # On first call, high is None, so set it to the last index
    if high is None:
        high = len(arr) - 1
    
    # Only proceed if there are at least two elements to sort
    # low < high means the subarray has at least 2 elements
    if low < high:
        # Partition the array and get the final pivot position
        # partition() rearranges elements and returns pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before the pivot
        # This sorts the left subarray from low to pivot_index-1
        quick_sort_inplace(arr, low, pivot_index - 1)
        
        # Recursively sort elements after the pivot
        # This sorts the right subarray from pivot_index+1 to high
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    # Return the sorted array (same reference as input)
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
    # random.randint returns a random integer between low and high (inclusive)
    random_index = random.randint(low, high)
    
    # Swap the randomly chosen pivot with the last element
    # This puts the pivot at the end temporarily
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    # Now the pivot value is at the high index
    pivot = arr[high]
    
    # Initialize i to track the position where elements <= pivot will go
    # i starts before the first element (low-1)
    i = low - 1
    
    # Iterate through all elements except the pivot (which is at high)
    for j in range(low, high):
        # If current element is less than or equal to pivot
        if arr[j] <= pivot:
            # Increment i to get the next position for smaller element
            i += 1
            # Swap element at i with element at j
            # This moves the smaller element to the left section
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in its correct position (right after all smaller elements)
    # i+1 is the position where the pivot belongs
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the final pivot index
    return i + 1


def quick_sort_detailed(arr, low=0, high=None, depth=0):
    """
    Detailed version with step-by-step output for learning
    This helps visualize the recursive divide-and-conquer process.
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
        depth: Recursion depth for indentation
    
    Returns:
        Sorted array
    """
    # On first call, high is None, so set it to the last index
    if high is None:
        high = len(arr) - 1
        # Print initial header and array
        print("\n" + "=" * 60)
        print("QUICK SORT - DETAILED WALKTHROUGH")
        print("=" * 60)
        print(f"Initial array: {arr}")
    
    # Create indentation based on recursion depth for visual tree
    indent = "  " * depth
    
    # Check if we have at least two elements to sort
    if low < high:
        # Print current subarray being sorted
        print(f"\n{indent}Sorting subarray {arr[low:high+1]} (indices {low}-{high})")
        
        # Choose random pivot
        pivot_idx = random.randint(low, high)
        pivot_value = arr[pivot_idx]
        print(f"{indent}Chosen pivot: {pivot_value} at index {pivot_idx}")
        
        # Partition the array
        print(f"{indent}Partitioning...")
        pivot_final = partition_detailed(arr, low, high, depth)
        
        # Print results after partitioning
        print(f"{indent}After partition: {arr[low:high+1]}")
        print(f"{indent}Pivot {pivot_value} is now at index {pivot_final}")
        
        # Recursively sort left subarray (elements before pivot)
        quick_sort_detailed(arr, low, pivot_final - 1, depth + 1)
        
        # Recursively sort right subarray (elements after pivot)
        quick_sort_detailed(arr, pivot_final + 1, high, depth + 1)
    else:
        # Base case: single element (low == high) or empty subarray
        if low == high:
            print(f"{indent}Base case: single element [{arr[low]}]")
    
    # Return the sorted array
    return arr


def partition_detailed(arr, low, high, depth=0):
    """
    Detailed partition with step-by-step output for learning
    Shows each comparison and swap during the partition process.
    """
    # Create indentation based on depth
    indent = "  " * depth
    
    # Choose random pivot
    random_index = random.randint(low, high)
    pivot_value = arr[random_index]
    
    # Print pivot selection and movement
    print(f"{indent}  Moving pivot {pivot_value} from index {random_index} to the end")
    # Swap pivot with last element
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    # Now pivot is at the end
    pivot = arr[high]
    
    # Initialize i to track boundary of elements <= pivot
    i = low - 1
    
    print(f"{indent}  i = {i} (index of last element < pivot)")
    
    # Iterate through all elements except the pivot
    for j in range(low, high):
        # If current element is less than or equal to pivot
        if arr[j] <= pivot:
            # Move boundary and prepare for swap
            i += 1
            # Check if we need to swap (different indices)
            if i != j:
                print(f"{indent}  j={j}: arr[{j}]={arr[j]} ≤ pivot → swap with arr[{i}]={arr[i]}")
                # Swap elements at i and j
                arr[i], arr[j] = arr[j], arr[i]
                # Show array after swap
                print(f"{indent}    Array now: {arr[low:high+1]}")
            else:
                # i and j are same, no swap needed
                print(f"{indent}  j={j}: arr[{j}]={arr[j]} ≤ pivot, i={i} (same index, no swap)")
        else:
            # Element is greater than pivot, no swap
            print(f"{indent}  j={j}: arr[{j}]={arr[j]} > pivot → no swap")
    
    # Place pivot in its final position
    print(f"{indent}  Placing pivot at index {i+1}")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"{indent}  Final partitioned section: {arr[low:high+1]}")
    
    # Return final pivot index
    return i + 1


def quick_sort_optimized(arr, low=0, high=None, threshold=10):
    """
    Optimized quick sort with insertion sort for small subarrays
    This hybrid approach improves performance by avoiding recursive calls for tiny arrays.
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
        threshold: Size threshold for using insertion sort
    
    Returns:
        Sorted array
    """
    # On first call, set high to last index
    if high is None:
        high = len(arr) - 1
    
    # Use insertion sort for small subarrays (size < threshold)
    # This avoids recursion overhead for tiny arrays
    if high - low < threshold:
        insertion_sort(arr, low, high)
        return arr
    
    # For larger arrays, use quick sort
    if low < high:
        # Partition using median-of-three pivot selection
        pivot_index = partition_median_of_three(arr, low, high)
        
        # Recursively sort left subarray
        quick_sort_optimized(arr, low, pivot_index - 1, threshold)
        
        # Recursively sort right subarray
        quick_sort_optimized(arr, pivot_index + 1, high, threshold)
    
    # Return sorted array
    return arr


def partition_median_of_three(arr, low, high):
    """
    Partition using median-of-three pivot selection
    This chooses a better pivot by taking the median of first, middle, and last elements.
    """
    # Calculate middle index
    mid = (low + high) // 2
    
    # Sort low, mid, and high to find median
    # If mid is less than low, swap them
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    
    # If high is less than low, swap them
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    
    # If high is less than mid, swap them
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Now arr[mid] is the median value
    # Move median to high-1 (second last position)
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    
    # Use the median as pivot
    pivot = arr[high - 1]
    
    # Initialize i to track boundary of elements <= pivot
    i = low
    
    # Partition using elements except the last two (low and high-1)
    for j in range(low, high - 1):
        # If current element is less than or equal to pivot
        if arr[j] <= pivot:
            # Swap with element at boundary
            arr[i], arr[j] = arr[j], arr[i]
            # Move boundary forward
            i += 1
    
    # Place pivot in its final position
    arr[i], arr[high - 1] = arr[high - 1], arr[i]
    
    # Return final pivot index
    return i


def insertion_sort(arr, low, high):
    """Insertion sort for small subarrays - efficient for nearly-sorted arrays"""
    # Iterate through each element starting from low+1
    for i in range(low + 1, high + 1):
        # Store current value as key
        key = arr[i]
        
        # Initialize j to compare with previous elements
        j = i - 1
        
        # Shift elements greater than key to the right
        # Continue while j >= low and element at j is greater than key
        while j >= low and arr[j] > key:
            # Move element one position right
            arr[j + 1] = arr[j]
            # Move j left to check next element
            j -= 1
        
        # Place key in its correct position
        arr[j + 1] = key


def quick_sort_iterative(arr):
    """
    Iterative version of quick sort using explicit stack
    This avoids recursion depth issues for very large arrays.
    
    Args:
        arr: Array to sort
    
    Returns:
        Sorted array
    """
    # Initialize stack with the entire array range (low, high)
    stack = [(0, len(arr) - 1)]
    
    # Continue while there are subarrays to process
    while stack:
        # Pop the next subarray range from stack
        low, high = stack.pop()
        
        # If subarray has at least two elements
        if low < high:
            # Partition the subarray and get pivot index
            pivot_index = partition(arr, low, high)
            
            # Push subarrays onto stack
            # To minimize stack size, push larger subarray first
            # Compare sizes of left and right subarrays
            if pivot_index - low < high - pivot_index:
                # Right subarray is larger, push it first
                stack.append((pivot_index + 1, high))
                # Then push left subarray
                stack.append((low, pivot_index - 1))
            else:
                # Left subarray is larger or equal, push it first
                stack.append((low, pivot_index - 1))
                # Then push right subarray
                stack.append((pivot_index + 1, high))
    
    # Return sorted array
    return arr


def three_way_partition(arr, low, high):
    """
    Three-way partition for handling duplicates (Dutch National Flag)
    This partitions the array into three sections: < pivot, = pivot, > pivot
    
    Returns:
        Tuple of (lt, gt) indices where:
        - lt is the last index of < pivot section
        - gt is the first index of > pivot section
    """
    # Choose first element as pivot
    pivot = arr[low]
    
    # Initialize three pointers:
    # lt (less than) - tracks boundary of elements < pivot
    lt = low
    
    # gt (greater than) - tracks boundary of elements > pivot
    gt = high
    
    # i - current element being examined
    i = low + 1
    
    # Continue until we've processed all elements
    while i <= gt:
        # If current element is less than pivot
        if arr[i] < pivot:
            # Swap with element at lt boundary
            arr[lt], arr[i] = arr[i], arr[lt]
            # Move lt boundary right
            lt += 1
            # Move to next element
            i += 1
        
        # If current element is greater than pivot
        elif arr[i] > pivot:
            # Swap with element at gt boundary
            arr[i], arr[gt] = arr[gt], arr[i]
            # Move gt boundary left
            gt -= 1
            # Don't increment i - need to check swapped element
        
        # If current element equals pivot
        else:
            # Just move to next element
            i += 1
    
    # Return boundaries for < pivot and > pivot sections
    return lt, gt


def quick_sort_3way(arr, low=0, high=None):
    """
    Quick sort with three-way partitioning for arrays with many duplicates
    This version handles duplicates efficiently by grouping them together.
    """
    # On first call, set high to last index
    if high is None:
        high = len(arr) - 1
    
    # Check if we have at least two elements
    if low < high:
        # Perform three-way partition
        lt, gt = three_way_partition(arr, low, high)
        
        # Repeatedly sort elements less than pivot
        quick_sort_3way(arr, low, lt - 1)
        
        # Repeatedly sort elements greater than pivot
        quick_sort_3way(arr, gt + 1, high)
    
    # Return sorted array
    return arr


def analyze_sorting_algorithm(arr, func, name):
    """Analyze performance of a sorting algorithm"""
    # Create a copy to avoid changing the original array
    arr_copy = arr.copy()
    
    # Record start time
    start = time.time()
    
    # Running the sorting function
    result = func(arr_copy)
    
    # Record end time
    end = time.time()
    
    # Print results
    print(f"\n{name}:")
    # Calculate time in milliseconds (multiply by 1000)
    print(f"  Time: {(end - start) * 1000:.4f} ms")
    
    # Print first 10 elements of result (or full if smaller)
    if len(result) > 10:
        print(f"  Result: {result[:10]}...")
    else:
        print(f"  Result: {result}")
    
    # Return sorted result
    return result


def generate_test_arrays():
    """Generate test arrays for performance analysis"""
    # Return dictionary of different array types for comprehensive testing
    return {
        # Random array: typical case
        "Random": [random.randint(1, 1000) for _ in range(100)],
        
        # Already sorted: tests pivot selection (worst case for naive)
        "Sorted": list(range(100)),
        
        # Reverse sorted: also worst case for naive
        "Reverse Sorted": list(range(100, 0, -1)),
        
        # Many duplicates: tests three-way partitioning
        "Many Duplicates": [random.randint(1, 10) for _ in range(100)],
        
        # Small array: for demonstration
        "Small": [5, 2, 8, 1, 9, 3, 7, 4, 6]
    }


# Example usage - only runs if script is executed directly
if __name__ == "__main__":
    # Print main header
    print("=" * 60)
    print("QUICK SORT ALGORITHM DEMONSTRATION")
    print("=" * 60)
    
    # Basic example array for demonstration
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal array: {arr}")
    
    # Test functional version (returns new sorted array)
    sorted_arr = quick_sort(arr)
    print(f"Sorted (functional): {sorted_arr}")
    
    # Test in-place version (changes original)
    arr_copy = arr.copy()
    quick_sort_inplace(arr_copy)
    print(f"Sorted (in-place): {arr_copy}")
    
    # Run detailed walkthrough for learning
    print("\n" + "=" * 60)
    print("DETAILED WALKTHROUGH")
    print("=" * 60)
    test_arr = [64, 34, 25, 12, 22, 11, 90].copy()
    quick_sort_detailed(test_arr)
    
    # Test different pivot strategies
    print("\n" + "=" * 60)
    print("PIVOT STRATEGY COMPARISON")
    print("=" * 60)
    
    # Generate test arrays
    test_arrays = generate_test_arrays()
    
    # Test each array type with different algorithms
    for arr_name, test_arr in test_arrays.items():
        print(f"\n{arr_name} Array (size: {len(test_arr)}):")
        
        # Test standard functional version
        analyze_sorting_algorithm(test_arr, quick_sort, "Standard (functional)")
        
        # Test in-place version with random pivot
        analyze_sorting_algorithm(test_arr, quick_sort_inplace, "In-place (random pivot)")
        
        # Create wrapper for improved version
        def opt_wrapper(a):
            # Call optimized version with threshold of 10
            return quick_sort_optimized(a.copy(), threshold=10)
        
        # Test optimized version
        analyze_sorting_algorithm(test_arr, opt_wrapper, "Optimized (with insertion sort)")
    
    # Demonstrate three way division/partition for duplicates
    print("\n" + "=" * 60)
    print("THREE-WAY PARTITIONING FOR DUPLICATES")
    print("=" * 60)
    
    # Array with many duplicates
    dup_arr = [3, 7, 3, 1, 3, 9, 3, 2, 3, 5]
    print(f"Original with duplicates: {dup_arr}")
    
    # Sort with three-way partitioning
    sorted_dup = quick_sort_3way(dup_arr.copy())
    print(f"Sorted (3-way): {sorted_dup}")
    
    # Compare with standard quick sort
    std_sorted = quick_sort(dup_arr)
    print(f"Sorted (standard): {std_sorted}")
    
    # Print key insights about quick sort
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
