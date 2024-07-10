from autogradercpp import autograder, file_handler, ansi_colors

BASE_PATH = 'base-path/'
ROOT_FOLDER_PATH = 'root-folder/'
FILENAME_TO_MATCH = 'Q1' 

TEST_INPUT_FILE_PATH = "testbenchi.txt"
TEST_OUTPUT_FILE_PATH = "testbencho.txt"

RUN_MODE = "standard" #Can choose from 'summary', 'concise', 'standard', 'verbose'

WAIT_TIMEOUT_SEC = 1 #If a file is taking too long to compile, fail it after WAIT_TIMEOUT_SEC seconds.
          
if __name__=="__main__":
    autograder = autograder.AutograderCpp(base_path=BASE_PATH, run_mode=RUN_MODE, timeout_sec=WAIT_TIMEOUT_SEC)
    autograder.grade_root_dir(ROOT_FOLDER_PATH, FILENAME_TO_MATCH, TEST_INPUT_FILE_PATH, TEST_OUTPUT_FILE_PATH )
