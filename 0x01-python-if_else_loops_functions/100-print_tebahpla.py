#!/usr/bin/python3
print(
    ''.join(
        '{}'.format(chr(122 - i).upper() if i % 2 != 0 else chr(122 - i))
        for i in range(26)
     ), end=""
)
