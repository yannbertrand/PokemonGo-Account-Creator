#!/usr/bin/python
# -*- coding: utf-8 -*-

from email.utils import parseaddr
from pikapy import random_account
from pikapy.ptcexceptions import *

__all__ = [
    'concoct_email',
    'concoct_number',
    'create_ptc_account'
]

def __is_email_address(email):
    return '@' in parseaddr(email)[1]

def concoct_email(email):
    if __is_email_address(email):
        return email
    else:
        return email + "@gmail.com"

def concoct_number(number):
    if number < 1:
        return 1
    elif number > 100:
        return 100
    
    return number

def create_ptc_account(email):
    return random_account(email = email, email_tag = True)
