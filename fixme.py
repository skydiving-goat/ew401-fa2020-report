#!\usr\bin\env python3

import re

with open(r'report.tex','r') as f:
    for line in f:
        print(re.sub(r'\\u\w{4}','',line))
