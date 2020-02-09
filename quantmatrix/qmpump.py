# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

import sys


def china_stock():
    pass


def main(args=None, options=None):
    if options is None:
        options = ClientOptions()

    options.realize(args, doc=__doc__)
    c = Controller(options)

    if options.args:
        c.onecmd(" ".join(options.args))
        sys.exit(c.exitstatus)

    if options.interactive:
        c.exec_cmdloop(args, options)
        sys.exit(0)  # exitstatus always 0 for interactive mode


if __name__ == "__main__":
    main()
