from __future__ import print_function

__author__ = 'nickv'

travis_file_name = '.travis.yml'

new_stable_branch_line = '/^stable\d+(\.\d+)?$/'

old_stable_branch_lines = {
    'stable4',
    'stable4.5',
    'stable5',
    'stable6',
    'stable7',
    'stable8',
    '/^stable\d*$/'
}


def is_stable_branch_line(line):
    """

    :param line: string
    :return: bool
    """

    return line[:6] == '    - ' and (line[6:-1] == new_stable_branch_line or line[6:-1] in old_stable_branch_lines)


travis_file = open(travis_file_name, 'r')
lines = travis_file.readlines()
travis_file.close()

travis_file = open(travis_file_name, 'w')

foundBranches = False
foundBranchesOnly = False
updatedBranchesOnly = False

for line in lines:
    if foundBranchesOnly and (line == '' or line[:6] != '    - '):
        travis_file.write('    - ' + new_stable_branch_line + '\n')
        updatedBranchesOnly = True
        foundBranchesOnly = False

    if line == 'branches:\n':
        foundBranches = True
    elif foundBranches and line == '  only:\n':
        foundBranchesOnly = True

    if not foundBranchesOnly or not is_stable_branch_line(line):
        travis_file.write(line)

if lines[-1][-1] != '\n':
    travis_file.write('\n')

travis_file.close()

if updatedBranchesOnly:
    print('Updated branches.only in .travis.yml')
else:
    print('Could not find branches.only in .travis.yml')
    exit(1)
