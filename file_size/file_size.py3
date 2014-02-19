#!/usr/bin/env python

import sys
import os

statinfo = os.stat(sys.argv[1])
print(statinfo.st_size)
