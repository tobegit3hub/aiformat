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


def print_diff_with_highlight(string1, string2):
    # Split strings into lines
    string1_lines = string1.splitlines()
    string2_lines = string2.splitlines()

    # Create a unified_diff
    diff = difflib.unified_diff(string1_lines, string2_lines, lineterm='')

    # Add color to the diff output
    for line in diff:
        if line.startswith('+'):
            print(f'\033[92m{line}\033[0m')  # Green text for additions
        elif line.startswith('-'):
            print(f'\033[91m{line}\033[0m')  # Red text for deletions
        elif line.startswith('@'):
            print(f'\033[94m{line}\033[0m')  # Blue text for positions
        else:
            print(line)