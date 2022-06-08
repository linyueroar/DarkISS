#!/usr/bin/env python3

# @file meta_parser.py
#
# @brief Script to generate execution functions for opcodes.
#
# @section description Description
# This script parse isa specification and a description file.
# Generate C++ code for opcodes
#
# @section todo_list TODO
# - None.
#
# @section author_doxygen_example Author(s)
# - Created by Xingliang Wu on 05/27/2022.
#
# Copyright (c) 2022 linyueroar.  All rights reserved.

import os
import sys
import re
import glob
import yaml
import argparse
import pprint
import collections

import logging
from libs import util

def parse_arg() -> argparse.Namespace:
    """! All args and documents are defined here. Be specific.
    @return argparse.Namespace object of arguments.
    """

    description = """
    Parse agnostic opcode documentation to C++ functions.
    Other languages to be supported in the future
    """

    parser = argparse.ArgumentParser(
        description     = description,
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s', '--spec',
                        type     = str,
                        action   = "store",
                        required = True,
                        help     = 'Specification')
    parser.add_argument('-c', '--config',
                        type     = str,
                        action   = "store",
                        required = True,
                        help     = 'description to explain your ISA spec format')
    parser.add_argument('-v', '--verbose',
                        type     = int,
                        action   = "store",
                        default  = logging.INFO,
                        help     = """
                        Verbosity of tool.
                        Refer to https://verboselogs.readthedocs.io/en/latest/readme.html#id4""")

    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_arg()
    util.create_logger(__name__)
    set_logger_verb(__name__, args.verbose)

    with open(args.spec) as spec_fp:
        lines = spec_fp.readlines()
        for line in lines:
            pass
    pass

