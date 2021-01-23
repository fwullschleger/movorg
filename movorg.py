import argparse
import fnmatch
import re
import os
import shutil
import subprocess
import sys
import logging
from logging import critical, error, info, warning, debug

MOVIE_DIR = "Resident.Evil.The.Final.Chapter-(2016)"
WORKING_DIR = "workingDir"
TEST_DIR = 'some_directory'


def prep_testdir(directory_argument):
    shutil.rmtree(MOVIE_DIR)
    shutil.copytree(WORKING_DIR, directory_argument)
    shell_tree_command(directory_argument)


def shell_tree_command(directory_argument):
    subprocess.run(["tree", directory_argument])


def parse_arguments():
    """Read arguments from a command line."""
    parser = argparse.ArgumentParser(description='Arguments get parsed via --commands')

    parser.add_argument('-v', metavar='verbosity', type=int, default=2,
                        help='Verbosity of logging: 0 -critical, 1- error, 2 -warning, 3 -info, 4 -debug')
    parser.add_argument('-w',
                        '--world',
                        action='store_true',
                        help='organize movies from hd-world.org')
    parser.add_argument('-n',
                        '--rename',
                        action='store_true',
                        help='rename movies from hd-world.org')
    parser.add_argument('directory',
                        action='store',
                        nargs='+',
                        help='movie directory to organize')

    args = parser.parse_args()
    verbose = {0: logging.CRITICAL, 1: logging.ERROR, 2: logging.WARNING, 3: logging.INFO, 4: logging.DEBUG}
    logging.basicConfig(format='%(asctime)s %(message)s', level=verbose[args.v], stream=sys.stdout)

    return args


def main():
    # loop over parameters 1 to n, skip 1st element in array which is the script path and name
    for directory in args.directory:
        debug("Directory: [%s]", directory)
        movie_title_year = directory

        # prep_testdir(directory)

        with os.scandir(directory) as entries:
            for entry in entries:

                if args.world:
                    org_hd_world(directory, entry)
                else:
                    movie_title_year = org_nima4k(entry, movie_title_year)

        if args.rename:
            rename_hd_world(directory)

        os.rename(directory, movie_title_year)
        shell_tree_command(movie_title_year)


def org_hd_world(directory, entry):
    if entry.is_file():
        if not fnmatch.fnmatch(entry.name, '*.mkv') and not fnmatch.fnmatch(entry.name, '*.nfo'):
            warning("Removing file: [%s]", entry.path)
            os.remove(entry.path)
    if entry.is_dir:
        if fnmatch.fnmatch(entry.name, 'Sample'):
            warning("Removing directory: [%s]", entry.path)
            shutil.rmtree(entry.path)
        if fnmatch.fnmatch(entry.name, 'Proof'):
            warning("Removing directory: [%s]", entry.path)
            shutil.rmtree(entry.path)
        if fnmatch.fnmatch(entry.name, 'Subs'):
            with os.scandir(entry.path) as subtitles:
                for subs in subtitles:
                    if subs.is_file:
                        info("Moving file [%s] up one directory.", subs.path)
                        shutil.move(subs.path, directory)
            warning("Removing directory: [%s]", entry.path)
            shutil.rmtree(entry.path)


def rename_hd_world(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file:
                info("Moving file [%s] up one directory.", entry.path)
                directory_name = directory.rstrip('/')
                new_filepath = re.sub('(?<=/)(.*[_|-]1080p)', directory_name, entry.path)
                os.renames(entry.path, new_filepath)


def org_nima4k(entry, movie_title_year):
    if entry.is_file():
        # TODO: look for info, nfo and mkv files and delete other files, use [!seq] (see desc. of method)
        if fnmatch.fnmatch(entry.name, "More-4K-Stuff.url"):
            warning("Removing file: [%s]", entry.path)
            os.remove(entry.path)
        if fnmatch.fnmatch(entry.name, "*.mkv"):
            match = re.search("^(\\w+(\\.\\w+)*)\\.([0-9]{4})(?!p)", entry.name)
            # Full match	0-36	Resident.Evil.The.Final.Chapter.2016
            # Group 0.              The entire match
            # Group 1.  	0-31	Resident.Evil.The.Final.Chapter
            # Group 2.  	23-31	.Chapter
            # Group 3.  	32-36	2016
            if match:
                movie_title_year = match.group(1) + '-(' + match.group(3) + ')'

    return movie_title_year


if __name__ == '__main__':
    args = parse_arguments()
    main()
