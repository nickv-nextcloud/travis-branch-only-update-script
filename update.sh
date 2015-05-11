#!/bin/bash
#
# Checkout and update the branch on all repos

echo "Checkout master"
echo "======================"
git checkout master

echo ""
echo "Delete existing branch"
echo "======================"
git branch -D update-travis-branches-only-setting

echo ""
echo "Checkout branch"
echo "======================"
git checkout -b update-travis-branches-only-setting

echo ""
echo "Update .travis.yml"
echo "======================"
python `dirname "$0"`/update.py

echo ""
echo "Add file to git status"
echo "======================"
git add .travis.yml

echo ""
echo "Commit branch"
echo "======================"
git commit -m "Update the branches.only setting in .travis.yml"

echo ""
echo "Push branch"
echo "======================"
git push origin update-travis-branches-only-setting
