#! /bin/bash

git ls-remote --exit-code course&>/dev/null
if test $? != 0; then
    echo "Course remote doesn't exist. Setting course remote to 'git@github.com:csula/cs4660-fall-2017.git'"
    git remote add course git@github.com:csula/cs4660-fall-2017.git
fi

echo "Downloading $1 from course repository ..."
git checkout course/master -- cs4660/$1
