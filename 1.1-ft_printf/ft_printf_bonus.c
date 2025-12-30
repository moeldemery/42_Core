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
#include "ft_printf_bonus.h"

size_t	ft_check_format(const char **str, va_list *args1)
{
	if (**str == '%' && *(*str + 1))
	{
		(*str)++;
		return (ft_print_clasifier_bonus(str, args1));
	}
	return (write(1, (*str), 1));
}

int	ft_print_clasifier(const char *str, va_list *args, t_flags f)
{
	if ((char)*str == '%')
		return (ft_print_percent_bonus(f));
	else if ((char)*str == 'c')
		return (ft_print_char_bonus(va_arg(*args, int), f));
	else if ((char)*str == 's')
		return (ft_print_str_bonus(va_arg(*args, char *), f));
	else if ((char)*str == 'p')
		return (ft_print_add_b((unsigned long)va_arg(*args, void *), f));
	else if ((char)*str == 'u')
		return (ft_print_u_int_bonus(va_arg(*args, unsigned int), f));
	else if ((char)*str == 'd' || (char)*str == 'i')
		return (ft_print_int_bonus(va_arg(*args, int), f));
	else if ((char)*str == 'x' || (char)*str == 'X')
		return (ft_print_hex_bonus(va_arg(*args, unsigned int), *str, f));
	else
		return (0);
}

int	ft_print_clasifier_bonus(const char **str, va_list *args2)
{
	t_flags	f;

	f = (t_flags){0, 0, 0, 0, 0, 0, -1};
	ft_flag_parser(str, &f);
	if (ft_isdigit(**str))
		f.width = ft_atoi(*str);
	while (ft_isdigit(**str))
		(*str)++;
	if (**str == '.')
	{
		(*str)++;
		f.padding = ft_atoi(*str);
		while (ft_isdigit(**str))
			(*str)++;
	}
	if (f.plus)
		f.space = 0;
	return (ft_print_clasifier (*str, args2, f));
}

int	ft_printf(const char *str, ...)
{
	va_list	args1;
	int		counter;

	counter = 0;
	if (!str)
		return (-1);
	va_start(args1, str);
	while (*str)
	{
		if (*str == '%')
			counter += ft_check_format(&str, &args1);
		else
			counter += write(1, str, 1);
		str++;
	}
	va_end(args1);
	return (counter);
}
