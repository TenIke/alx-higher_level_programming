#!/usr/bin/python3
"""Defines an object attribute lookup function"""

def lookup(obj):
    """Return a list of object's available attributes"""
    return(dir(obj))
