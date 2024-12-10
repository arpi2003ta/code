def is_abecedarian(s, index=0):
    # Base case: If we've reached the last character or only one character left
    if index == len(s) - 1:
        return True
    
    # Check if the current character is less than or equal to the next one
    if s[index] <= s[index + 1]:
        # Recursive case: Check the next pair of characters
        return is_abecedarian(s, index + 1)
    else:
        # If current character is greater than the next one, it's not Abecedarian
        return False

# Test cases
print(is_abecedarian('accddmop'))  # Expected output: True
print(is_abecedarian('addccnm'))   # Expected output: False
