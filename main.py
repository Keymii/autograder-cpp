import autograder
import file_handler
ROOT_FOLDER_PATH = '../Day4_Thurs_9_Nov-20231110T172808Z-001'
FILENAME_TO_MATCH = 'Q1' 

TEST_INPUT_FILE_PATH = "./inp.txt"
TEST_OUTPUT_FILE_PATH = "./output.txt"

file_paths = file_handler.search_cpp_files(ROOT_FOLDER_PATH, FILENAME_TO_MATCH)
input_test_cases = file_handler.read_test_cases(TEST_INPUT_FILE_PATH)
output_test_cases = file_handler.read_test_cases(TEST_OUTPUT_FILE_PATH)
for roll in file_paths:
    print("-"*100)
    path = file_paths[roll]
    message = f"\033[1m{roll}\033[22m: {path if path == 'absent' else 'present'}"
    print(message)
    if path !="absent":
        autograder.autograde(path, input_test_cases, output_test_cases)