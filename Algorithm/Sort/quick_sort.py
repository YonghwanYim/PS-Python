"""
* Author : Yonghwan Yim
* Title : Quick Sort
"""
"""
* Quick Sort is a divide-and-conquer algorithm. 
  It selects a pivot element, partitions the array into elements 
  less than or equal to the pivot and elements greater than the pivot, 
  and then recursively sorts the subarrays.

* Time Complexity:
    - Best case: O(n log n)
    - Average case: O(n log n)
    - Worst case (pivot always smallest/largest): O(n²)

* Space Complexity:
    - O(log n) for recursion stack (in-place version)
"""

# 재귀형 Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # 배열 길이 0 또는 1이면 이미 정렬 완료

    pivot = arr[len(arr) // 2]  # 가운데 값을 pivot으로 선택
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# 테스트
arr = [12, 7, 14, 9, 10, 5, 3, 8]
print(quick_sort(arr))  # [3, 5, 7, 8, 9, 10, 12, 14]