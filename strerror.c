#include <error.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
	int err;

	if(argc < 2)
		return 0;

	if(sscanf(argv[1],"%d",&err) != 1)
			return 1;

	printf("Error %d = %s\n",err,strerror(err));

	return 0;
}
