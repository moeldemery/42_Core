/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 16:39:50 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/24 16:39:54 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlcpy(char *dest, const char *src, size_t size)
{
	size_t	i;
	size_t	cnt;

	i = 0;
	cnt = 0;
	while (src[cnt])
	{
		cnt++;
	}
	if (size > 0)
	{
		while (src[i] != '\0' && (i < (size - 1)))
		{
			dest[i] = src[i];
			i++;
		}
		dest[i] = '\0';
	}
	return (cnt);
}
/*
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


void	ft_print_result(int n)
{
	char c;

	if (n >= 10)
		ft_print_result(n / 10);
	c = n % 10 + '0';
	write (1, &c, 1);
}

int		main(int argc, const char *argv[])
{
	char	*dest;
	int		arg;

	alarm(5);
	if (!(dest = (char *)malloc(sizeof(*dest) * 15)) || argc == 1)
		return (0);
	memset(dest, 0, 15);
	memset(dest, 'r', 6);
	if ((arg = atoi(argv[1])) == 1)
	{
		ft_print_result(ft_strlcpy(dest, "lorem", 15));
		write(1, "\n", 1);
		write(1, dest, 15);
	}
	else if (atoi(argv[1]) == 2)
	{
		ft_print_result(ft_strlcpy(dest, "", 15));
		write(1, "\n", 1);
		write(1, dest, 15);
	}
	else if (atoi(argv[1]) == 3)
	{
		ft_print_result(ft_strlcpy(dest, "lorem ipsum", 3));
		write(1, "\n", 1);
		write(1, dest, 15);
	}
	else if (atoi(argv[1]) == 4)
	{
		ft_print_result(ft_strlcpy(dest, "lorem ipsum dolor sit amet", 15));
		write(1, "\n", 1);
		write(1, dest, 15);
	}
	else if (atoi(argv[1]) == 5)
	{
		ft_print_result(ft_strlcpy(dest, "lorem ipsum dolor sit amet", 0));
		write(1, "\n", 1);
		write(1, dest, 15);
	}
	return (0);
}
*/