from os.path import isfile, join, isdir
import re
import os
from typing import Tuple, Dict, List
from dearpygui.core import *
from dearpygui.simple import *


window_width, window_height = 650, 635
widget_width = 400
widget_height = 300


# def resimulate_organization(sender, data) -> None:
#     path = get_data("directory")

#     if path and os.path.exists(path):
#         dirs = [f for f in os.listdir(path) if isdir(join(path, f))]
#         print(dirs)
#         for dir in dirs:
#             dir_path = join(path, dir)
#             print("Directory: {0}\nPath: {1}".format(dir, dir_path))
#             for file in os.listdir(dir_path):
#                 file_path = join(dir_path, file)
#                 print("Moving {0} file to .. [path: {1}]".format(file, file_path))
#                 os.replace(file_path, join(path, file))
#             print("Removing {0} directory [path: {1}]".format(dir, dir_path))
#             os.rmdir(dir_path)


# def clear_directory_selector(sender, data) -> None:
#     set_value("directory_label", "Selected directory shows here...")
#     add_data("directory", "")


# def apply_selected_directory(sender, data) -> None:
#     directory = join(data[0], data[1])
#     print(directory)
#     add_data("directory", directory)
#     set_value("directory_label", get_data("directory"))


# def directory_picker_callback(sender, data) -> None:
#     select_directory_dialog(callback=apply_selected_directory)


# def re_counter(array: list, counter: int, pattern: str) -> Tuple[list, int]:  # Counting & returning the matched ones
#     """
#     :param array:
#     :param counter:
#     :param pattern:
#     :return:
#     :rtype: Tuple[list, int]
#     """
#     temp = []
#     for elem in array:
#         if re.fullmatch(pattern, elem):
#             counter += 1
#             temp.append(elem)
#     return temp, counter


# def file_explorer(sender="", data="") -> Dict[str, List[str]]:  # Moving the files based on some rules
#     """
#     :param sender
#     :param data
#     :return: None
#     """
#     extension_log = {}
#     path = get_data("directory")  # Getting the path from directory data
#     separator = "."  # Setting the default separator
#     show_logger()  # Setting up the logger
#     set_log_level(0)  # To show all the logs
#     if path and os.path.exists(path):
#         files = [f for f in os.listdir(path) if isfile(join(path, f))]  # Getting the files from the specified directory

#         for file in files:  # Looping through all the files
#             print("File: {0}\nPath: {1}".format(file, join(path, file)))
#             if (p := file.rfind(separator)) >= 0:  # Getting the extension
#                 if not isdir(join(path, file[p:])):  # If there isn't any directory with the file,
#                     print("No directory associated with the extension found.")
#                     log_debug("No directory associated with the extension found.")
#                     new_name = join(file[p:], file)
#                 else:  # If the folder with the file's extension exists,
#                     print("Extension directory found.")
#                     if isfile(new_path := join(path, file[p:], file)):  # If a file with the same name exists,
#                         print("Same file name exists...\nConfiguring new one with RegEx...")
#                         dummy_files = [f for f in os.listdir(join(path, file[p:]))
#                                        if isfile(join(path, file[p:], f))]  # Getting the contents of the extension file
#                         arr, _ = re_counter(
#                             dummy_files, 0, r"^{name}-\d+\.\w*$".format(name=file[:p]))  # Getting the RegExed files
#                         print("Debug:", arr)
#                         if not arr:
#                             dummy = 0
#                         else:
#                             log_debug(dummy :=
#                                       int(re.findall(r"\d", sorted(arr, reverse=True)[0])[0]))  # Getting the biggest digit

#                         new_name = join(file[p:], "{0}-{1}{2}".format(file[:p], str(dummy + 1), file[p:]))
#                         log_debug("{0}-{1}{2}".format(file[:p], str(dummy + 1), file[p:]))

#                     else:  # If there isn't any occurrences,
#                         print("No repeating file found...\nJust changing the directory...")
#                         new_name = join(file[p:], file)

