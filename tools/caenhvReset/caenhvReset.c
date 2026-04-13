#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/ioctl.h>

int main(int argc, char **argv)
{
  const char* usage="usage:  caenhv_reset [--hard] [--soft] device\n";
  
  const int softReset=2e5; // 200 milliseconds
  const int hardReset=1e6; // 1 second

  if (argc!=3) {
      fprintf(stderr,usage);
      exit(1);
  }

  int hard;
  if      (strcmp(argv[1],"--soft")==0) hard=0;
  else if (strcmp(argv[1],"--hard")==0) hard=1;
  else {
      fprintf(stderr,usage);
      fprintf(stderr,"One of --hard/--soft is required.\n");
      exit(1);
  }

  const char* device=argv[2];
  const int fd = open(device,O_RDWR | O_NOCTTY);
  const int flag = TIOCM_DTR;
  ioctl(fd,TIOCMBIS,&flag);
  if (hard) usleep(hardReset);
  else      usleep(softReset);
  ioctl(fd,TIOCMBIC,&flag);
  close(fd);
  exit(0);
}

