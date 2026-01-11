/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 15:47:56 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/28 15:47:58 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static int	ft_digit_base_count(long long n)
{
	if (n > 9)
		return (1 + ft_digit_base_count(n / 10));
	else if (n < 0)
		return (ft_digit_base_count((unsigned)n * -1));
	else
		return (1);
}

void	ft_putnbr_fd(int n, int fd)
{
	char		str[11];
	long long	temp_n; 
	size_t		str_len;

	str_len = ft_digit_base_count(n);
	temp_n = n;
	ft_bzero(str, 11);
	if (temp_n < 0)
	{
		write(fd, "-", 1);
		temp_n = -temp_n;
	}
	if (temp_n == 0)
		str[0] = '0';
	while (temp_n > 0)
	{
		str[--str_len] = (temp_n % 10) + '0';
		temp_n = temp_n / 10;
	}
	write(fd, str, ft_digit_base_count(n));
}

/*
#include <stdlib.h>
#include <unistd.h>

int		main(int argc, const char *argv[])
{
	int		arg;

	alarm(5);
	if (argc == 1)
		return (0);
	else if ((arg = atoi(argv[1])) == 1)
		ft_putnbr(0);
	else if (arg == 2)
		ft_putnbr(5);
	else if (arg == 3)
		ft_putnbr(-5);
	else if (arg == 4)
		ft_putnbr(42);
	else if (arg == 5)
		ft_putnbr(-57);
	else if (arg == 6)
		ft_putnbr(164189);
	else if (arg == 7)
		ft_putnbr(-987441);
	else if (arg == 8)
		ft_putnbr(2147483647);
	else if (arg == 9)
		ft_putnbr(-2147483648LL);
	return (0);
}
*/