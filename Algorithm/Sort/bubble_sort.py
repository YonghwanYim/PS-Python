"""
* Author : Yonghwan Yim
* Title : Bubble Sort
"""
"""
* Bubble sort repeatedly steps through the array, compares adjacent elements, 
  and swaps them if they are in the wrong order.

    - After each pass, the largest element “bubbles up” to the end of the array.
    - This process is repeated until the array is sorted.

* Time Complexity:
    - Best case (already sorted): O(n)
    - Average case: O(n²)
    - Worst case (reverse sorted): O(n²)

* Space Complexity:
    - O(1) (in-place)
"""

# O(n²) 정렬 알고리즘 중 가장 비효율적임
def bubble_sort(arr):
    for i in range(len(arr) - 1):  # 첫 pass에서 가장 큰 원소는 맨 뒤로 고정됨. 따라서 n-1번의 pass면 충분
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5,3,8,4,2]))
# [2,3,4,5,8]








