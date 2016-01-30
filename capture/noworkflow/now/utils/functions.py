# Copyright (c) 2016 Universidade Federal Fluminense (UFF)
# Copyright (c) 2016 Polytechnic Institute of New York University.
# This file is part of noWorkflow.
# Please, consult the license terms in the LICENSE file.
"""Define utility functions"""
from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

import inspect
import os
import types

from datetime import datetime
from pkg_resources import resource_string, resource_listdir, resource_isdir
from textwrap import dedent

from .cross_version import cross_compile
from .io import redirect_output


MODULE = __name__
MODULE = MODULE[:MODULE.rfind('.')]
MODULE = MODULE[:MODULE.rfind('.')]


def wrap(string, initial="  ", other="\n  "):
    """Re-indent indented text"""
    return initial + other.join(dedent(string).split('\n'))


def resource(filename, encoding=None):
    """Access resource content via setuptools"""
    content = resource_string(MODULE, filename)
    if encoding:
        return content.decode(encoding=encoding)
    return content


def resource_ls(path):
    """Access resource directory via setuptools"""
    return resource_listdir(MODULE, path)


def resource_is_dir(path):
    """Access resource directory via setuptools"""
    return resource_isdir(MODULE, path)


def abstract():
    """Raise abstract Exception"""
    frame = inspect.currentframe().f_back
    name = frame.f_code.co_name
    raise Exception("Abstract method: {}".format(name))


def timestamp(time):
    if not time:
        return -1
    epoch = datetime(1970,1,1)
    return (time - epoch).total_seconds()


def prolog_repr(var):
    """Return repr from var without string prefix"""
    result = repr(var)
    if result[1] in ('"', "'"):
        result = result[1:]
    return result