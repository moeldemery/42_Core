/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_util_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 16:36:29 by meldemir          #+#    #+#             */
/*   Updated: 2025/12/19 16:36:30 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf_bonus.h"

void	ft_flag_parser(const char **str, t_flags *f)
{
	while (ft_strchr("+- #0", **str))
	{
		if (**str == '+')
			f->plus = 1;
		else if (**str == ' ')
			f->space = 1;
		else if (**str == '-')
			f->minus = 1;
		else if (**str == '#') 
			f->hash = 1;
		else if (**str == '0') 
			f->zero = 1;
		(*str)++;
	}
}

int	ft_print_char_bonus(int c, t_flags f)
{
	int		count;
	char	pad_char;

	pad_char = ' ';
	if (f.zero && !f.minus && f.padding == -1) 
		pad_char = '0';
	count = 0;
	if (!f.minus)
		while (count < f.width - 1)
			count += write(1, &pad_char, 1);
	count += write(1, &c, 1);
	if (f.minus)
		while (count < f.width)
			count += write(1, " ", 1);
	return (count);
}

int	ft_print_int_bonus(int n, t_flags f)
{
	int	count;

	count = 0;
	if (n >= 0 && f.plus)
		count += write(1, "+", 1);
	else if (n >= 0 && f.space)
		count += write(1, " ", 1);
	count += ft_putnbr_base(n, DEC);
	while (f.minus && count < f.width)
		count += write(1, " ", 1);
	return (count);
}

int	ft_print_u_int_bonus(unsigned int n, t_flags f)
{
	int		count;
	int		len;
	char	pad_char;

	pad_char = ' ';
	if (f.zero && !f.minus && f.padding == -1) 
		pad_char = '0';
	count = 0;
	len = ft_num_len_base(n, 10);
	while (!f.minus && count < (f.width - len))
		count += write(1, &pad_char, 1);
	count += ft_putnbr_base_unsigned(n, DEC);
	while (f.minus && count < f.width)
		count += write(1, " ", 1);
	return (count);
}

int	ft_print_add_b(unsigned long addr, t_flags f)
{
	int	len;
	int	count;

	if (!addr)
		return (ft_print_str_bonus("(nil)", f));
	len = ft_num_len_base(addr, 16) + 2;
	count = 0;
	while (!f.minus && count < (f.width - len))
		count += write(1, " ", 1);
	write(1, "0x", 2);
	count += ft_putnbr_base_unsigned(addr, HEXS) + 2;
	while (f.minus && count < f.width)
		count += write(1, " ", 1);
	return (count);
}
