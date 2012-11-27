#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>

#define GPM_BUFSZ 200

/* Return physical memory size in kB */
size_t getphysmem() {
	FILE *meminfo;
	char *buf;
	unsigned long physmem;
	int len;
	int ret;

	buf = (char *)malloc(GPM_BUFSZ);
	if (NULL == buf) {
		perror(NULL);
		return -1;
	}

	meminfo = fopen ("/proc/meminfo", "r");
	if (NULL == meminfo) {
		perror(NULL);
		free(buf);
		return -1;
	}

	while (buf == fgets(buf, GPM_BUFSZ, meminfo)) {
		ret = strncmp(buf, "MemTotal:", 9);
		if (ret == 0) {
			ret = sscanf(buf, "%*s %lu %*s", &physmem);
			if (ret == 1) {
				free(buf);
				fclose(meminfo);
				return physmem;
			}
		}
	}
	return -1;
}

int main(int argc, char *argv[]) {

	pid_t mypid;
	pid_t mypgid;
	pid_t ppid;
	size_t pgsize;
	size_t memsize;
	long pagesize;
	long count;
	long ppmb;
	void *mem;
	size_t limit;

	int opt;

	limit = 71000;

	while((opt = getopt(argc,argv,"l:")) != -1)
	{
		switch(opt)
		{
			case 'l':
				if(sscanf(optarg,"%lu",&limit) != 1)
				{
					fprintf(stderr,"Invalid value for limit: \"%s\"\nExpected integer.\n",optarg);
					exit(1);
				}
				break;
			default:
				fprintf(stderr,"Unknown argument '%c'\n",opt);
				exit(1);
				break;
		}
	}

	pagesize=sysconf(_SC_PAGESIZE);
	mypid=getpid();
	ppid = getppid();
	mypgid=getpgid(mypid);
	memsize=getphysmem();

	ppmb = 1024 * 1024 / pagesize;

	if (memsize == -1)
		memsize = 666;

	fprintf(stdout, "master --  "
			"limit: %lu\n"
		"pid: %8lu  pgid: %8lu  ppid: %8lu\n"
		"           memsize: %10lu  pagesz: %7li\n",
		mypid, mypgid, ppid, memsize, pagesize);
	fflush(stdout);

	for (count=1; mem=calloc(1, pagesize); count++) {
		if (0 == count % ( 10 * ppmb))
			fprintf(stdout, "%12li ", count / ppmb);
		if (0 == count % (5 * 10 * ppmb))
			fprintf(stdout, "\n");
		if (0 == count % (5 * 5 * 10 * ppmb))
			fflush(stdout);

		if (count >= limit*ppmb)
		{
			fprintf(stdout,"Reached limit of %lu pages\n",limit);
			fflush(stdout);
			break;
		}

	}

	fprintf(stdout, "\n");
	fflush(stdout);

	if (mem == NULL) {
		perror(NULL);
		fprintf(stderr, "calloc failed - exit!\n");
		exit (-1);
	}

	return 0;
}
