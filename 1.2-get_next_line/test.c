#include <stdio.h>
#include "get_next_line.h"
#include <fcntl.h>

int main()
{
    int fd;

    fd = open("text.txt", O_RDONLY);

    printf("\nline1 :%s$\n",get_next_line(fd));
    printf("\nline2 :%s$\n",get_next_line(fd));
    printf("\nline3 :%s$\n",get_next_line(fd));
    printf("\nline4 :%s\n",get_next_line(fd));
    printf("\nline4 :%s\n",get_next_line(fd));
}