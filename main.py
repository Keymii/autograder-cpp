import sys
sys.path.insert(1, './autogradecpp')# caution: path[0] is reserved for script path (or '' in REPL)
from autogradecpp import autograder, file_handler, ansi_colors


ROOT_FOLDER_PATH = '../Day4_Thurs_9_Nov-20231110T172808Z-001'
FILENAME_TO_MATCH = 'Q1' 

TEST_INPUT_FILE_PATH = "./inp.txt"
TEST_OUTPUT_FILE_PATH = "./output.txt"

RUN_MODE = "standard" #Can choose from 'summary', 'concise', 'standard', 'verbose'

WAIT_TIMEOUT_SEC = 5 #If a file is taking too long to compile, fail it after this many seconds.
          
if __name__=="__main__":
    autograder.grade_root_dir(ROOT_FOLDER_PATH, FILENAME_TO_MATCH, TEST_INPUT_FILE_PATH, TEST_OUTPUT_FILE_PATH, RUN_MODE, WAIT_TIMEOUT_SEC)