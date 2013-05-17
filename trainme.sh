#!/bin/sh
#
# Requires pyTesseractTrainer, which is available under the GPLv3 at://code.google.com/p/pytesseracttrainer/
# 
# First command line argument is the id number for the tif file.
#
# Update LANG and FONT variables.
#
# PYTT is the directory in which pyTesseractTrainer-*.py is stored.
#

LANG=lang
FONT=font
PYTT=/path/to/script

if [[ $# == 0 ]];then
	echo Need ID number
	exit 1
fi

ID=$1
tesseract ${LANG}.${FONT}.exp${ID}.tif ${LANG}.${FONT}.exp${ID} -l ${FONT} batch.nochop makebox

python2.6 ${PYTT}/pyTesseractTrainer-1.03.py 

echo Continue?
read CONTINUE

if [[ $CONTINUE != "yes" && $CONTINUE != "y" ]];then
	echo Stopping
	exit
fi

tesseract ${LANG}.${FONT}.exp${ID}.tif ${LANG}.${FONT}.exp${ID} nobatch box.train

unicharset_extractor ${LANG}.${FONT}.exp*.box

shapeclustering -F font_properties -U unicharset ${LANG}.${FONT}.exp*.tr

mftraining -F font_properties -U unicharset -O ${LANG}.unicharset ${LANG}.${FONT}.exp*.tr

cntraining ${LANG}.${FONT}.exp*.tr

for i in shapetable normproto inttemp pffmtable;do 
	mv -f $i ${LANG}.$i
done

combine_tessdata ${LANG}.

