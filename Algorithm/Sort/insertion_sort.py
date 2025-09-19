"""
* Author : Yonghwan Yim
* Title : Insertion Sort
"""
"""
* Insertion sort builds the sorted array one element at a time.

    - Start from the second element.
    - Compare it with the elements before it.
    - Shift larger elements to the right until the correct position for the current element is found.
    - Insert the element.
    - Repeat for all elements.

* Time Complexity:
    - Best case (already sorted): O(n)
    - Average case: O(n²)
    - Worst case (reverse sorted): O(n²)

* Space Complexity:
    - O(1) (in-place, requires no extra memory)
"""

# selection ,bubble과 달리 필요할 때만 위치를 바꿈 (n² 정렬 알고리즘 중에선 가장 빠름)
def insertion_sort(arr):
    for i in range(1, len(arr)):  # 첫 index는 정렬 되어있다고 가정.
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key: # 오름차순 정렬. key보다 작은 값이 나오면 반복문 종료
            arr[j+1] = arr[j]          # 오른쪽으로 한칸씩 밀기
            j -= 1
        arr[j+1] = key         # 마지막에 key를 다시 삽입
    return arr

print(insertion_sort([5,3,8,4,2]))
# [2,3,4,5,8]
