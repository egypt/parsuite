#!/usr/bin/python3.6

import argparse
import os
from pathlib import Path
from sys import exit, modules as sys_modules

from parsuite import modules
from parsuite import helpers
from parsuite.core.suffix_printer import *
from parsuite.core.argument import Argument

if __name__ == '__main__':

    ap = argument_parser = argparse.ArgumentParser(
        description='Parse the planet.')


    subparsers = ap.add_subparsers(help='Parser module selection.')
    subparsers.required = True
    subparsers.dest = 'module'
    esprint('Starting the parser')
    # strap arguments from modules as argument groups
    esprint('Loading modules')
    for handle,module in modules.handles.items():

        helpers.validate_module(module)
        sub = subparsers.add_parser(handle,help=module.help)

        for arg in module.args:
            sub.add_argument(*arg.pargs, **arg.kwargs)

    args = ap.parse_args()
    
    if 'input_file' in args:
        helpers.validate_input_file(args.input_file)

    esprint(f'Executing module: {args.module}')

    modules.handles[args.module].parse(
        **vars(args)
    )
    
    esprint('Module execution complete. Exiting.')