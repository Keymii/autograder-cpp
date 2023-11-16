import autograder
import file_handler
import ansi_colors

ROOT_FOLDER_PATH = '../Day4_Thurs_9_Nov-20231110T172808Z-001'
FILENAME_TO_MATCH = 'Q1' 

TEST_INPUT_FILE_PATH = "./inp.txt"
TEST_OUTPUT_FILE_PATH = "./output.txt"

RUN_MODE = "standard" #Can choose from 'summary', 'concise', 'standard', 'verbose'

WAIT_TIMEOUT_SEC = 5 #If a file is taking too long to compile, fail it after this many seconds.

file_paths = file_handler.search_cpp_files(ROOT_FOLDER_PATH, FILENAME_TO_MATCH)
input_test_cases = file_handler.read_test_cases(TEST_INPUT_FILE_PATH)
output_test_cases = file_handler.read_test_cases(TEST_OUTPUT_FILE_PATH)
for roll in file_paths:
    print()
    print("-"*100)
    path = file_paths[roll]
    message =ansi_colors.colorize_line( ansi_colors.colorize_line(f"{roll}: {path if path == 'absent' else 'present'}", ansi_colors.FOREGROUND_COLORS['yellow']), ansi_colors.FOREGROUND_COLORS['bold'])
    print(message)
    if path !="absent":
        autograder.autograde(path, input_test_cases, output_test_cases, run_mode=RUN_MODE, timeout_sec=WAIT_TIMEOUT_SEC)