#!/bin/sh

if [[ $1 == "" ]];then
    echo Usage: $0 \<target directory \>
    exit 1
fi

PROJDIR=$1
ORIGDIR=$(pwd)
DIRLIST=$(find . -type d -maxdepth 1)

for dir in $DIRLIST;do
    if [[ $dir == "." ]];then
	continue
    fi
    if [[ ! -d $dir/.git ]];then
	echo skipping $dir
	continue
    fi
    echo Sync\'ing $dir
    cd $dir
    REPODIR=$PROJDIR/${dir}.git
    if [[ ! -d $REPODIR ]];then
	cd $(dirname $REPODIR)
	git clone --bar $ORIGDIR/$dir || exit 42
	cd $ORIGDIR/$dir
    fi
    git push $REPODIR master || exit 42
    cd $ORIGDIR
done
