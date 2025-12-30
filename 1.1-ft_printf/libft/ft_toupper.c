/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 16:40:35 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/24 16:40:39 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_toupper(int inpt)
{
	if ((inpt >= 97 && inpt <= 122))
	{
		inpt = inpt - 32;
	}
	return (inpt);
}

/*
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>

int		main(int argc, const char *argv[])
{
	int		i;
	int		c;
	int		arg;

	alarm(5);
	if (argc == 1)
		return (0);
	else if ((arg = atoi(argv[1])) == 1)
	{
		i = 0;
		while (i <= 47)
		{
			c = ft_toupper(i);
			write(1, &c, 1);
			i++;
		}
	}
	else if (arg == 2)
	{
		i = '0';
		while (i <= '9')
		{
			c = ft_toupper(i);
			write(1, &c, 1);
			i++;
		}
	}
	else if (arg == 3)
	{
		i = 58;
		while (i <= 64)
		{
			c = ft_toupper(i);
			write(1, &c, 1);
			i++;
		}
	}
	else if (arg == 4)
	{
		i = 'A';
		while (i <= 'Z')
		{
			c = ft_toupper(i);
			write(1, &c, 1);
			i++;
		}
	}
	else if (arg == 5)
	{
		i = 91;
		while (i <= 96)
		{
			c = ft_toupper(i);
			write(1, &c, 1);
			i++;
		}
	}
	else if (arg == 6)
	{
		i = 'a';
		while (i <= 'z')
		{
			c = ft_toupper(i);
			write(1, &c, 1);
			i++;
		}
	}
	else if (arg == 7)
	{
		i = 123;
		while (i <= 127)
		{
			c = ft_toupper(i);
			write(1, &c, 1);
			i++;
		}
	}
	return (0);
}
*/