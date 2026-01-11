/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 16:37:18 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/24 16:37:20 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_bzero(void *s, size_t n)
{
	size_t	i;

	i = 0;
	while (i < n)
		*((char *) s + i++) = '\0';
}

/*
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int		main(int argc, const char *argv[])
{
	void	*mem;

	alarm(5);
	if (argc == 1 || !(mem = malloc(sizeof(*mem) * 5)))
		return (0);
	if (atoi(argv[1]) == 1)
	{
		memset(mem, 'a', 5);
		ft_bzero(mem, 5);
		write(1, mem, 5);
	}
	else if (atoi(argv[1]) == 2)
	{
		memset(mem, 'b', 5);
		ft_bzero(mem, 0);
		write(1, mem, 5);
	}
	return (0);
}

*/