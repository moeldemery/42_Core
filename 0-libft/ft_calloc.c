/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 23:45:22 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/27 23:45:24 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*s;
	size_t	max;

	max = ~((size_t)0);
	if (size == 0 || nmemb == 0)
	{
		s = malloc(0);
		if (!s)
			return (NULL);
		return (s);
	}
	if ((max / size < nmemb)) 
		return (NULL);
	s = (void *)malloc(nmemb * size);
	if (!s)
		return (NULL);
	ft_bzero(s, nmemb * size);
	return (s);
}

/*
#include <stdlib.h>
#include <unistd.h>

int		main(int argc, const char *argv[])
{
	char	*str;

	alarm(5);
	if (argc == 1)
		return (0);
	else if (atoi(argv[1]) == 1)
	{
		str = (char *)ft_calloc(30, 1);
		if (!str)
			write(1, "NULL", 4);
		else
			write(1, str, 30);
	}
	return (0);
}
	*/