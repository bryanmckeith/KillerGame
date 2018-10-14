#!/usr/bin/python
# -*- coding: latin-1 -*-

import hashlib
import re
from random import randint

def get_code(string1, string2, string3, string4):
    """ Out of 4 strings, return random hexa code on 8 digits """

    """ Skip special characters and whitespaces """
    string1_formatted = re.sub(r'[^a-zA-Z0-9_]', "", string1)
    string2_formatted = re.sub(r'[^a-zA-Z0-9_]', "", string2)
    string3_formatted = (re.sub(r'[^a-zA-Z0-9_]', "", string3)).encode('utf-8')
    string4_formatted = (re.sub(r'[^a-zA-Z0-9_]', "", string4)).encode('utf-8')

    string3_hash = str( int( hashlib.sha1(string3_formatted).hexdigest(), \
                             16) \
                        % 10**3)
    string4_hash = str( int( hashlib.sha1(string4_formatted).hexdigest(), \
                             16) \
                        % 10**3)
    
    code = string3_hash \
        + string1_formatted[randint(0,len(string1_formatted)-1)] \
        + string4_hash \
        + string2_formatted[randint(0,len(string2_formatted)-1)]

    return code
