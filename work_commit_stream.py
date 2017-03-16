"""
To reset the first commit on a branch -
    git update-ref -d HEAD

# Checkout the working tree of a specific commit
    git checkout 5ced9f0ee2180d636225a1fd8563eea169312ac3 -- .

# Use the commit message of a specific commit
    git commit --reuse-message=5ced9f0ee2180d636225a1fd8563eea169312ac3


"""

__author__ = "ryan@rypeck.com"

import os
import subprocess
import sys

commit_list = []

with open('commit_stream', 'r') as fo:
    for line in fo.readlines():
        commit_list.append(line.strip())

for commit in commit_list:
    subprocess.call(['git', 'pull'])
    subprocess.call(['git', 'checkout', commit, '--', '.'])
    subprocess.call(['git', 'commit', '--reuse-message={}'.format(commit)])
    subprocess.call(['git', 'push', '-f'])
