import shutil
import os

def main():
    folder_path = "json_delta/temp"
    folder_path_new = "json_delta/temp1"
    shutil.rmtree(folder_path)
    os.makedirs(folder_path_new)
main()