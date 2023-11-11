import subprocess
from pathlib import Path
from diff import find_and_print_differences
def run_test(input_str, expected_output, question_path):
    # Compile the C++ code
    compile_command = "s++ " + str(question_path) #LQ2_D_Q1.cpp"
    # print(compile_command)
    subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Run the compiled program with input
    run_command = f"./a.out"

    timeout_sec=5

    try:
        process = subprocess.run(run_command, input=input_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout = timeout_sec)
    
        # Check if the output matches the expected output
        actual_output = process.stdout.strip()

        passFlag =  actual_output == expected_output.strip()
        if not passFlag:
            find_and_print_differences(actual_output,expected_output)

        return passFlag
    except subprocess.TimeoutExpired:
        print(f"Test case timed out after {timeout_sec} seconds.")
        return False

def read_test_cases(file_path):

    file = open(file_path, "r") 
    lines = file.readlines()
    
    test_cases = []


    for line in lines:
        if line.startswith("#testcase_input"):
            test_cases.append("")
            
        elif line.startswith("#testcase_output"):
            test_cases.append("")
        else:
            test_cases[-1] += line
    
    return test_cases

def autograde(path):
    input_test_cases = read_test_cases("./testbenchi.txt")
    output_test_cases = read_test_cases("./testbencho.txt")
    enumerated_test_cases = enumerate(zip(input_test_cases, output_test_cases), 1)
    for i, (input_str, expected_output) in enumerated_test_cases:
        try:
            testSuccess = run_test(input_str, expected_output, path) 
        except Exception as e:
            testSuccess = False
            print("Error occured")
            print(e)
        if testSuccess:
            print(f"Test case {i}: Passed")
        else:
            print(f"Test case {i}: Failed")

def search_cpp_files(root_folder, filename_to_match):
    root = Path(root_folder)
    cpp_file_path_list=[]
    for roll_number_path in root.iterdir():
        if roll_number_path.is_dir():
            found = False
            for file_path in roll_number_path.rglob('*.cpp'):
                if filename_to_match in file_path.name:
                    print("-"*100)
                    print(f"{roll_number_path.name}: present")
                    cpp_file_path_list.append(file_path)
                    #autograde(file_path)
                    found = True
                    break
            if not found:
                print("-"*100)
                print(f"{roll_number_path.name}: absent")
    return cpp_file_path_list

if __name__ == "__main__":
    file_paths = search_cpp_files('../Day4_Thurs_9_Nov-20231110T172808Z-001', 'Q2')
    for path in file_paths:
        autograde(path)


