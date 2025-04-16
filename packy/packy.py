# packy.py


import sys
import os
import argparse

# Get the absolute path of the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the path to the functions_packy folder to sys.path
sys.path.append(os.path.join(script_dir, 'functions_packy'))



def main():

    parser = argparse.ArgumentParser(description="Packy - your friendly helper in passing labs")
    
    # Adding command-line arguments
    # # parser.add_argument('-h', '--help', action='store_true', help='Packy help info')
    parser.add_argument('-b', '--build', action='store_true', help='Build project with CMake')
    parser.add_argument('-r', '--run',   action='store_true', help='Run your build code')
    parser.add_argument('-t', '--test',  action='store_true', help='Create unit test code templ')
    parser.add_argument('-o', '--org',   action='store_true', help='Help create new labs dir')
    parser.add_argument('-d', '--doc',   action='store_true', help='Create report docx file')

    args = parser.parse_args()
    
    if args.build:
        from packy_functions import build, run
        build()
        run()
    
    elif args.run:
        from packy_functions import run
        run()
    
    elif args.test:
        from tests_generation import create_tests
        create_tests()
    
    elif args.org:
        from file_manage import Input_lab_nums, Create_labs
        numbers = Input_lab_nums()
        Create_labs(numbers)

    elif args.doc:
        from auto_report import gen_doc
        gen_doc()
    
if __name__ == "__main__":
    main()
