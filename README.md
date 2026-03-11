# quick-sorts
A thorough execution of Quick Sort, a pivot-based partitioning in-place sorting algorithm. Several rounds of improvements, and complex visualizations are all part of this approach.

## Problem Description

The divide and conquer method of sorting an array involves selecting a pivoting element, dividing the array around it (bigger elements on the right, smaller elements on the left), and then sorting the subarrays recursively.

### How It Works
1. **Choose Pivot:** Select a pivot element (random selection helps avoid worst-case)
2. **Partition:** Rearrange array so elements smaller than pivot go left, larger go right
3. **Recursively Sort:** Apply quick sort to left and right subarrays

### Example
**Input:** `[64, 34, 25, 12, 22, 11, 90]`  
**Output:** `[11, 12, 22, 25, 34, 64, 90]`

## Algorithm Analysis

### Time Complexity
- **Best Case:** O(n log n) - Balanced partitions
- **Average Case:** O(n log n) - Random pivots
- **Worst Case:** O(n²) - Unbalanced partitions (pivot always smallest/largest)

### Space Complexity
- **Auxiliary Space:** O(log n) for recursion stack (average case)

### Properties
- ✅ **In-place sorting** - Sorts within original array
- ❌ **Unstable** - Equal elements may be reordered
- ✅ **Excellent cache locality** - Works well with hardware caches
- ✅ **Fastest in practice** - For most datasets

## Complete Python Implementation

### Approach 1: Functional Version (Simple)
```python
import random

def quick_sort(arr):
    """
    Functional version - returns new sorted list
    
    This version creates new lists and is easier to understand.
    """
    if len(arr) <= 1:
        return arr
    
    # Choose random pivot
    pivot = random.choice(arr)
    
    # Partition into three lists
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + middle + quick_sort(right)
