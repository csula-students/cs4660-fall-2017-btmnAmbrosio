#! /bin/bash

SUBJECT=$1
# Make sure the directory is at the repository root
cd $( dirname $0 ) && cd ..

# Check if the remote is already set
git ls-remote --exit-code course&>/dev/null
if test $? != 0; then
    echo "Course remote doesn't exist. Setting course remote to 'https://github.com/csula/cs4660-fall-2017.git'"
    git remote add course https://github.com/csula/cs4660-fall-2017.git
fi

# Need to fetch the remote first prior to download
git fetch course

echo "Downloading $SUBJECT from course repository ..."
git checkout course/master -- cs4660/$SUBJECT
echo "Redownloading test codes"
git checkout course/master -- cs4660/test

