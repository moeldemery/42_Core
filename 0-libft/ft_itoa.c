/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 09:40:20 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/28 09:40:23 by meldemir         ###   ########.fr       */
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

char	*ft_itoa(int n)
{
	char		*str;
	size_t		str_len;
	long long	temp_n; 

	temp_n = n;
	str_len = ft_digit_base_count(n);
	if (temp_n < 0)
		str_len++;
	str = malloc (sizeof(char) * (str_len + 1));
	if (!str)
		return (NULL);
	str[str_len] = '\0';
	if (temp_n < 0)
	{
		str[0] = '-';
		temp_n = -temp_n;
	}
	if (temp_n == 0)
		str[0] = '0';
	while (temp_n > 0)
	{
		str[--str_len] = (temp_n % 10) + '0';
		temp_n = temp_n / 10;
	}
	return (str);
}

/*
#include <stdlib.h>
#include <unistd.h>

void	ft_print_result(char const *s)
{
	int		len;

	len = 0;
	while (s[len])
		len++;
	write(1, s, len);
}

int		main(int argc, const char *argv[])
{
	int		arg;

	alarm(5);
	if (argc == 1)
		return (0);
	else if ((arg = atoi(argv[1])) == 1)
	{
		char *res = ft_itoa(0);
		ft_print_result(res);
		free(res);
	}
	else if (arg == 2)
	{
		char *res = ft_itoa(9);
		ft_print_result(res);
		free(res);
	}
	else if (arg == 3)
	{
		char *res = ft_itoa(-9);
		ft_print_result(res);
		free(res);
	}
	else if (arg == 4)
	{
		char *res = ft_itoa(10);
		ft_print_result(res);
		free(res);
	}
	else if (arg == 5)
	{
		char *res = ft_itoa(-10);
		ft_print_result(res);
		free(res);
	}
	else if (arg == 6)
	{
		char *res = ft_itoa(8124);
		ft_print_result(res);
		free(res);
	}
	else if (arg == 7)
	{
		char *res = ft_itoa(-9874);
		ft_print_result(res);
		free(res);
	}
	else if (arg == 8)
	{
		char *res = ft_itoa(543000);
		ft_print_result(res);
		free(res);
	}
	else if (arg == 9)
	{
		char *res = ft_itoa(-2147483648LL);
		ft_print_result(res);
		free(res);
	}
	else if (arg == 10)
	{
		char *res = ft_itoa(2147483647);
		ft_print_result(res);
		free(res);
	}
	return (0);
}
    */