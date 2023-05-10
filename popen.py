#!/usr/bin/env python3

import subprocess
import time

p = subprocess.Popen('./a.out', stdin=subprocess.PIPE, stdout=subprocess.PIPE)

print(f"Child PID: {p.pid}")

while True:
    # Faff with stdin/stdout?
    print('.')
    if p.poll() is not None:
        print(f"The process exittted with status code: {p.poll()}")
    time.sleep(2)

# vim: sw=4
