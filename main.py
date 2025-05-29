from secret import *

output_code = int(input())

if output_code == 1:
    raise OSError("Run witch admin privilages!")
else:
    bsod_anyway(output_code)
