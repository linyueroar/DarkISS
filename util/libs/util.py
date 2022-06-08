##
# @file util.py
#
# @brief commonly used functions this whole project shared.
#
# @section description Description
# This package includes commonly used functions.
# Go over it before you add any new util functions.
# Likely something you need has already been implemented here.
#
# @section libraries_main Libraries/Modules
# - logging libraries.
#   - Set logging verbosity
# - file processing libraries.
#   - Access to Sensor and TempSensor classes.
#
# @section todo_list TODO
# - None.
#
# @section author_doxygen_example Author(s)
# - Created by Xingliang Wu on 05/27/2022.
#
# Copyright (c) 2022 linyueroar.  All rights reserved.


import yaml
import logging
import verboselogs

def load_yml(input_yml:str) -> dict :
    """! Helper function. Load yml by dir name and return dict of yml.
    @return dict of loaded yml
    """
    with open(input_yml, 'r') as yml_fp :
        yml= yaml.safe_load(yml_fp)
        return yml

def create_logger(name:str) -> None:
    """! Helper function. Create logger with given name
    @param name The name of looger to be created
    """
    logger = verboselogs.VerboseLogger(name)
    print(name)

def set_logger_verb(name:str, verbosity:int) -> None:
    """! Helper function. Load yml by dir name and return dict of yml.
    @param name         The name of looger to be created
    @param verbosity    Verbosity for the logger. Detail defines refer to 
                        https://verboselogs.readthedocs.io/en/latest/readme.html#id4
    """
    logger = logging.getLogger(name)
    logger.setLevel(verbosity)