#                     print("New File: {0}\nNew Path:{1}".format(file, new_path))

#                 print(new_name)

#                 try:
#                     extension_log[file[p:]] = [*extension_log[file[p:]], (file, new_name)]
#                 except KeyError:
#                     extension_log[file[p:]] = [(file, new_name)]

#             else:  # If no extension is provided to the file,
#                 log_warning("No extension found for {0}".format(file))
#                 print("No extension found for {0}".format(file))

#             print("-------------------")
#             log_debug("-------------------")

#         print(extension_log)
#         return extension_log


# def file_diff(sender="", data=""):
#     if data:
#         f_data = data
#     else:
#         f_data = file_explorer()
#     print(f_data)
#     delete_item("File Differ")
#     with window("File Differ", width=widget_width, height=widget_height, no_resize=True, no_close=True, autosize=True, no_move=False,  x_pos=(window_width-widget_width) // 2, y_pos=widget_height):
#         if f_data:
#             add_tab_bar("differ")
#             for f_ext, f_names in f_data.items():
#                 print(f_ext)
#                 add_tab(f_ext, tip="List of files which have {0} extension...".format(f_ext))
#                 for f_name in f_names:
#                     print("\t{0}\n".format(f_name))
#                     name = "{0}->{1}".format(f_name[0], f_name[1])
#                     add_text(name=name)
#                     add_same_line()
#                     add_button(name="{0}_button".format(name), arrow=True,
#                                tip="Remove this change.", callback_data=[name, f_data], callback=diff_switch)
#                 add_dummy()
#                 end()
#         else:
#             add_text("Nothing to arrange!")

#         add_spacing(count=5)
#         add_separator()
#         add_button("Refresh", callback=file_diff)
#         add_same_line()

#         if f_data:
#             add_button("Apply changes", callback_data=["apply", f_data], callback=diff_switch)
#             add_same_line()
#             add_button("Cancel", callback_data="close", callback=diff_switch)
#         else:
#             add_button("Close", callback_data="close", callback=diff_switch)


# def diff_switch(sender, data):
#     if data == "close":
#         delete_item("File Differ")
#     elif isinstance(data, list):
#         cmd = data[0]
#         extensions = data[1]
#         print("cmd")
#         if cmd == "apply":
#             print("hey")
#             if file_arranger(data=extensions):
#                 print("All extensioned files have been arranged...")

#         else:
#             element = cmd
#             print(element)
#             print(extensions)
#             temp = element.split("->")
#             to_be_searched = tuple(element.split("->"))
#             extension = temp[0][temp[0].rfind("."):]
#             dummy = extensions[extension].index(to_be_searched)
#             del extensions[extension][dummy]
#             if not extensions[extension]:
#                 del extensions[extension]
#             print(extensions)
#             file_diff(data=extensions)


# def file_arranger(sender="", data=""):
#     if data:
#         path = get_data("directory")
#         for extension, changes in data.items():
#             for old, new in changes:  # Relative paths
#                 os.replace(join(path, old), join(path, new))
#                 print(old, new)
#         return True


# # if change:
# #                         os.mkdir(join(path, file[p:]))  # Creating new file with the initial file extension.
# #                         # Moving the file to the created directory.
# #                         os.replace(join(path, file), join(path, file[p:], file))
# #                         log_debug("Created a new folder for {0}".format(file))
# #                         print("Created a new folder for {0}".format(file))


# # if change:
# #                             os.replace(join(path, file),
# #                                        join(path, file[p:],
# #                                             new_name := "{0}-{1}{2}".format(file[:p], str(dummy + 1), file[p:])))  # Moving the RegExed file
# #                             print("Created new file with RegEx {0}".format("{0}-{1}{2}".format(
# #                                 file[:p], str(dummy + 1), file[p:])))

# # if change:
# #                             os.replace(join(path, file),
# #                                        join(path, file[p:], file))  # Moving the file as it is
