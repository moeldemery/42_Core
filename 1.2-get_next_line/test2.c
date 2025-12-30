#include <stdio.h>
#include "get_next_line_bonus.h"
#include <fcntl.h>

int main()
{
    int fd;
    int fd2;
    fd = open("text.txt", O_RDONLY);
    fd2 = open("text copy.txt", O_RDONLY);

    printf("fd1 = %d, fd2 = %d\n", fd, fd2);
    printf("\nline1A :%s$\n",get_next_line(fd));
    printf("\nline1B :%s$\n",get_next_line(fd2));
    printf("\nline2A :%s$\n",get_next_line(fd));
    printf("\nline2B :%s\n",get_next_line(fd2));

}