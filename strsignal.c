#include <error.h>
#include <stdio.h>
#include <string.h>
#include <signal.h>

int main(int argc, char **argv)
{
	int err;

	if(argc < 2)
		return 0;

	if(sscanf(argv[1],"%d",&err) != 1)
			return 1;

	printf("Signal %d = %s\n",err,strsignal(err));

	return 0;
}
