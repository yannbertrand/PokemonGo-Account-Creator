#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Create some Pokémon Go accounts')
parser.add_argument('email', type=str, help='a gmail adress')
parser.add_argument('latitude', type=float,
                    help='the latitude the account uses to join the game')
parser.add_argument('longitude', type=float,
                    help='the longitude the account uses to join the game')
parser.add_argument('-n', '--number', type=int, default=100,
                    help='number of accounts to create')
parser.add_argument('-v', '--verbose', action="store_true",
                    help='increase output verbosity')
