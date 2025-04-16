# packy-fuctions.py

import os
import shutil
import argparse
import subprocess



# Build project
def build():
    # Check if CMakeLists.txt exists in the current directory
    if os.path.exists("CMakeLists.txt"):
        # Ensure the 'build' directory exists or create it
        os.makedirs("build", exist_ok=True)

        # Run cmake to configure the project
        try:
            print("Running CMake configuration...")
            subprocess.run(["cmake", "-S", ".", "-B", "build"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"CMake configuration failed: {e}")
            exit(1)

        # Run cmake to build the project
        try:
            print("Building project...")
            subprocess.run(["cmake", "--build", "build"], check=True)
            print("Compilation successful!")
        except subprocess.CalledProcessError as e:
            print(f"Build failed: {e}")
            exit(1)

    else:
        print("No CMakeLists.txt found in the current directory!")
        exit(1)



# Run application to test it
def run():
    try:
        print("\n\n=== RUNNING APPLICATION ===\n")
        subprocess.run(["./build/unit_tests"], check=True)
        subprocess.run(["./build/lab"], check=True)
    except Exception as e:
        print(f"Error running application: {e}")
        
