import pyperclip
import keyboard

def copy_line_to_clipboard(file_path):
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            pyperclip.copy(first_line)
            print("Line copied:", first_line)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def remove_first_line(file_path):
    try:
        with open(file_path, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(file_path, 'w') as fout:
            fout.writelines(data[1:])
    except Exception as e:
        print("An error occured", e)

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    while(True):
        for i in range(10):
            print("When CTRL+V is pressed, copying next line.")
            keyboard.wait('ctrl+v')
            copy_line_to_clipboard(file_path)
            remove_first_line(file_path)
        restart = input("10 codes copied, restart program ? (Y/N)")
        if restart.lower() != "y":
            print("program  ended.")
            break
