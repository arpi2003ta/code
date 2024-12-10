def binary_search(lst, target):
    # Initialize the left and right pointers
    left, right = 0, len(lst) - 1
    
    while left <= right:
        # Find the middle index
        mid = (left + right) // 2
        mid_value = lst[mid]
        
        # Check if the target is at the mid index
        if mid_value == target:
            return True
        # If the target is smaller, search in the left half
        elif mid_value > target:
            right = mid - 1
        # If the target is larger, search in the right half
        else:
            left = mid + 1
    
    # If the target is not found
    return False
# Accept numbers from the user to form the search list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Sort the list before performing binary search (required for binary search)
numbers.sort()

# Accept the target number to search for
target = int(input("Enter the number you want to search for: "))

# Call the binary search function
if binary_search(numbers, target):
    print(f"{target} is in the list.")
else:
    print(f"{target} is not in the list.")
