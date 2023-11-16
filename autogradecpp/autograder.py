import subprocess
from file_handler import search_cpp_files, read_test_cases
from diff import find_and_print_differences
import ansi_colors
def run_test(input_str, expected_output, question_path,timeout_sec, run_mode="standard"): 
    # If no output found, wait for timeout_sec = 5 seconds before throwing a timeout and moving on. This ensures program moves on even if DUT is stuck in infinite loop

    # Compile the C++ code
    compile_command = "g++ " + str(question_path)
    # print(compile_command)
    subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Run the compiled program with input
    run_command = f"./a.out"

    try:
        process = subprocess.run(run_command, input=input_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout = timeout_sec)
        # Check if the output matches the expected output
        actual_output = process.stdout.strip()
        passFlag =  actual_output == expected_output.strip()
        if (run_mode=="standard" and not passFlag) or run_mode=="verbose":
            find_and_print_differences(actual_output,expected_output)
        return passFlag
    except subprocess.TimeoutExpired:
        if run_mode!= "summary":
            print(ansi_colors.colorize_line(f"Test case timed out after {timeout_sec} seconds.",ansi_colors.ERROR_COLOR))
        return False

def autograde(path, input_test_cases, output_test_cases, run_mode="standard", timeout_sec=5):
    enumerated_test_cases = enumerate(zip(input_test_cases, output_test_cases), 1)
    total_cases = len(input_test_cases)
    num_test_passed = 0
    for i, (input_str, expected_output) in enumerated_test_cases:
        try:
            if run_mode != "summary":
                print(ansi_colors.colorize_line(f"\nEvaluating test case {i}\n",ansi_colors.FOREGROUND_COLORS['underline']), end='' if run_mode == "concise" else '\n')
            testSuccess = run_test(input_str=input_str, expected_output=expected_output, question_path=path, run_mode=run_mode, timeout_sec=timeout_sec) 
            num_test_passed+=testSuccess
        except Exception as e:
            testSuccess = False
            if run_mode != "summary":
                print(ansi_colors.colorize_line("An error occured while evaluting the test case", ansi_colors.ERROR_COLOR))
                print(e)
        if run_mode != "summary":
            if testSuccess:
                print(ansi_colors.colorize_line(f"Test case {i}: Passed", ansi_colors.TEST_PASSED_COLOR))
            else:
                print(f"Test case {i}: Failed")
            if run_mode != "concise":
                print()
    print(ansi_colors.colorize_line(f"Passed {num_test_passed}/{total_cases}",ansi_colors.BACKGROUND_COLORS['blue']))
        
def grade_root_dir(ROOT_FOLDER_PATH, FILENAME_TO_MATCH, TEST_INPUT_FILE_PATH, TEST_OUTPUT_FILE_PATH, RUN_MODE, WAIT_TIMEOUT_SEC):
    file_paths = search_cpp_files(ROOT_FOLDER_PATH, FILENAME_TO_MATCH)
    input_test_cases = read_test_cases(TEST_INPUT_FILE_PATH)
    output_test_cases = read_test_cases(TEST_OUTPUT_FILE_PATH)
    for roll in file_paths:
        print('\n'+"-"*100)
        path = file_paths[roll]
        message =ansi_colors.colorize_line( ansi_colors.colorize_line(f"{roll}: {path if path == 'absent' else 'present'}", ansi_colors.FOREGROUND_COLORS['yellow']), ansi_colors.FOREGROUND_COLORS['bold'])
        print(message)
        if path !="absent":
            autograde(path, input_test_cases, output_test_cases, run_mode=RUN_MODE, timeout_sec=WAIT_TIMEOUT_SEC)
  

if __name__ == "__main__":
    file_paths = search_cpp_files('../Day4_Thurs_9_Nov-20231110T172808Z-001', 'Q1')
    input_test_cases = read_test_cases("./inp.txt")
    output_test_cases = read_test_cases("./output.txt")
    for roll in file_paths:
        print("-"*100)
        path = file_paths[roll]
        message = f"\033[1m{roll}\033[22m: {path if path == 'absent' else 'present'}"
        print(message)
        if path !="absent":
            autograde(path, input_test_cases, output_test_cases)