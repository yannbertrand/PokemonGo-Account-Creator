#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

class Logger:
    def __init__(self, verbose):
        self.__verbose = verbose

    def log(self, message, no_verbose=False):
        if no_verbose or self.__verbose:
            print message

    def ask(self, message):
        notOk = True
        while notOk:
            answer = str(raw_input("> " + message + " (Y/n) "))
            if answer == "Y":
                notOk = False
            elif answer == "n":
                self.log("Quitting")
                sys.exit()

