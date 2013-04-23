#include <stdio.h>
#include <limits.h>
#include <errno.h>
#include <string.h>
#include <mpi.h> 


int main(int argc, char **argv)
{
  int rank;
  char outname[FILENAME_MAX], *envval;
  const char default_arg[] = "LD_LIBRARY_PATH", *arg;
  FILE *output = NULL;

  arg = default_arg;
  if(argc >= 2)
 	arg = argv[1];

  MPI_Init(&argc,&argv);
  
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);

  sprintf(outname,"%s.rank%d",arg,rank);
  
  output = fopen(outname,"w");
  if(output == NULL)
    {
      fprintf(stderr,"[node %d]: Could not open file \"%s\"\n",rank,outname);
      if(errno)
	{
	  fprintf(stderr,"[node %d]: Reason(%d): %s\n",rank,errno,strerror(errno));
	  MPI_Abort(MPI_COMM_WORLD,errno);
	}
    }

  fprintf(output,"%s=",arg);
  envval = getenv(arg);
  if(envval != NULL)
    fprintf(output,"%s",envval);
  fprintf(output,"\n");
  
  fclose(output);

  MPI_Finalize();
  
  return 0;
}
