/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ftprintf.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 13:40:17 by meldemir          #+#    #+#             */
/*   Updated: 2025/12/01 13:40:19 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int	ft_print_address(unsigned long addr)
{
	if (!addr)
		return (write (1, "(nil)", 5));
	write (1, "0x", 2);
	return (ft_putnbr_base_unsigned((unsigned long long)addr, HEXS) + 2);
}

int	ft_print_clasifier(const char *str, va_list args)
{
	if ((char)*str == '%')
		ft_putchar_fd('%', 1);
	else if ((char)*str == 'c')
		ft_putchar_fd(va_arg (args, int), 1);
	else if ((char)*str == 's')
		return (ft_putstr_fd (va_arg (args, char *), 1));
	else if ((char)*str == 'p')
		return (ft_print_address ((unsigned long)va_arg (args, void *)));
	else if ((char)*str == 'd')
		return (ft_putnbr_base (va_arg (args, int), DEC));
	else if ((char)*str == 'i')
		return (ft_putnbr_base (va_arg (args, int), DEC));
	else if ((char)*str == 'u')
		return (ft_putnbr_base (va_arg (args, unsigned int), DEC));
	else if ((char)*str == 'x')
		return (ft_putnbr_base (va_arg (args, unsigned int), HEXS));
	else if ((char)*str == 'X')
		return (ft_putnbr_base (va_arg (args, unsigned int), HEX));
	else
		write (1, str, 1);
	return (1);
}

int	ft_printf(const char *str, ...)
{
	va_list	args1;
	int		counter;
	int		i;

	i = 0;
	counter = 0;
	if (!str)
		return (-1);
	va_start(args1, str);
	while (str[i] != '\0')
	{
		if ((char)str[i] == '%' && str[i + 1])
		{
			i++;
			counter += ft_print_clasifier((str + i), args1);
		}
		else
		{
			write (1, (str + i), 1);
			counter++;
		}
		i++;
	}
	va_end(args1);
	return (counter);
}
