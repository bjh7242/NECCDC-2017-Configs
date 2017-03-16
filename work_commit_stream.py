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

number_of_teams = 2

# Change to a different repo we are working out of.
os.chdir("./remote_repo")

if not os.path.isfile("initialized"):
    # Change to a different repo we are working out of.

    for team in range(1, number_of_teams+1):
        # Create the branch for the team
        subprocess.call(['git', 'checkout', '--orphan', 'team-{0}-master'.format(team)])
        # Push it to the team's server/master branch and track it
        #subprocess.call([
        #    'git', 'remote', 'add', 'team-{}'.format(team), 'team git reference'
        #])

        commit = '5ced9f0ee2180d636225a1fd8563eea169312ac3'

        # Checkout the Initial Commit
        subprocess.call(['git', 'checkout', commit, '--', '.'])
        subprocess.call(['git', 'commit', '--reuse-message={}'.format(commit)])

        # Push and set the upstream
        #subprocess.call(['git', 'push', '--set-upstream',
        #    'team-{}/master'.format(team), 'team-{0}-master'.format(team)])

        subprocess.call(['git', 'push', '--set-upstream', 'origin', 'team-{0}-master'.format(team)])
        
    with open('initialized', 'w') as fo:
        fo.write(commit + '\n')

finished_commits = []

with open('initialized', 'r') as fr:
    last_stored_commit = fr.readlines()[-1].strip()

print last_stored_commit

last_commit = None

found_last_commit = False

new_commits = []

for commit in commit_list:
    if found_last_commit:
        new_commits.append(commit)

    if commit == last_stored_commit:
        found_last_commit = True

for commit in new_commits:
    for team in range(1, number_of_teams+1):
        subprocess.call(['git', 'checkout', 'team-{0}-master'.format(team)])
        subprocess.call(['git', 'pull'])
        subprocess.call(['git', 'checkout', commit, '--', '.'])
        subprocess.call(['git', 'commit', '--reuse-message={}'.format(commit)])
        subprocess.call(['git', 'push', '-f'])
        last_commit = commit

    with open('initialized', 'a') as fo:
        fo.write(last_commit + '\n')
    break
