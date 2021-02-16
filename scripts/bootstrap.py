#!/usr/bin/env python3

import argparse
from pathlib import Path
import os

project_files=["CMakeLists.txt", "src/CMakeLists.txt"]
class_files=["src/main.cpp", "src/Class.cpp", "include/Class.h"]

def main():
    args = cli()
    if (args.interactive):
        interactive()
    else:
        replaceName(args.name)
        replaceClass(args.classname)

def replace(filename, pre_string, post_string):
    with open(filename, 'r') as f: 
        file_source = f.read()
    replace_string = file_source.replace(pre_string, post_string)
    with open(filename, 'w') as f: 
        f.write(replace_string)

def replaceName(name):
    for f in project_files:
        replace(f, "projectname", name)

def replaceClass(name):
    for f in class_files:
        if "main" in f:
            replace(f, "Class", name)
        else:
            replace(f, "Class", name)
            replace(f, "CLASS", name.upper())
            fext = Path(f).suffix
            fpth = Path(f).parent.stem
            os.rename(f, fpth+"/"+name+fext)
    for f in project_files:
        replace(f, "Class", name)


def interactive():
    ...

def cli():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Bootstrapper for cpp_template\n \nRenames files, classes etc.",
        epilog= "Example usage: \n"
                "  bootstrap.py -i \n"
                "  bootstrap.py -n projectname -c ProjectClass \n"
        )

    parser.add_argument('-i','--interactive', action='store_true', help="Interactive mode")
    parser.add_argument('-n','--name', default=None, nargs='?', help="Project name - for cmake and exec")
    parser.add_argument('-c','--classname', default=None, nargs='?', help="Class name - for class names and filenames")
    args = parser.parse_args() 
    return args

if __name__ == "__main__":
    main()