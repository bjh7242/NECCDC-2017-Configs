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

git_servers_urls = {
    'black': 'git@github.com:bjh7242/NECCDC-2017-Configs.git',
}

# Change to a different repo we are working out of.
os.chdir("./remote_repo")

if not os.path.isfile("initialized"):
    # Change to a different repo we are working out of.

    for team, url in git_servers_urls.iteritems():
        # Create the branch for the team
        subprocess.call(['git', 'checkout', '--orphan',
            'team-{0}-master'.format(team)])

        print "Team {0} URL is {1}".format(team, url)

        # Push it to the team's server/master branch and track it
        subprocess.call([
            'git', 'remote', 'add', 'team-{}'.format(team), url
        ])

        commit = '5ced9f0ee2180d636225a1fd8563eea169312ac3'

        # Checkout the Initial Commit
        subprocess.call(['git', 'checkout', commit, '--', '.'])
        subprocess.call(['git', 'commit', '--reuse-message={}'.format(commit)])
        subprocess.call(['git', 'commit', '--amend', '--no-edit', '--date=now'])

        # Push and set the upstream
        subprocess.call([
            'git', 'push', '--set-upstream', 'team-{}'.format(team),
            'team-{}-master:master_test_test'.format(team)])
                            # This needs to be set to master for prod


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
    for team in git_servers_urls.keys():
        subprocess.call(['git', 'checkout', 'team-{0}-master'.format(team)])
        subprocess.call(['git', 'pull'])
        subprocess.call(['git', 'checkout', commit, '--', '.'])
        subprocess.call(['git', 'commit', '--reuse-message={}'.format(commit)])
        subprocess.call(['git', 'commit', '--amend', '--no-edit', '--date=now'])
       
        # Force push.
        subprocess.call(
                ['git', 'push', '-f', 'team-{0}'.format(team), 'HEAD:master_test_test']
        )
        last_commit = commit

    with open('initialized', 'a') as fo:
        fo.write(last_commit + '\n')

    # Only do one commit at a time.
    break
