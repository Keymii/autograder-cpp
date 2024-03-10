import subprocess
from file_handler import search_cpp_files, read_test_cases
from diff import find_and_print_differences
import ansi_colors
from exceptions import GccCompilerException

class AutograderCpp:

    """
    List of supported run_modes (case sensitive):
    - verbose
    - standard
    - concise
    - summary

    """

    def __init__(self, run_mode:str="standard", timeout_sec:float=5, base_path:str="") -> None:
        self.configure(run_mode=run_mode, timeout_sec=timeout_sec, base_path=base_path)
        if not self.check_gcc_installed():
            raise GccCompilerException("Could not detect an installed instance of gcc/g++. Please check the compiler and try again.")

    def configure(self, run_mode:str="standard", timeout_sec:float=5, base_path:str="") -> None:
        self.run_mode = run_mode
        self.timeout_sec = timeout_sec
        self.base_path=base_path

    def check_gcc_installed(self):
        try:
            subprocess.run(['g++', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def run_test(self,input_str:str, expected_output:str, question_path:str) -> bool: 
        # If no output found, wait for timeout_sec (default 5) seconds before throwing a timeout and moving on. This ensures program moves on even if DUT is stuck in infinite loop

        # Compile the C++ code
        compile_command = "g++ " + str(question_path)
        # print(compile_command)
        subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Run the compiled program with input
        run_command = f"./a.out"

        try:
            process = subprocess.run(run_command, input=input_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout = self.timeout_sec)
            # Check if the output matches the expected output
            actual_output = process.stdout.strip()
            passFlag =  actual_output == expected_output.strip()
            if (self.run_mode=="standard" and not passFlag) or self.run_mode=="verbose":
                find_and_print_differences(actual_output,expected_output)
            return passFlag
        except subprocess.TimeoutExpired:
            if self.run_mode!= "summary":
                print(ansi_colors.colorize_line(f"Test case timed out after {self.timeout_sec} seconds.",ansi_colors.ERROR_COLOR))
            return False

    def autograde(self, path:str, input_test_cases:str, output_test_cases:str) -> None:
        enumerated_test_cases = enumerate(zip(input_test_cases, output_test_cases), 1)
        total_cases = len(input_test_cases)
        num_test_passed = 0
        for i, (input_str, expected_output) in enumerated_test_cases:
            try:
                if self.run_mode != "summary":
                    print(ansi_colors.colorize_line(f"\nEvaluating test case {i}\n",ansi_colors.FOREGROUND_COLORS['underline']), end='' if self.run_mode == "concise" else '\n')
                testSuccess = self.run_test(input_str=input_str, expected_output=expected_output, question_path=path) 
                num_test_passed+=testSuccess
            except Exception as e:
                testSuccess = False
                if self.run_mode != "summary":
                    print(ansi_colors.colorize_line("An error occured while evaluting the test case", ansi_colors.ERROR_COLOR))
                    print(e)
            if self.run_mode != "summary":
                if testSuccess:
                    print(ansi_colors.colorize_line(f"Test case {i}: Passed", ansi_colors.TEST_PASSED_COLOR))
                else:
                    print(f"Test case {i}: Failed")
                if self.run_mode != "concise":
                    print()
        print(ansi_colors.colorize_line(f"Passed {num_test_passed}/{total_cases}",ansi_colors.BACKGROUND_COLORS['blue']))
            
    def grade_root_dir(self, ROOT_FOLDER_PATH:str, FILENAME_TO_MATCH:str, TEST_INPUT_FILE_PATH:str, TEST_OUTPUT_FILE_PATH:str) -> None:
        file_paths = search_cpp_files(self.base_path + ROOT_FOLDER_PATH, FILENAME_TO_MATCH)
        input_test_cases = read_test_cases(self.base_path + TEST_INPUT_FILE_PATH)
        output_test_cases = read_test_cases(self.base_path + TEST_OUTPUT_FILE_PATH)
        for roll in file_paths:
            print('\n'+"-"*100)
            path = file_paths[roll]
            message =ansi_colors.colorize_line( ansi_colors.colorize_line(f"{roll}: {path if path == 'absent' else 'present'}", ansi_colors.FOREGROUND_COLORS['yellow']), ansi_colors.FOREGROUND_COLORS['bold'])
            print(message)
            if path !="absent":
                self.autograde(path, input_test_cases, output_test_cases)
    
if __name__ == "__main__":
    autograder = AutograderCpp(base_path='/media/keymii/SecondBox/autograder/', run_mode='concise', timeout_sec=1)
    autograder.grade_root_dir("Day4_Thurs_9_Nov-20231110T172808Z-001", "Q1", "testbenchi.txt", "testbencho.txt" )
