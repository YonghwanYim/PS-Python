"""
* Author : Yonghwan Yim
* Title : Selection Sort
"""
"""
* Selection sort repeatedly finds the minimum element from the unsorted part
  of the array and swaps it with the first unsorted element.
  
    - First pass: put the smallest element at index 0.
    - Second pass: put the second smallest element at index 1.
    - Continue until the array is sorted.
  
* Time Complexity:
    - Best case: O(n²)
    - Average case: O(n²)
    - Worst case: O(n²)
  
* Space Complexity:
    - O(1) (in-place, requires no extra memory)
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i              # 처음에는 index 0을 min_idx로 초기화
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:   # 작은 값을 갖는 index를 min_idx에 저장
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]   # 비교를 마치면 min_idx를 스왑 후 다음 반복 시작
    return arr

print(selection_sort([5,3,8,4,2]))
# [2,3,4,5,8]