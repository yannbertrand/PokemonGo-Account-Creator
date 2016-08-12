#!/usr/bin/python
# -*- coding: utf-8 -*-

"""ptc-creator.py - Create multiple PTC accounts using file."""

from pikapy import *
import sys

def create_ptc_account(username, password, email):
  account_info = random_account(username, password, email)
  print('Created new ptc account {}'.format(account_info[USERNAME]))

with open(str(sys.argv[1])) as f:
  credentials = [x.strip().split(':') for x in f.readlines()]

for username, password, email in credentials:
  create_ptc_account(username, password, email)
