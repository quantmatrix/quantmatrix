# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

import sys
import warnings


class Options:
    stderr = sys.stderr
    stdout = sys.stdout
    exit = sys.exit
    warnings = warnings

    uid = gid = None

    progname = sys.argv[0]
    configfile = None
    schemadir = None
    configroot = None
    here = None
