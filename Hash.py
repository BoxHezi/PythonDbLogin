#!/usr/bin/python

import hashlib


def encode(string):
    return string.encode('utf-8')


def encrypt(code):
    string = encode(str(code))
    return hashlib.md5(string).hexdigest()
