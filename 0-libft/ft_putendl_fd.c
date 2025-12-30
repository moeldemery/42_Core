/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 15:41:38 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/28 15:41:40 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_putendl_fd(char *s, int fd)
{
	ft_putstr_fd(s, fd);
	write(fd, "\n", 1);
}
/*
#include <stdlib.h>
#include <unistd.h>
#include "../../../libft.h"

int		main(int argc, const char *argv[])
{
	int		arg;

	alarm(5);
	if (argc == 1)
		return (0);
	else if ((arg = atoi(argv[1])) == 1)
		ft_putendl_fd("lorem ipsum dolor sit amet", 2);
	else if (arg == 2)
		ft_putendl_fd("  lorem\nipsum\rdolor\tsit amet  ", 1);
	else if (arg == 3)
		ft_putendl_fd("", 2);
	else if (arg == 4)
		ft_putendl_fd("lorem ipsum do\0lor sit amet", 1);
	return (0);
}
	*/