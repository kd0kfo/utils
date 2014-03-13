#!/bin/sh

DIR=$1

if [[ -z $DIR ]];then
	echo Directory Name Required
	exit 1;
fi

RETVAL=""
for lib in $DIR/*.jar;do
        RETVAL=$lib:$RETVAL
done

echo $RETVAL
