
#Participation Activity

def getBinaryStrings(n):
    """
    Generate all binary strings of length n.

    Args:
    n (int): The length of the binary strings to generate.

    Returns:
    List[List[int]]: A list of all binary strings of length n.
    """
    if n == 0:
        return [[]]
    else:
        # Generate all smaller strings of length n-1
        smaller_strings = getBinaryStrings(n - 1)
        # Prepend 0 and 1 to each smaller string to generate all combinations for length n
        return [[0] + s for s in smaller_strings] + [[1] + s for s in smaller_strings]

# Example usage
binary_strings = getBinaryStrings(2)
print(binary_strings)
