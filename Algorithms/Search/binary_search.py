
def binary_search(array, target_element) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is found at mid
        if array[mid] == target_element:
            return mid

        # If target is greater, ignore left half
        elif array[mid] < target_element:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # If the target is not found in the array
    return -1


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 203
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element {target} is present at index {result}.")
    else:
        print(f"Element {target} is not present in the array.")
