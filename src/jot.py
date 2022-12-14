#!/usr/bin/python3

import os
import pendulum
import sys

exe="$EDITOR %{path}:2147483647"

# Begin code
## Parse environment
if "JOT_DIR" in os.environ:
    jotRoot=os.path.expandvars("$JOT_DIR")
else:
    print("Journal directory not set! Please assign environment variable 'JOT_DIR'")
    exit(1)

if not os.path.exists(jotRoot):
    print("Journal directory does not exist! Please create before running 'jot'.")
    exit(1)

## Compute timestamps
now = pendulum.now()
week_of_year = f'{now.week_of_year:02}'
week_of_month = f'{now.week_of_month:02}'
editStart = pendulum.parse(f"{now.year}-W{week_of_year}")
editEnd = editStart.add(weeks=1)

## Compute file information
title = f"{now.format('MMMM')} Week #{editStart.week_of_month}"
timecode = f"{now.year}/{now.month}/week{now.week_of_month}"
destPath=f"{jotRoot}/{timecode}.md"
destDir=os.path.dirname(destPath)
## Create files (if necessary)
if not os.path.exists(destPath):
    if not os.path.exists(destDir):
        os.system(f"mkdir --parents '{destDir}'")
    original_stdout = sys.stdout
    with open(destPath, 'w') as f:
        sys.stdout = f
        print("---")
        print(f"title: '{title}'")
        print(f"date: {editStart}")
        print(f"publishDate: {editEnd}")
        print("---")
        sys.stdout = original_stdout

## Execute command
command = exe.replace("%{path}", destPath)
command = os.path.expandvars(command)

os.getcwd()
os.system(command)

# Hack for console_scripts
def main():
    pass
