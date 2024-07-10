from autogradercpp.ansi_colors import TEXT_FOUND_COLOR, TEXT_EXPECTED_COLOR, colorize_line

def find_and_print_differences(actual_text:str, expected_text:str) -> None:
    lines_actual = actual_text.splitlines()
    lines_expected = expected_text.splitlines()

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