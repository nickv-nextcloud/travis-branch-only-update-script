from __future__ import print_function

__author__ = 'nickv'

travis_file_name = '.travis.yml'

new_stable_branch_line = '    - CORE_BRANCH=stable8.2\n'

old_stable_branch_line = '    - CORE_BRANCH=master\n'

travis_file = open(travis_file_name, 'r')
lines = travis_file.readlines()
travis_file.close()

travis_file = open(travis_file_name, 'w')
updatedEnvGlobalCoreBranch = False

for line in lines:
    print(line)
    print(line == old_stable_branch_line)

    if line == old_stable_branch_line:
        travis_file.write(new_stable_branch_line)
        updatedEnvGlobalCoreBranch = True
    else:
        travis_file.write(line)

if lines[-1][-1] != '\n':
    travis_file.write('\n')

travis_file.close()

if updatedEnvGlobalCoreBranch:
    print('Updated branches.only in .travis.yml')
else:
    print('Could not find env.global.CORE_BRANCH in .travis.yml')
    exit(1)
