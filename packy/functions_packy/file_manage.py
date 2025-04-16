# file_manage.py

import os
import shutil

# Create, dublicate lab templ
# name lab and save lab number

current_dir    = os.getcwd()
template_dir   = os.path.join(current_dir, './lab_templ')
templ_file_dir = "./report/lab-number.txt"


def Input_lab_nums():
    numbers = []

    while True: 
        # Step 1: Ask lab number
        lab_number = input("Write lab number: ")
        numbers.append(lab_number)
        print( "[+] Labs will be created: " + str(numbers) )
        
        # Step 2: Continue or exit 
        if input("Do you want to continue? [y/n]: ").lower() != "y":
            break  # If the answer is not "y", exit the loop

    return numbers

def Create_labs(numbers):
    
    for lab_number in numbers:

        target_dir = os.path.join(current_dir, f"{lab_number}_lab")

        # Step 1: Copy the template directory (only if it doesn't exist)
        if not os.path.exists(target_dir):
            shutil.copytree(template_dir, target_dir)
        else:
            print(f"[-] Warning: {target_dir} already exists. Skipping.")
            continue

        # Step 2: Modify a specific file inside the copied directory
        file_path = os.path.join(target_dir, templ_file_dir)
        with open(file_path, "w") as f:
            f.write(lab_number)  # Write some content to the file

        print(f"[+] Lab №{lab_number} created.")



# numbers = Input_lab_nums()
# Create_labs(numbers)
