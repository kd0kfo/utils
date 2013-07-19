#!/bin/sh

perl -pe 's/\e\[?.*?[\@-~]//g' < /dev/stdin

