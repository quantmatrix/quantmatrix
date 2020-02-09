# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


from cmd import Cmd
import os
import sys


class Cli(Cmd):
    def __init(self):
        Cmd.__init__(self)
        self.prompt = "quantmatrix"

    def do_hello(self, line):
        print("hello", line)


if __name__ == "__main__":
    cli = Cli()
    cli.cmdloop()
