/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 15:46:23 by meldemir          #+#    #+#             */
/*   Updated: 2025/10/27 15:46:43 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf_bonus.h"

static int	ft_strchardiscrite(char *str)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	if (str[0] == '\0')
		return (0);
	while (str[i] != '\0')
	{
		while (str[j] != '\0')
		{
			if (str[i] == str[j] && i != j)
				return (0);
			j++;
		}
		i++;
	}
	return (1);
}

static int	ft_strisvalid(char *str)
{
	int	i;

	i = 0;
	if (str[0] == '\0')
		return (0);
	while (str[i] != '\0')
	{
		if (str[i] >= 'a' && str[i] <= 'z')
			i++;
		else if (str[i] >= 'A' && str[i] <= 'Z')
			i++;
		else if (str[i] >= '0' && str[i] <= '9')
			i++;
		else
			return (0);
	}
	return (1);
}

size_t	ft_putnbr_base(long long nbr, char *base)
{
	char	ch;
	size_t	counter;

	counter = 0;
	if (ft_strchardiscrite(base) && ft_strisvalid(base) && ft_strlen(base) > 1)
	{
		if (nbr < 0)
		{
			nbr = nbr * -1;
			write(1, "-", 1);
			counter++;
		}
		if (nbr >= (int)ft_strlen(base))
			counter += ft_putnbr_base(nbr / ft_strlen(base), base);
		ch = base[nbr % ft_strlen(base)];
		write(1, &ch, 1);
		counter++;
	}
	return (counter);
}

size_t	ft_putnbr_base_unsigned(unsigned long long nbr, char *base)
{
	char	ch;
	size_t	counter;

	counter = 0;
	if (ft_strchardiscrite(base) && ft_strisvalid(base) && ft_strlen(base) > 1)
	{
		if (nbr >= (unsigned long long)ft_strlen(base))
			counter += ft_putnbr_base_unsigned(nbr / ft_strlen(base), base);
		ch = base[nbr % ft_strlen(base)];
		write(1, &ch, 1);
		counter++;
	}
	return (counter);
}

int	ft_num_len_base(unsigned long long n, int base_len)
{
	int	len;

	len = 0;
	if (n == 0)
		return (1);
	while (n != 0)
	{
		len++;
		n /= base_len;
	}
	return (len);
}
