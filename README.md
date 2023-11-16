# Autograder for C++

## Overview

The given autograder expects that there is a directory containing all the files under test in following order -

    root_folder
        |---- roll1
        |       |---- file1.cpp
        |       |---- file2.cpp
        |       |---- some_filename_to_match.cpp
        |---- roll2
        |       |---- file1.cpp
            ...

Roll is the unique identification string of each submitter.

The autograder looks for every folder/roll in the root folder and checks for the first file whose filename contains the keyword ```filename_to_match```, a parameter to the helper function ```search_cpp_files(root_folder, filename_to_match)```. If found, the file is tested under the provided input and output cases. Otherwise, absent is marked.

<!-- ## Modes

- **Concise:** Only shows if the testcase was passed or failed
- **Standard:** Shows passed if test case was passed, shows line-by-line comparision of actual and expected outputs if test case was failed
- **Verbose:** Shows line-by-line comparision of actual and expected outputs for each test case -->

## Instructions

| :exclamation:  Make sure you have g++ compiler installed on your system before running the autograder|
|-----------------------------------------|
1. Create an input file and separate input test cases using a line containing ```#testcase_input``` keyword
2. Create an output file and separate inputcases using a line containing ```#testcase_output``` keyword
3. Specify the required data in the variables declared in main.py
4. Run ```main.py``` 