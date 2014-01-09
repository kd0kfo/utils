#!/bin/bash

function ackbar() {
		local name="$0"
		local code="$1"
		echo ${name} errored out line with code ${code}
		echo Line Stack: ${BASH_LINENO[*]}
		exit $code
}

trap 'ackbar $?' ERR

