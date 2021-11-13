import os
import shutil

def ask_file_name():
    file_name = ''
    while not file_name:
        file_name = input('What is the file name? ')
        search_path = input('What is the starting search path? ex: "/Users", "D:" ')
    return file_name, search_path

def find_files(filename, search_path):
    result = []

    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result

def list_to_string(mylist):
    mylist = str(mylist)
    mylist = mylist.strip("['")
    mylist = mylist.strip("']")
    return mylist

def change_dir(current_dir):
    print(f'This is where the file is now {current_dir}')
    question = ''
    while not question:
        question = input('Would you like to change the file location? ')
        question = question.upper()
        if question == 'Y':
            new_location = input('Where would you like the file? Please insert direct path: ')
            return new_location
        else:
            print('Your file is safe here. ')
            return current_dir

def move_file(old_location, new_location):
    shutil.move(old_location, new_location)

def main():
    file_name, search_path = ask_file_name()

    current_dir = find_files(file_name, search_path)
    print(current_dir)
    current_dir = list_to_string(current_dir)

    location = change_dir(current_dir)

    move_file(current_dir, location)

#/Users/densmoreb/Desktop/21Winter/CSE 111/Week 12/area_rectangle.py

main()