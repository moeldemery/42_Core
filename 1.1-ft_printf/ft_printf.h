/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ftprintf.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 13:40:07 by meldemir          #+#    #+#             */
/*   Updated: 2025/12/01 13:40:09 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>
# include "libft/libft.h"
# define DEC	"0123456789" 
# define HEXS	"0123456789abcdef"
# define HEX	"0123456789ABCDEF"

size_t	ft_putnbr_base(long long nbr, char *base);
int		ft_printf(const char *str, ...);
size_t	ft_putnbr_base_unsigned(unsigned long long nbr, char *base);
int		ft_print_address(unsigned long addr);
int		ft_print_clasifier(const char *str, va_list args);

#endif