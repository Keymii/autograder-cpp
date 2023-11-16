from difflib import unified_diff
from ansi_colors import TEXT_FOUND_COLOR, TEXT_EXPECTED_COLOR, colorize_line
def find_and_print_differences(actual_output, expected_output):
    lines_actual = actual_output.splitlines()
    lines_expected = expected_output.splitlines()

    max_len = max(len(lines_actual), len(lines_expected))
    
    print("Line   | Actual Output        | Expected Output")
    print("-------|----------------------|---------------------")

    for i, (line_actual, line_expected) in enumerate(zip(lines_actual + [''] * (max_len - len(lines_actual)), lines_expected + [''] * (max_len - len(lines_expected))), 1):
        if line_actual != line_expected:
            line_actual_colored = colorize_line(line_actual, TEXT_FOUND_COLOR) 
            line_expected_colored = colorize_line(line_expected, TEXT_EXPECTED_COLOR) 
            print(f"{i:<7}| {line_actual_colored.ljust(29)} | {line_expected_colored}")
        else:
            print(f"{i:<7}| {line_actual.ljust(20)} | {line_expected}")

if __name__=="__main__":
# Example usage:
    actual_output = """Line 1
Line 2
Line 3"""

    expected_output = """Line 1
Modified Line 2
Line 3"""

    find_and_print_differences(actual_output, expected_output)
