import os
import subprocess

def execute_python_scripts_in_folder(folder_path):
    # Get the name of the current script
    current_script_name = os.path.basename(__file__)

    # List all files in the folder
    python_files = [f for f in os.listdir(folder_path) if f.endswith('.py') and f != current_script_name]

    # Sort files to ensure a consistent order and execute every other script
    for script in python_files[::2]:  # Slicing with [::2] to get every other script
        script_path = os.path.join(folder_path, script)
        print(f"Executing: {script_path}")
        try:
            # Execute the script using subprocess
            subprocess.run(['python', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while executing {script}: {e}")

if __name__ == "__main__":
    # Replace 'your_folder_path' with the path to your folder containing the scripts
    folder_path = 'C:/Users/apcoelho/Desktop/Selenium Scripts'  # e.g., 'C:/path/to/your/folder'
    execute_python_scripts_in_folder(folder_path)
