# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-

import cmd


class LSBInitExitStatuses:
    SUCCESS = 0
    GENERIC = 1
    INVALID_ARGS = 2
    UNIMPLEMENTED_FEATURE = 3
    INSUFFICIENT_PRIVILEGES = 4
    NOT_INSTALLED = 5
    NOT_RUNNING = 7


class Cli(cmd.Cmd):

    def __init__(self,
                 completekey: str,
                 stdin=None,
                 stdout=None
                 ):
        self.prompt = "Quantmatrix >"
        self.intro = "Welcome to Quantmatrix!"
        self.vocab = ['help']

        cmd.Cmd.__init__(self, completekey, stdin, stdout)

    def default(self, line):
        """
        undefined command
        :param line:
        :return:
        """
        pass


class Controller(cmd.Cmd):

    def __init__(self,
                 options,
                 completekey='tab',
                 stdin=None,
                 stdout=None
                 ):
        self.options = options
        self.prompt = self.options.prompt + '> '
        self.options.plugins = []
        self.vocab = ['help']
        self._complete_info = None
        self.exitstatus = LSBInitExitStatuses.SUCCESS
        cmd.Cmd.__init__(self, completekey, stdin, stdout)
        for name, factory, kwargs in self.options.plugin_factories:
            plugin = factory(self, **kwargs)
            for a in dir(plugin):
                if a.startswith('do_') and callable(getattr(plugin, a)):
                    self.vocab.append(a[3:])
            self.options.plugins.append(plugin)
            plugin.name = name
