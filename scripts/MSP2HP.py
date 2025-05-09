# -*- coding: utf-8 -*-
import mh_operator_legacy as _

from mh_operator.legacy.common import get_argv, get_logger, global_state, is_main

global_state.LibraryAccess = LibraryAccess

from mh_operator.legacy.LibraryEdit import import_jcamps

logger = get_logger()

import glob
import logging
import os


def main():
    import argparse

    argv = get_argv()
    parser = argparse.ArgumentParser(
        prog=argv[0],
        description="Convert the MSP to .L (HP) format",
        epilog="Example: shebang --interpreter LEC MSP2HP.py -- --output 'C:\MassHunter\Library\demo.L' --verbose /path/to/jdx/dir/",
    )
    parser.add_argument("jdxs", nargs="+", help="The jcamp file or directory path")
    parser.add_argument("-o", "--output", help="The output library path")
    parser.add_argument(
        "-f",
        "--force",
        default=False,
        action="store_true",
        help="overwrite exsting library",
    )
    parser.add_argument(
        "-v", "--verbose", default=False, action="store_true", help="verbose logging"
    )
    args = parser.parse_args(argv[1:])

    if args.verbose:
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
    logger.debug("file: {}, input: {}".format(__file__, args.output))

    jdx_path = []
    for p in args.jdxs:
        if os.path.isfile(p):
            jdx_path.append(p)
        else:
            jdx_path.extend(
                os.path.join(p, f) for f in os.listdir(p) if f.endswith(".jdx")
            )

    import_jcamps(jdx_path, os.path.abspath(args.output), overwrite=args.force)


if is_main(__file__):
    main()
