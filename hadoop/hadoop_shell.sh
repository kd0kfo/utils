#!/bin/sh

echo Welcome to Hadoop Shell. 
echo To exit the shell, type exit and press enter.

lastline=""
while read -p "> " line;do
	case $line in
    exit)
			break
			;;
	last)
			echo $lastline
			continue
			;;	
	esac
    hadoop fs -${line}
	lastline=$line
done
