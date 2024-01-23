import difflib

def print_diff(string1, string2):
    # Split strings into lines
    string1_lines = string1.splitlines()
    string2_lines = string2.splitlines()

    # Create a Differ object
    differ = difflib.Differ()

    # Calculate the difference
    diff = differ.compare(string1_lines, string2_lines)

    # Print the results
    print('\n'.join(diff))
