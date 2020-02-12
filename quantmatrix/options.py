# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

import sys
import warnings
from typing import TextIO


class Options:
    stderr: TextIO = sys.stderr
    stdout: TextIO = sys.stdout
    exit = sys.exit
    warnings = warnings

    uid = gid = None

    progname = sys.argv[0]
    configfile = None
    schemadir = None
    configroot = None
    here = None


class CliOptions(Options):
    pass
