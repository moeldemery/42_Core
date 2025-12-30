#include "ft_printf_bonus.h"
#include<stdio.h>
#include <stdlib.h>
#include <limits.h>

int main() {

	


	ft_printf("i am % +c \n", 'a');
	   printf("i am % +c \n", 'a');

	   ft_printf("i am % ++c \n", 'b');
	   printf("i am % ++c \n", 'b');

	ft_printf("i am %+ + c \n", 'c');
	   printf("i am %+ + c \n", 'c');

	ft_printf("i am %+ + c \n", 'd');
	   printf("i am %+ + c \n", 'd');

	ft_printf("welcome and %  s \n", "hi world");
	   printf("welcome and %  s \n", "hi world");

	ft_printf("%d\n", printf("welcome and %+ +s \n", NULL));
	   printf("%d\n", printf("welcome and %+ +s \n", NULL));

	ft_printf("%5%");
	   printf("%5%");
	ft_printf("%-5%");
	   printf("%-5%");
	ft_printf("%-05%");
	   printf("%-05%");
	ft_printf("%-x", 42);
	ft_printf("%.c", 'a');
	ft_printf("%-c", 'a');
	ft_printf("%-s", "hello");
	ft_printf("%-s", NULL);
	ft_printf("%23s", NULL);
	ft_printf("%.s", NULL);
	ft_printf("%32s", "abc");
	ft_printf("%16s", "nark nark");
	ft_printf("%5s", "goes over");
	ft_printf("%-32s", "abc");
	ft_printf("%-16s", "nark nark");
	ft_printf("%-5s", "goes over");
	ft_printf("%.7s", "hello");
	ft_printf("%.3s", "hello");
	ft_printf("%.s", "hello");

	return 0;
}
