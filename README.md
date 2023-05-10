# Overview

This repo contains a minimal way to reproduce an issue where
`subprocess.Popen.poll()` considers any subprocess which is traced to be
terminated.

# Instructions

1. Build the process `make`
2. In one terminal, run the script: `./popen.py`
3. Note the pid of the child ($PID)
4. In another terminal, attach a debugger to $PID, e.g. `lldb -p $PID`

# Expected behvaviour

`poll` continues to return None (the child process is still running).

# Actual behaviour

The script prints "The process has exited with status code: 0" (and continues
to do so forever, even if you detach the debugger).
