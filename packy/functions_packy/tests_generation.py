# tests_generation.py

import os
import re

src_dir = './src'
test_dir = './tests'
test_file_name = 'unit_tests.cpp'

def generate_test_template(class_name, return_type, params, 
                           function_name=None, comment=None, 
                           expected_result="0"):
    # If it's a class method, we need to create an object of the class
    if class_name:
        method_call = f'{class_name} obj; result = obj.{function_name}({", ".join(params)});'
    else:
        method_call = f'result = {function_name}({", ".join(params)});'



    test_template = f"""    
                  
// Test for function {function_name} {f'on {class_name}' if class_name else ''}
TEST({function_name}Test, BasicTest) {{
    {return_type} result;
    {method_call}
    EXPECT_EQ(result, {expected_result});
}}
""" 
    return test_template



def process_file(file_path):
    # Analyze file for finding functions to generate tests
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Regex to detect both class member functions and regular functions
    function_pattern = r'(\w+(?:\s*\*\s*\w+)*)\s+(\w+)\s*(?:::\s*(\w+))?\s*\((.*?)\)\s*(?=\{)'

    test_code = ""

    for line in lines:
        # Search functions/methods
        match = re.search(function_pattern, line)
        if match:
            return_type = match.group(1)
            function_name = match.group(2)
            class_name = match.group(3)  # This captures the class name if present

            # Skip the 'main' function (if present)
            if function_name == 'main':
                continue

            params = match.group(4).split(',')

            # Generate test for every found function
            test_code += generate_test_template(function_name, return_type, [param.strip() for param in params], class_name)

    return test_code


def create_tests():
    
    os.makedirs(test_dir, exist_ok=True)

    # Clean file before adding new tests
    with open(os.path.join(test_dir, test_file_name), 'w') as test_file:
        # Add standard headers for tests
        test_file.write('#include <gtest/gtest.h>\n#include "../src/function.h"\n\n')

        # Recursively go through all files in '/src' directory
        for root, _, files in os.walk(src_dir):
            for file_name in files:
                # Filter out non-C++ files
                if file_name.endswith('.cpp') or file_name.endswith('.h'):
                    file_path = os.path.join(root, file_name)
                    print(f"Processing file: {file_path}")  # Debugging line
                    test_code = process_file(file_path)

                    if test_code:
                        with open(os.path.join(test_dir, test_file_name), 'a') as test_file:
                            test_file.write(f"\n// Tests for file {file_name}\n")
                            test_file.write(test_code)
                    else:
                        print(f"No functions found in {file_path}")  # Debugging line

