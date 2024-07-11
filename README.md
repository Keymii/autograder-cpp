# Autograder for C++

## Overview

The program expects that there is a directory containing all the files under test in following order -

    base_path/
        |---- some_path1/testbenchi.txt
        |---- some_path2/testbencho.txt
        |---- some_path3/root_folder/
                    |---- roll1/
                    |       |---- file1.cpp
                    |       |---- file2.cpp
                    |       |---- some_filename_to_match.cpp
                    |---- roll2/
                    |       |---- file1.cpp
                        ...

In most cases `base_path` could be kept an empty string.  

`Roll` is the unique identification string of each submitter.

The autograder looks for every folder/roll in the root folder and checks for the first file whose filename contains the keyword ```filename_to_match```, a parameter to the helper function ```search_cpp_files(root_folder, filename_to_match)```. If found, the file is tested under the provided input and output cases. Otherwise, absent is marked.

## Modes

- **Summary:**  Only shows the net number of test cases passed
- **Concise:** Shows whether the testcase was passed or failed
- **Standard:** Shows passed if test case was passed, shows line-by-line comparision of actual and expected outputs if test case was failed
- **Verbose:** Shows line-by-line comparision of actual and expected outputs for each test case

## User Instructions

| :exclamation:  Make sure you have g++ compiler installed on your system before running the autograder|
|-----------------------------------------|
1. Create an *.txt file containing sample inputs and separate the input test cases using a line containing ```#testcase_input``` as the beginnig keyword
2. Create an *.txt file containing expected outputs and separate the test cases using a line containing ```#testcase_output``` as the beginning keyword
3. Execute the following program with proper parameters

```python
from autogradercpp.autograder import AutograderCpp

autograder = AutograderCpp(
        base_path=BASE_PATH, 
        run_mode=RUN_MODE, 
        timeout_sec=WAIT_TIMEOUT_SEC
    )

autograder.grade_root_dir(
        ROOT_FOLDER_PATH, 
        FILENAME_TO_MATCH, 
        TEST_INPUT_FILE_PATH, 
        TEST_OUTPUT_FILE_PATH 
    )
```


## Some Helper Functions

Below are some helper functions whose usability, I believe, can be expanded beyond just this autograder.

- autograder.py contains ```grade_root_dir(args*)``` which runs the assembled process of finding files and grading every single roll.
- file_handler.py contains ```read_test_cases(str)``` which returns the test case inputs and expected outputs into an array readable by autograder. It has to be run separately for input file and output file. 
- autograder.py contains ```autograde(args*)``` which can run the testbench on one file at a time
- diff.py contains ```find_and_print_differences(actual_text, expected_text)``` which compares the texts line by line
