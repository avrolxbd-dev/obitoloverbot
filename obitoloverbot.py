import time
import sys

logo = '''   _____ _                                
 |_   _| |           /\                  
   | | | |_ ____    /  \__   ___ __ ___  
   | | | __|_  /   / /\ \ \ / / '__/ _ \ 
  _| |_| |_ / /   / ____ \ V /| | | (_) |
 |_____|\__/___| /_/    \_\_/ |_|  \___/ 
                                         
                                         
'''

# Function to take user input
def get_user_input():
    print("Please provide the following details:")
    data_type = input("Enter the data type (e.g., 'Gmail', 'Hotmail', 'Yahoo'): ")
    sheet_link = input("Enter the sheet link: ")
    return data_type, sheet_link

# Function to print text slowly (typing animation)
def slow_print(text, color_code="\033[91m", delay=0.002):
    """Print text with typing animation and color"""
    sys.stdout.write(color_code)  # set color
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")  # reset color

# Function to display logo with animation
def display_tool_logo():
    print("\n********************************")
    slow_print(logo, color_code="\033[91m", delay=0.0015)  # red = \033[91m
    print("********************************\n")

# Function to perform the main task
def perform_task():
    print("Starting the tool...\n")
    for i in range(50):
        # Print 'Checked' in green using ANSI escape codes
        print(f"\033[92m{i+1} Checked\033[0m")
        time.sleep(0.1)

# Main function to run the tool
def run_tool():
    data_type, sheet_link = get_user_input()
    print(f"Data Type: {data_type}")
    print(f"Sheet Link: {sheet_link}\n")

    display_tool_logo()
    perform_task()

if __name__ == "__main__":
    run_tool()
