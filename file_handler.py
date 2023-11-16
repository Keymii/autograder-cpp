from pathlib import Path
from diff import  colorize_line
from ansi_colors import ERROR_COLOR
def search_cpp_files(root_folder, filename_to_match):
    root = Path(root_folder)
    cpp_file_path_dict={}
    for roll_number_path in root.iterdir():
        if roll_number_path.is_dir():
            found = False
            for file_path in roll_number_path.rglob('*.cpp'):
                if filename_to_match in file_path.name:
                    cpp_file_path_dict[roll_number_path.name]=file_path
                    found = True
                    break
            if not found:
                cpp_file_path_dict[roll_number_path.name]="absent"
    return cpp_file_path_dict

def read_test_cases(file_path):
    file = open(file_path, "r") 
    lines = file.readlines()
    test_cases = []
    file_category = None
    for line in lines:
        if line.startswith("#testcase_input"):
            if file_category == "output":
                raise TestBenchValidationException("Input values found in output test case file, please check the test files")
            test_cases.append("")
            if file_category == None:
                file_category = "input"
            
        elif line.startswith("#testcase_output"):
            if file_category == "input":
                raise TestBenchValidationException("Output values found in input test case file, please check the test files")
            test_cases.append("")
            if file_category == None:
                file_category = "output"
        else:
            test_cases[-1] += line
        return test_cases
    
class TestBenchValidationException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self) -> str:
        return colorize_line(self.message, ERROR_COLOR)