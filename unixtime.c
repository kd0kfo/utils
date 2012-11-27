#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdio.h>
#include <getopt.h>

struct option long_opts[] = {
  {"help",0,NULL,'h'},
  {"format",1,NULL,'f'},
  {"usage",0,NULL,'h'},
  {NULL,0,NULL,0}
};
const char short_opts[] = "f:h";
static const char unixtime_default_format[] = "%d %B %Y  %H:%M";

void print_help()
{
  printf("unixtime -- Converts a unix time stamp to a human readable time and date\n");
  printf("Copyright 2011 David Coss, PhD\n");
  printf("This program comes with ABSOLUTELY NO WARRANTY and is released for use under the terms of the GNU Public License.\nFor details visit http://www.gnu.org/licenses/gpl-3.0.html\n\n");
  printf("Usage: unixtime [options] <unix time stamp>\n");
  printf("\nOptions:\n");
  printf("--format, -f\tSpecified format string, for details see help for strftime\n");
  printf("           \tDefault: \"%s\"\n",unixtime_default_format);
  printf("--help, -h\tThis help message\n");
  printf("--usage   \tSame as \"--help\"\n");

}

int main(int argc, char **argv)
{
  time_t the_time;
  int opt_flag;
  int retval = 0;
  const char *format = unixtime_default_format;
  const size_t output_size = 512;
  char output[output_size];
  struct tm time_struct;

  if(argc == 1)
    {
      print_help();
      exit(0);
    }

  while((opt_flag = getopt_long(argc,argv,short_opts,long_opts,NULL)) != -1)
    {
      switch(opt_flag)
	{
	case 'f':
	  format = optarg;
	  break;
	default:
	  fprintf(stderr,"Unknown flag: %c",opt_flag);
	  if(optarg != NULL)
	    fprintf(stderr," (%s)",optarg);
	  fprintf(stderr,"\nFor usage, run ./%s --usage\n",argv[0]);
	  exit(-1);
	  break;
	case 'h':case '?':
	  print_help();
	  exit(retval);
	  break;
	}
    }

  if(optind >= argc)
    {
      fprintf(stderr,"A unix time is needed.\n");
      exit(-1);
    }
  
  if(sscanf(argv[optind],"%lu",&the_time) != 1)
    {
      fprintf(stderr,"Could not interpret %s as a long integer.\n",argv[optind]);
      exit(-1);
    }

  memset(output,0,sizeof(char)*output_size);
  localtime_r(&the_time,&time_struct);
  strftime(output,output_size,format,&time_struct);
  printf("%s\n",output);
  
  return 0;
}
