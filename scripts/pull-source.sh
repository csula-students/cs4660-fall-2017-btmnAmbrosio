#! /bin/bash

git ls-remote --exit-code course&>/dev/null
if test $? != 0; then
    echo "Course remote doesn't exist. Setting course remote to 'git@github.com:csula/cs4660-fall-2017.git'"
    git remote add course git@github.com:csula/cs4660-fall-2017.git
fi

# Need to fetch the remote first prior to download
git fetch course

echo "Downloading $1 from course repository ..."
git checkout course/master -- cs4660/$1
echo "Redownloading test codes"
git checkout course/master -- cs4660/test
