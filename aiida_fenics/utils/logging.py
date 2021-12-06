# -*- coding: utf-8 -*-
"""Utilities to deal with logging."""
import contextlib
import os
import sys


@contextlib.contextmanager
def suppress_output():
    """Suppress all output written to ``sys.stdout`` and ``sys.stderr`` by redirecting it to ``os.devnull``."""
    with open(os.devnull, 'wb') as devnull:
        try:
            stderr = os.dup(sys.stderr.fileno())
            stdout = os.dup(sys.stdout.fileno())
            os.dup2(devnull.fileno(), sys.stderr.fileno())
            os.dup2(devnull.fileno(), sys.stdout.fileno())
            yield
        finally:
            os.dup2(stderr, sys.stderr.fileno())
            os.dup2(stdout, sys.stdout.fileno())
