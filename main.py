#!/usr/bin/python
# -*- coding: utf-8 -*-

"""pokemongo-account-creator.py - Create Pokémon Go accounts programmatically"""

from logger import Logger
from parser import parser
from utils import *

try:
    args = parser.parse_args()

    logger = Logger(args.verbose)
    logger.log("Verbose mode activated")

    args.email = concoct_email(args.email)
    logger.log("Asking if email address is fine")
    logger.ask("Is `%s` your email address?" % args.email)
    logger.log("Email validated")

    args.number = concoct_number(args.number)
    logger.log("Asking if number of accounts is ok")
    logger.ask("Do you want to create %d accounts?" % args.number)
    logger.log("Number of accounts validated")

    logger.log(" ", True)
    logger.log("Creating %d account(s)" % args.number, True)
    logger.log("...", True)

    for i in range(args.number):
        account = create_ptc_account(args.email)

        logger.log("Created a new ptc account (%d of %d)" % i % args.number, True)
        logger.log(" - username: %s" % account[USERNAME])
        logger.log(" - password: %s" % account[PASSWORD])
        logger.log(" - email: %s" % account[EMAIL])
        logger.log("...", True)

        # ToDo - Validate the ToS

    logger.log("Successfully created %d accounts" % args.number, True)

except KeyboardInterrupt:
    logger.log("Quitting")