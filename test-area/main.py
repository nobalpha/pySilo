# TODO directory management bug

from os.path import isfile, join, isdir
import re
import os
from typing import Tuple
from dearpygui.dearpygui import *

    
def apply_selected_directory(sender, data):
    directory = "{0}/{1}".format(data[0], data[1])
    add_data("directory", directory)


def directory_picker(sender, data):
    select_directory_dialog(callback=apply_selected_directory)


def file_diff(sender, data):
    add_window("File Diff", 100, 100, resizable=False, title_bar=False, autosize=True)
    for i in range(10):
        add_text("hello there" + str(i))
    add_spacing(count=5)
    add_button("Apply changes")
    add_same_line()
    add_button("Cancel", callback="end")


def re_counter(array: list, counter: int, pattern: str) -> Tuple[list, int]:  # Counting & returning the matched ones
    """
    :param array:
    :param counter:
    :param pattern:
    :return:
    :rtype: Tuple[list, int]
    """
    temp = []
    for elem in array:
        if re.fullmatch(pattern, elem):
            counter += 1
            temp.append(elem)
    return temp, counter


def file_organizer(sender, data) -> None:  # Moving the files based on some rules
    """
    :param sender
    :param data
    :return: None
    """
    path = get_data("directory")  # Getting the path from DearPy label text
    separator = "."  # Setting the default separator
    show_logger()  # Setting up the logger
    set_log_level(0)  # To show all the logs

    files = [f for f in os.listdir(path) if isfile(join(path, f))]  # Getting the files from the specified directory

    for file in files:  # Looping through all the files
        print("File: {0}\nPath: {1}".format(file, "{0}/{1}".format(path, file)))
        if (p := file.rfind(separator)) >= 0:  # Getting the extension
            if not isdir(join(path, file[p:])):  # If there isn't any directory with the file,
                print("No directory associated with the extension found.")
                log_debug("No directory associated with the extension found.")
                os.mkdir(join(path, file[p:]))  # Creating new file with the initial file extension.
                os.replace(join(path, file), join(path, file[p:], file))  # Moving the file to the created directory.
                log_debug("Created a new folder for {0}".format(file))
                print("Created a new folder for {0}".format(file))
                new_name = file
            else:  # If the folder with the file's extension exists,
                print("Extension directory found.")
                if isfile(new_path := join(path, file[p:], file)):  # If a file with the same name exists,
                    print("Same file name exists...\nConfiguring new one with RegEx...")
                    dummy_files = [f for f in os.listdir(join(path, file[p:]))
                                   if isfile(join(path, file[p:], f))]  # Getting the contents of the extension file
                    arr, _ = re_counter(
                        dummy_files, 0, r"^{name}-\d+\.\w*$".format(name=file[:p]))  # Getting the RegExed files
                    print("Debug:", arr)
                    if not arr:
                        dummy = 0
                    else:
                        log_debug(dummy :=
                                  int(re.findall(r"\d", sorted(arr, reverse=True)[0])[0]))  # Getting the biggest digit

                    os.replace(join(path, file),
                               join(path, file[p:],
                                    new_name := "{0}-{1}{2}".format(file[:p], str(dummy + 1), file[p:])))  # Moving the RegExed file

                    log_debug("{0}-{1}{2}".format(file[:p], str(dummy + 1), file[p:]))
                    print("Created new file with RegEx {0}".format("{0}-{1}{2}".format(
                        file[:p], str(dummy + 1), file[p:])))
                else:  # If there isn't any occurrences,
                    print("No repeating file found...\nJust changing the directory...")
                    os.replace(join(path, file),
                               join(path, file[p:], file))  # Moving the file as it is
                    new_name = file

                print("New File: {0}\nNew Path:{1}".format(file, new_path))
                print(new_name)

        else:  # If no extension is provided to the file,
            log_warning("No extension found for {0}".format(file))
            print("No extension found for {0}".format(file))

        print("-------------------")
        log_debug("-------------------")


set_main_window_size(500, 500)
cwd = os.getcwd()
add_label_text("##filedir", cwd, data_source="directory")
add_separator()
add_button("Directory Selector", callback=directory_picker)
add_button("Diff", callback=file_organizer)

start_dearpygui()