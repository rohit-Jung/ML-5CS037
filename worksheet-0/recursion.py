"""
This module is used to practice recursion

Recursion is a method to solve problems where 
similar logic is repeated. Its has two main parts:

1. Base case: The base case is the stopping condition of the recursion.
2. Recursive case: The recursive case is the logic that is repeated.(calling itself)
"""

from dataset import directory_structure, example_nested_list

def sum_nested_list(nested_list):
    """ "
    Returns the sum of the nested list
    """
    total_sum = 0
    for element in nested_list:
        if isinstance(element, list):
            total_sum += sum_nested_list(element)
        else:
            total_sum += element
    return total_sum


def generate_permutations(string):
    """Generates all the permutations for the given string

    Args:
        string (str): The string to be permuted
    """
    # base case
    if len(string) == 1:
        return [string]

    # recursive case
    permutations = []
    for i, char in enumerate(string):
        remaining_chars = string[:i] + string[i + 1 :]
        remaining_perm = generate_permutations(remaining_chars)
        for perm in remaining_perm:
            print(perm + char + remaining_chars)
            permutations.append(char + perm)

    return permutations


def calculate_directory_size(directory: dict) -> int:
    """calculates the size of the directory

    Args:
        directory (dict): the dict. of directory

    Returns:
        int: total size of directory
    """
    # base case
    length = 0
    if len(directory) == 0:
        return 0

    # recursive case
    for _, value in directory.items():
        if isinstance(value, dict):
            length += calculate_directory_size(value)
        else:
            length += value

    return length


def main():
    """The main function to be executed
    """
    print(generate_permutations("bc"))
    print("Size of directory", calculate_directory_size(directory_structure))
    print("\n")
    print("Sum of nested list", sum_nested_list(example_nested_list))

# only runs the main function if it is the main file executed
if __name__ == "__main__":
    main()
