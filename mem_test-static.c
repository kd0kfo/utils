#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(int argc, char **argv)
{ 
  size_t the_size = 134217728, counter;
  static double massive_array[134217728];

  struct timespec tim, tim2;

  printf("Size of double: %d\n",sizeof(double));
  printf("Size of char: %d\n",sizeof(char));

  printf("I have a static array of : %lu doubles\n",the_size);

  
  massive_array[0] = 1;
  massive_array[1] = 3.14159;
  massive_array[2] = massive_array[0] + massive_array[1];

  printf("2: %f\n",massive_array[2]);

  massive_array[0] = 42.0;
  counter = 1;
  for(;counter<the_size;counter++)
		  massive_array[counter] = massive_array[counter-1] + 123.45;

  printf("3: %f\n",massive_array[the_size-1]);

#if 1
  tim.tv_sec = 300;   
  tim.tv_nsec = 0;

  printf("Sleeping: %d s...\n",tim.tv_sec);

  if(nanosleep(&tim , &tim2) < 0 )
    {
      fprintf(stderr,"Could not sleep.\n");
      if(errno)
	{
	  fprintf(stderr,"Reason: %s\n",strerror(errno));
	  exit(errno);
	}
      exit(1);
    }
#endif 
  return 0;
}
