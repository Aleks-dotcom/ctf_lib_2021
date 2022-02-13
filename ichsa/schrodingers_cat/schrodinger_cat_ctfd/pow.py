#!/usr/bin/env python

import re
import hashlib
import string



def unhash(remote_out):
    REGEX = "(_i_hav3_done_my_work_\w+)\) will return (\w+)"
    m = re.search(REGEX, remote_out)
    done_work = m.group(1)
    hash_val = m.group(2)
    found = False
    for i in string.ascii_letters:
        for j in string.ascii_letters:
            for k in string.ascii_letters:
                for l in string.ascii_letters:
                    
                    val = i + j + k + l
                    temp_hash = hashlib.sha256(bytes(val + done_work,'utf-8')).hexdigest()
                    if hash_val == temp_hash:
                        found = True
                        return ','.join(val)
    print("did not found :(")
    return ""

pow = unhash(__pow_line__)


