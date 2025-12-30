/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_util_b_bonus.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 11:52:04 by meldemir          #+#    #+#             */
/*   Updated: 2025/12/22 11:52:06 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf_bonus.h"

int	ft_print_str_bonus(char *s, t_flags f)
{
	int	len;
	int	count;
	int	i;

	count = 0;
	if (!s)
		s = "(null)";
	len = ft_strlen(s);
	if (f.padding >= 0 && f.padding < len)
		len = f.padding;
	i = -1;
	while (!f.minus && ++i < (f.width - len))
		count += write(1, " ", 1);
	count += write(1, s, len);
	i = -1;
	while (f.minus && ++i < (f.width - len))
		count += write(1, " ", 1);
	return (count);
}

int	ft_print_hex_bonus(unsigned int n, char type, t_flags f)
{
	int	count;
	int	len;

	len = ft_num_len_base(n, 16);
	if (f.hash && n != 0)
		len += 2;
	count = 0;
	while (!f.minus && count < (f.width - len))
		count += write(1, " ", 1);
	if (f.hash && n != 0)
	{
		if (type == 'x')
			count += write(1, "0x", 2);
		else if (type == 'X')
			count += write(1, "0X", 2);
	}
	if (type == 'x')
		count += ft_putnbr_base(n, HEXS);
	else 
		count += ft_putnbr_base(n, HEX);
	while (f.minus && count < f.width)
		count += write(1, " ", 1);
	return (count);
}

int	ft_print_percent_bonus(t_flags f)
{
	int	count;

	count = 0;
	if (!f.minus)
		while (count < f.width - 1)
			count += write(1, " ", 1);
	count += write(1, "%", 1);
	if (f.minus)
		while (count < f.width)
			count += write(1, " ", 1);
	return (count);
}
