def swap_first_last(lst):
    # Use unpacking and slicing to swap first and last elements
    lst[0], *middle, lst[-1] = lst[-1], *lst[1:-1], lst[0]
    return lst

# Example usage:
my_list = [10, 20, 30, 40, 50]
swapped_list = swap_first_last(my_list)
print(swapped_list)
