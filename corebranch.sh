#!/bin/bash
#
# Checkout and update the branch on all repos

set -e

CORE_BRANCH=stable8.2

echo "Fetch $CORE_BRANCH"
echo "======================"
git fetch origin $CORE_BRANCH

set +e

echo ""
echo "Delete existing $CORE_BRANCH"
echo "======================"
git branch -D $CORE_BRANCH

set -e

echo "Checkout $CORE_BRANCH"
echo "======================"
git checkout -b $CORE_BRANCH

set +e

echo ""
echo "Delete existing branch"
echo "======================"
git branch -D update-travis-core-branch

set -e

echo ""
echo "Checkout branch"
echo "======================"
git checkout -b update-travis-core-branch

echo ""
echo "Reset branch"
echo "======================"
git reset --hard origin/$CORE_BRANCH

echo ""
echo "Update .travis.yml"
echo "======================"
python `dirname "$0"`/corebranch.py

echo ""
echo "Add file to git status"
echo "======================"
git add .travis.yml

echo ""
echo "Commit branch"
echo "======================"
git commit -m "Update the env.global.CORE_BRANCH setting in .travis.yml"

echo ""
echo "Push branch"
echo "======================"
git push origin update-travis-core-branch

