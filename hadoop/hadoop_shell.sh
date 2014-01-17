#!/bin/sh

echo Welcome to Hadoop Shell. 
echo To exit the shell, type exit and press enter.

while read -p "> " line;do
    if [[ $line == exit ]];then
	break
    fi
    hadoop fs -${line}
done
