#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(int argc, char **argv)
{ 
  size_t the_size = 42, counter;
  double *massive_array = NULL;


  struct timespec tim, tim2;

  printf("Size of double: %d\n",sizeof(double));
  printf("Size of char: %d\n",sizeof(char));

  the_size = 1 << 27;
  the_size *= 4;
  printf("Allocating: %lu doubles\n",the_size);

  massive_array = (double*)malloc(the_size*sizeof(double));
  if(massive_array == NULL)
  {
    fprintf(stderr,"Could not allocate %lu doubles\n");
    if(errno)
    {
        fprintf(stderr,"Reason: %s\n",strerror(errno));
        exit(errno);  
    }
    exit(1);
  }

  massive_array[0] = 1;
  massive_array[1] = 3.14159;
  massive_array[2] = massive_array[0] + massive_array[1];

  printf("2: %f\n",massive_array[2]);

#if 0
  counter=0;
  for(;counter<the_size;counter++)
		  massive_array[counter] = massive_array[counter-1] + 123.45;
#endif

  printf("3: %f\n",massive_array[the_size-1]);
  tim.tv_sec = 300;   
  tim.tv_nsec = 0;

  printf("Sleeping: %d s...\n",tim.tv_sec);

  if(nanosleep(&tim , &tim2) < 0 )
    {
      free(massive_array);
      fprintf(stderr,"Could not sleep.\n");
      if(errno)
	{
	  fprintf(stderr,"Reason: %s\n",strerror(errno));
	  exit(errno);
	}
      exit(1);
    }
  
  free(massive_array);
  
  return 0;
}
