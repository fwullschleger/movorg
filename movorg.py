import argparse
import fnmatch
import re
import os
import shutil
import subprocess
import sys
import logging

MOVIE_DIR = "Resident.Evil.The.Final.Chapter-2016"
WORKING_DIR = "workingDir"
TEST_DIR = 'some_directory'

logging.basicConfig(format='%(asctime)s %(message)s')


def prep_testdir(directory_argument):
    shutil.rmtree(MOVIE_DIR)
    shutil.copytree(WORKING_DIR, directory_argument)
    shell_tree_command(directory_argument)


def shell_tree_command(directory_argument):
    subprocess.run(["tree", directory_argument])


def parse_arguments():
    """Read arguments from a command line."""
    parser = argparse.ArgumentParser(description='Arguments get parsed via --commands')
    # parser.add_argument("-i", metavar='input file', required=False,
    #                     help='an input dataset in .txt file')
    parser.add_argument('directory', metavar='directory', nargs='+',
                        help='movie directory to organize')

    args = parser.parse_args()

    return args


def main():
    args = parse_arguments()

    # loop over parameters 1 to n, skip 1st element in array which is the script path and name
    for arg in vars(args):
        print("Argument: ", arg)

        prep_testdir(arg)

        with os.scandir(arg) as entries:
            for entry in entries:
                if entry.is_file():
                    # TODO: look for info, nfo and mkv files and delete other files, use [!seq] (see desc. of method)
                    if fnmatch.fnmatch(entry.name, "More-4K-Stuff.url"):
                        print("Removing file: ", entry.path)
                        os.remove(entry.path)
                    if fnmatch.fnmatch(entry.name, "*.mkv"):
                        match = re.search("^(\\w+(\\.\\w+)*)\\.([0-9]{4})(?!p)", entry.name)
                        # Full match	0-36	Resident.Evil.The.Final.Chapter.2016
                        # Group 0.              The entire match
                        # Group 1.  	0-31	Resident.Evil.The.Final.Chapter
                        # Group 2.  	23-31	.Chapter
                        # Group 3.  	32-36	2016
                        if match:
                            moveTitle_Year = match.group(1) + '-' + match.group(3)

        os.rename(arg, moveTitle_Year)
        shell_tree_command(moveTitle_Year)


if __name__ == '__main__':
    main()
