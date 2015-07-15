#!/usr/bin/env python

import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    if words[4] == '-9999':
        pass
#    print words
    else:
        print words[0],(float(words[4])/10)
