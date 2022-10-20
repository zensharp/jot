#!/usr/bin/python3

import argparse
import glob
import os
import platform
import re
import subprocess
import yaml

# Helper
## Auxilary Classes
class Session:
    def __init__(self):
        self.verb = config["verb"]
        self.verbose = config["verbose"]
        self.dryRun = config["dry_run"]

# Helper functions
def tryRun(x):
    if session.dryRun:
        print(f"[DRY RUN] {x}")
        return False
    os.system(x)
    return True

def listOrSingle(x):
    if type(x) is list:
        return x
    return [x]

def dictGet(dict, key, fallback):
    if key in dict:
        return dict[key]
    return fallback

# Begin code
## Parse configuration
parser = argparse.ArgumentParser(description="Journal Helper", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("verb", help="The journal operation", nargs='?', default="load")
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logging")
parser.add_argument("-n", "--dry-run", action="store_true", help="Dry run mode")
config = vars(parser.parse_args())

## Parse environment
session = Session()

# Hack for console_scripts
def main():
    pass
